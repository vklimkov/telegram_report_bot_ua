
import random


class CommentsGenerator:
    def __init__(self, utterances_path="comments/text_comments.txt"):
        with open(utterances_path, 'r') as fp:
            self._utterances = [x.strip() for x in fp.readlines()]

    def get_random_text_comment(self):
        return random.choice(self._utterances)
