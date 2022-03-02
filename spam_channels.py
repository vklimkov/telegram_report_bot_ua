import logging
import asyncio
import datetime
import random

from telethon import errors
from telethon import functions, types

from comments_generator import CommentsGenerator
from client_factory import ClientFactory
from channels_database import ChannelsDatabase


client = ClientFactory.create_client(session_name="spam")
comments = CommentsGenerator()
sent_messages = set()
visited_channels = set()


async def main():
    channels_db = ChannelsDatabase()

    while True:
        for priority in channels_db.get_priorities():
            for telegram_channel in channels_db.channels_iterator(priority, shuffle=True):
                try:
                    # get last message in the chat if possible
                    async for message in client.iter_messages(telegram_channel, limit=1):
                        text = comments.get_random_text_comment()
                        sent = await client.send_message(telegram_channel, text, comment_to=message)
                        sent_messages.add(sent.id)
                        visited_channels.add(sent.peer_id.channel_id)
                        logging.info('Sent message to {}'.format(telegram_channel))
                except ValueError:
                    logging.info('{} channel not found'.format(telegram_channel))
                except errors.UsernameInvalidError:
                    logging.info('There is no {}'.format(telegram_channel))
                except errors.FloodWaitError as e:
                    seconds_left = e.seconds
                    while seconds_left > 0:
                        logging.info('Flood wait. Waiting for {}...'.format(str(datetime.timedelta(seconds=seconds_left))))
                        seconds_left -= 60
                        await asyncio.sleep(60)
                except errors.MsgIdInvalidError:
                    logging.info('Couldnt find last message in the chat {}. Maybe cant send to this one'.format(telegram_channel))
                except Exception as e:
                    logging.info('some other exception for {}: {}'.format(telegram_channel, str(e)))
                    await asyncio.sleep(10 + 5 * random.random())
        await asyncio.sleep(180)


with client:
    logging.basicConfig(level=logging.INFO)
    client.loop.run_until_complete(main())
