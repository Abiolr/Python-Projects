class QuizBrain:
    def __init__(self, list):
        self.number = 0
        self.list = list

    def still_has_questions(self):
        return len(self.number) < len(self.list)

    def next_question(self):
        current_question = self.list[self.number]
        self.number +=1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        score = 0
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            score +=1
            print(f"{score}/{self.number}")
        else:
            print("that's wrong")
        print(f"the correct answer is {correct_answer}.")
