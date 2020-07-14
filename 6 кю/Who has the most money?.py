'''You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".'''


def most_money(students):
    student_name = ''
    sum_student = 0
    check_all = 0
    for student in students:
        current_sum = student.fives * 5 + student.tens * 10 + student.twenties * 20
        if current_sum > sum_student:
            sum_student = current_sum
            student_name = student.name
        elif current_sum == sum_student:
            if check_all == 0:
                check_all += 2
            else:
                check_all += 1

    if check_all == len(students):
        return 'all'
