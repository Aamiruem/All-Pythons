import random

class KBCGame:
    def __init__(self):
        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "Who wrote 'Romeo and Juliet'?",
            # Add more questions as needed
        ]

        self.options = [
            ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
            ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"],
            # Add options corresponding to each question
        ]

        self.correct_answers = ['A', 'B', 'A']  # Update with correct answers
        self.current_question_index = 0
        self.total_questions = len(self.questions)
        self.user_score = 0

    def display_question(self):
        print("\n" + self.questions[self.current_question_index])
        for option in self.options[self.current_question_index]:
            print(option)
        print("Your answer (Enter A, B, C, or D): ")

    def get_user_answer(self):
        user_answer = input("Enter your answer: ").upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ").upper()
        return user_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answers[self.current_question_index]

    def get_correct_answer(self):
        return self.options[self.current_question_index][ord(self.correct_answers[self.current_question_index]) - ord('A')]

    def play_game(self):
        print("Welcome to Kaun Banega Crorepati!")
        print("Answer the following questions to win.")

        while self.current_question_index < self.total_questions:
            self.display_question()

            user_answer = self.get_user_answer()

            if self.check_answer(user_answer):
                print("Correct! You earned 1000 points.")
                self.user_score += 1000
            else:
                print("Incorrect! The correct answer is", self.get_correct_answer())
                break  # End the game if the answer is incorrect

            self.current_question_index += 1

        print("Game over! Your total score is:", self.user_score, "points.")

if __name__ == "__main__":
    kbc_game = KBCGame()
    kbc_game.play_game()
