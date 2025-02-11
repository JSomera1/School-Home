import time
from rich import print
from question_library import QuestionLibrary


class Game:
    def __init__(
        self, category=None, difficulty=None, number=None, filename="trivia.json"
    ):
        lib = QuestionLibrary(filename)
        self.questions = lib.get_questions(category, difficulty, number)
        self.score = 0

    def play(self):
        scores = {"easy": 1, "medium": 2, "hard": 3}
        for question in self.questions:
            print(f"{'=' * 80}\n")
            print(question)
            start = time.time()
            good_input = False
            while not good_input:
                try:
                    answer = input("? ")
                except (KeyboardInterrupt, EOFError):
                    print("\nIt was fun playing! See you soon.")
                    return self.score

                if (
                    len(answer) == 1
                    and answer.isnumeric()
                    and int(answer) in (1, 2, 3, 4)
                ):
                    good_input = True

            elapsed = round(time.time() - start, 1)
            score = 0
            if question == answer:
                print(f"[bold green]Good :)[/bold green]")
                multiplier = 1
                if elapsed <= 3:
                    multiplier = 3
                elif elapsed <= 5:
                    multiplier = 2
                multiplier = 1
                score = scores[question.difficulty] * multiplier
                self.score += score
            else:
                print("[bold red]Bad :([/bold red]")
                print(f"[red]Correct answer was: {question.correct_answer}[/red]")

            print(f"Answered in {elapsed} seconds. Scored {score} points.")
        return self.score


if __name__ == "__main__":
    args = {}

    lib = QuestionLibrary("trivia.json")
    cats = lib.get_categories()
    for idx, c in enumerate(cats, 1):
        print(idx, c)
    choice = input("Select category? ")

    if choice.isnumeric() and 0 <= int(choice) - 1 <= len(cats):
        args["category"] = cats[int(choice) - 1]

    diff = input("Choose difficulty: easy, medium, or hard? ")
    if diff in ("easy", "medium", "hard"):
        args["difficulty"] = diff

    number = input("How many questions? ")
    if number.isnumeric() and int(number) > 0:
        args["number"] = int(number)

    if len(args):
        print("[bold green]Custom options:[/bold green]")
        for option, value in args.items():
            print(f"- {option}: {value}")

    print("[yellow]\nPress any key to start!\n[/yellow]")
    input()

    g = Game(**args)
    score = g.play()
    print(f"[yellow]Well done! Your score is: {score}[/yellow]")
