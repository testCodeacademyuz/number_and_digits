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
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)


# n = 54, output = 4, n = 32, output = 2, n = 20, output = 0, n = 98, output = 8
class TaskTwo(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(54) == 4
    
    def test_case_2(self, solution):
        return solution(32) == 2
    
    def test_case_3(self, solution):
        return solution(20) == 0
    
    def test_case_4(self, solution):
        return solution(98) == 8
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 55, output = 10, n = 23, output = 5, n = 99, output = 18, n = 100, output = 1
class TaskThree(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(55) == 10
    
    def test_case_2(self, solution):
        return solution(23) == 5
    
    def test_case_3(self, solution):
        return solution(99) == 18
    
    def test_case_4(self, solution):
        return solution(100) == 1
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 342, output = 3, n = 213, output = 2, n = 999, output = 9, n = 188, output = 1
class TaskFour(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(342) == 3
    
    def test_case_2(self, solution):
        return solution(213) == 2
    
    def test_case_3(self, solution):
        return solution(999) == 9
    
    def test_case_4(self, solution):
        return solution(188) == 1
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 564, output = 6, n = 213, output = 1, n = 999, output = 9, n = 188, output = 8
class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(564) == 6
    
    def test_case_2(self, solution):
        return solution(213) == 1
    
    def test_case_3(self, solution):
        return solution(999) == 9
    
    def test_case_4(self, solution):
        return solution(188) == 8
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 564, output = 15, n = 213, output = 6, n = 999, output = 27, n = 188, output = 17
class TaskSix(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(564) == 15
    
    def test_case_2(self, solution):
        return solution(213) == 6
    
    def test_case_3(self, solution):
        return solution(999) == 27
    
    def test_case_4(self, solution):
        return solution(188) == 17
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 123, output = 6, n = 542, output = 40, n = 992, output = 162
class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(123) == 6
    
    def test_case_2(self, solution):
        return solution(542) == 40
    
    def test_case_3(self, solution):
        return solution(992) == 162
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 123, output = 3, n = 542, output = 9, n = 992, output = 18, n = 100, output = 1

class TaskEight(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(123) == 3
    
    def test_case_2(self, solution):
        return solution(542) == 9
    
    def test_case_3(self, solution):
        return solution(992) == 18
    
    def test_case_4(self, solution):
        return solution(100) == 1
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 123, output = 13, n = 289, output = 19, n = 992, output = 92, n = 100, output = 10
class TaskNine(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(123) == 13
    
    def test_case_2(self, solution):
        return solution(289) == 19
    
    def test_case_3(self, solution):
        return solution(992) == 92
    
    def test_case_4(self, solution):
        return solution(100) == 10
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

# n = 123, output = 321, n = 289, output = 982, n = 992, output = 299, n = 721, output = 127
class TaskTen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_case_1(self, solution):
        return solution(123) == 321
    
    def test_case_2(self, solution):
        return solution(289) == 982
    
    def test_case_3(self, solution):
        return solution(992) == 299
    
    def test_case_4(self, solution):
        return solution(721) == 127
    
    def check(self,solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = all(test_cases)
        self.checking(tg_username, isSolved, self.homework_name)

q1 = TaskOne('num_digit01', 'number_and_digits')
q2 = TaskTwo('num_digit02', 'number_and_digits')
q3 = TaskThree('num_digit03', 'number_and_digits')
q4 = TaskFour('num_digit04', 'number_and_digits')
q5 = TaskFive('num_digit05', 'number_and_digits')
q6 = TaskSix('num_digit06', 'number_and_digits')
q7 = TaskSeven('num_digit07', 'number_and_digits')
q8 = TaskEight('num_digit08', 'number_and_digits')
q9 = TaskNine('num_digit09', 'number_and_digits')
q10 = TaskTen('num_digit10', 'number_and_digits')