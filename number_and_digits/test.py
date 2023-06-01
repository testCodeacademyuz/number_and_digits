import requests

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")

        if response.status_code == 404:
            print("❗️ Siz kursga ro'yxatga olinmagansiz!")
        elif response.status_code == 201:
            print("❕ Sizning javobingiz muvafaqqiyatli yuborildi!")


#  A two-digit integer is given. 
# Output its first digit (the number of tens).
class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(42) == 4
    
    def test_case_2(self, solution):
        return solution(12) == 1
    
    def test_case_3(self, solution):
        return solution(88) == 8
    
    def test_case_4(self, solution):
        return solution(93) == 9
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1,
            self.test_case_2,
            self.test_case_3,
            self.test_case_4
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)


q1 = TaskOne('num_digit01', 'number_and_digits')