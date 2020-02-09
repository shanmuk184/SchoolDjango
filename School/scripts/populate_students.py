from ..models import Teacher, Student, ClassRoom, User

import datetime
'''

Create classrooms that teaches two subjects for all teachers.
Each student will study 4 different classes.
Each class will hold 15 students for now.
'''
#
#
# def create_classes_and_class_rooms():
#     teachers = Teacher.objects.filter(school_id=1).prefetch_related('subjects')
#     total_classes = 60
#     # class_room = ClassRoom.objects.create(name='class 1', school_id=1)
#     classes_added = 0
#     class_index = 1
#     classes = []
#     for teacher in teachers:
#         for subject in teacher.subjects.all():
#             cls = Class(name='Class '+str(class_index), school_id=1)
#             cls.subject = subject
#             classes.append(cls)
#             class_index +=1
#             classes_added += 1
#     Class.manager.bulk_create(classes)

def create_students(standard, classes, student_index):
    student_count = 15
    iter_index = 1
    current_index = student_index
    students = []
    all_mappings = []
    for i in range(student_count):
        student = Student()
        student.doj = datetime.date(1970, 1, 1)
        user = User()
        user.name = 'Student '+str(current_index)
        user.save()
        student.user = user
        student.ranking = i
        student.roll_num = i
        student.standard = standard

        student.cls = classes
        all_mappings.append(student)
        current_index += 1
    Student.manager.bulk_create(all_mappings)
    return current_index


def create_class_mappings():
    classes = ClassRoom.objects.all()
    class_index = 0
    standard = 1
    student_index=1
    class_count = ClassRoom.objects.all()
    for cls in classes:
        student_index = create_students(standard, cls, student_index)
        # class_index +=4
        standard += 1




def run():
    # create_classes_and_class_rooms()
    create_class_mappings()