#Add a constractor for the cohort class 
class  cohort_four:
    def __init__(self,student_name,age,course_unit,start_date,end_date):
        self.student_name = student_name
        self.age = age
        self.course_unit = course_unit
        self.start_date = start_date
        self.end_date = end_date
p1 = cohort_four('Edith',20,'computer_programming','21/08/24','14/12/24')
print(p1.student_name)
print(p1.age)
print(p1.course_unit)
print(p1.start_date)
print(p1.end_date)
print(f'my name is {p1.student_name} , am {p1.age} pursucing  {p1.course_unit} and i started on {p1.start_date} and ending on {p1.end_date}')


#Add a method to the class that prints the cohort name, and the total number of students
class cohort:
    def __init__(self,cohort_name,total_number_student):
        self.cohort_name = cohort_name
        self.total_number_student = total_number_student
    def method(num):
        print(f'The name of our cohort is {num.cohort_name} and the total number of students are  {num.total_number_student}')
p1 = cohort('cohort_four',65)
p1.method()


#Create new instance of the cohort class 1
class cohort_iv:
    def __init__(self,cohort_name,cohort_size,start_date):
        self.cohort_name = cohort_name
        self.cohort_size = cohort_size
        self.start_date = start_date
p1 =cohort_iv('cohort_1', 22,'08/23')
print(p1.cohort_name)
print(p1.cohort_size)
print(p1.start_date)
print(f'The name of our  is {p1.cohort_name} and our cohort size is {p1.cohort_size} on {p1.start_date}')