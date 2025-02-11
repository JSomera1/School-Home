import json
import random
from question import Question


class QuestionLibrary:
    def __init__(self, filename):
        with open(filename, "r") as fp:
            data = json.load(fp)

        self.questions = [
            Question(
                elem["question"],
                elem["correct_answer"],
                elem["incorrect_answers"],
                elem["category"],
                elem["difficulty"],
            )
            for elem in data
        ]

    def __len__(self):
        return len(self.questions)

    def get_categories(self):
        return list(set([q.category for q in self.questions]))

    def get_questions(self, category=None, difficulty=None, number=None):
        if difficulty not in ("easy", "medium", "hard"):
            difficulty = None

        filtered = self.questions.copy()

        if difficulty:
            filtered = [q for q in filtered if q.difficulty == difficulty]

        if category:
            filtered = [q for q in filtered if q.category == category]

        random.shuffle(filtered)

        if number:
            filtered = filtered[:number]

        return filtered
