from student import Student, Course
import course_funtions as cf

nils_nilsen = Student("Nils", "Nilsen", 22, "IT676")

programering1 = Course("Prugramering 1", "ITF10219", 10)
webutvikling = Course("Webutvikling", "ITF18724",10)
design = Course("Design etc", "ITF10783", 10)

nils_nilsen.enroll_in_course(programering1)
nils_nilsen.enroll_in_course(webutvikling)
nils_nilsen.enroll_in_course(design)

print('med metode i klassen')
print(nils_nilsen.get_total_credits())

print('med ekstern funksjon')
print(cf.calculate_total_credits(nils_nilsen.courses))

all_courses = [programering1, webutvikling, design]
print(cf.calculate_total_credits(all_courses))

print(nils_nilsen.__init__.__doc__)

print(list.append.__doc__)