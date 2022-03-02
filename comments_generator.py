
import os
import glob
import json
import random


class CommentsGenerator:
    def __init__(self, utterances_path="comments/text_comments.txt", json_dir="comments/jsons"):
        with open(utterances_path, 'r') as fp:
            self._utterances = [x.strip() for x in fp.readlines()]
        self._jsons = list(glob.glob(os.path.join(json_dir, "*.json")))

    def get_random_text_comment(self):
        return random.choice(self._utterances)

    def get_random_media_comment(self):
        path = random.choice(self._jsons)
        with open(path, 'r') as fp:
            res = json.load(fp)
        return res

