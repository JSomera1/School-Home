import random


class Question:
    def __init__(self, text, correct, incorrect, cat, diff):
        if diff not in ("easy", "medium", "hard"):
            #raises an exception 
            raise AttributeError

        self.difficulty = diff
        self.category = cat
        self.question = text
        self.answers = incorrect + [correct]
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct) + 1

    def __str__(self):
        return "\n".join(
            [self.question]
            + [f"{num}: {answer}" for num, answer in enumerate(self.answers, 1)]
        )

    def __eq__(self, answer):
        if type(answer) is int:
            return answer == self.answer_id
        elif type(answer) is str:
            if answer.isnumeric():
                return int(answer) == self.answer_id

        return False

    @property
    def correct_answer(self):
        return self.answers[self.answer_id - 1]

    __repr__ = __str__
    # def __repr__(self):
    #     return self.__str__()


if __name__ == "__main__":
    question1 = Question("Who am I?", "Tim", ["not", "wrong", "bad"], "People", "easy")
    print(question1.answers)
    print(question1)
