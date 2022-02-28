import asyncio
import configparser
import datetime
import os
import random

import pandas as pd
import questionary
from telethon import TelegramClient
from telethon import errors
from telethon import functions, types

from text_generator import generate_text

if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_id = config['TelegramApi']['api_id']
    api_hash = config['TelegramApi']['api_hash']
else:
    api_id = int(questionary.password('Api ID:').ask())
    api_hash = questionary.password('Api hash:').ask()

    config = configparser.ConfigParser()
    config['TelegramApi'] = {'api_id': api_id,
                             'api_hash': api_hash,
                             }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

client = TelegramClient('session_new', api_id, api_hash)
client.start()

print('Bot started')


async def main():
    number_of_channels_rep = 150
    number_completed = 0
    df_main = pd.read_csv('telegram_db.csv')
    df_main.sort_values(by=['priority'])

    df_grouped = df_main.groupby(['priority'], as_index=False)['channel'].agg(lambda x: list(x))
    while number_completed < number_of_channels_rep:
        for i in list(df_grouped['priority']):
            for telegram_channel in df_grouped[df_grouped['priority'] == i]['channel'].tolist()[0]:
                if "https://" in telegram_channel:
                    telegram_channel = telegram_channel.split('/')[-1]
                elif '@' in telegram_channel:
                    telegram_channel = telegram_channel[1:]
                try:
                    result = await client(functions.account.ReportPeerRequest(
                        peer=telegram_channel,
                        reason=types.InputReportReasonSpam(),
                        message=generate_text())
                    )
                    print(telegram_channel.strip(), result)
                except ValueError:
                    print("Channel not found")
                    number_completed -= 1
                except errors.UsernameInvalidError:
                    print("Nobody is using this username, or the username is unacceptable")
                except errors.FloodWaitError as e:
                    seconds_left = e.seconds
                    while seconds_left > 0:
                        print("Flood wait error. Waiting for ", str(datetime.timedelta(seconds=seconds_left)))
                        seconds_left -= 60
                        await asyncio.sleep(60)
                number_completed += 1
                await asyncio.sleep(10 + 2 * random.random())


with client:
    client.loop.run_until_complete(main())
