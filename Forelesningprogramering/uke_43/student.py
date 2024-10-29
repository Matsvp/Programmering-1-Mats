

class Student:
    """
    Klassen Student har attributtene first_name, last_name, age og student_id.
    """
    def __init__(self, first_name, last_name, age , student_id):
        """
        INIT kjører automatisk når et objekt av klassen Student blir opprettet.
        :param first_name: Fornavn til studenten
        :param last_name: Etternavn til studenten
        :param age: Alder til studenten
        :param student_id: Studentnummeret til studenten
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


    def enroll_in_course(self, course):
        self.courses.append(course)

    def get_total_credits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits
    
    
        
class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

