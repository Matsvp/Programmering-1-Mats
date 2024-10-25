

class Student:
    def __init__(self, first_name, last_name, age , student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

nils_nilsen = Student("Nils", "Nilsen", 22, "IT123")
anne_annesen = Student("Anne", "Annesen", 21, "IT124")

print(f'{nils_nilsen.first_name} {nils_nilsen.last_name} er {nils_nilsen.age} år gammel og har student id {nils_nilsen.student_id}')
print(f'{anne_annesen.first_name} {anne_annesen.last_name} er {anne_annesen.age} år gammel og har student id {anne_annesen.student_id}')
