
import random
import pandas as pd


class ChannelsDatabase:
    def __init__(self, path="telegram_db.csv"):
        self._db_main = pd.read_csv(path)
        self._db_main.sort_values(by=['priority'])

        self._db_grouped = self._db_main.groupby(['priority'], as_index=False)['channel'].agg(lambda x: list(x))

    def get_priorities(self):
        return list(self._db_grouped['priority'])

    def channels_iterator(self, priority, shuffle=False):
        channels = self._db_grouped[self._db_grouped['priority'] == priority]['channel'].tolist()[0]
        if shuffle:
            random.shuffle(channels)
        for telegram_channel in channels:
            if "https://" in telegram_channel:
                telegram_channel = telegram_channel.split('/')[-1]
            elif '@' in telegram_channel:
                telegram_channel = telegram_channel[1:]
            yield telegram_channel

