from ..models import School, Teacher, Class, ClassRoom, Student, User
import datetime
'''

Create classrooms that teaches two subjects for all teachers.
Each student will study 4 different classes.
Each class will hold 15 students for now.
'''


def create_classes_and_class_rooms():
    teachers = Teacher.objects.filter(school_id=1).prefetch_related('subjects')
    total_classes = 60
    class_room = ClassRoom.objects.create(name='class 1', school_id=1)
    classes_added = 0
    class_index = 1
    classes = []
    for teacher in teachers:
        for subject in teacher.subjects.all():
            cls = Class()
            cls.subject = subject
            cls.taught_by = teacher
            # cls.per_class_duration = 60
            # cls.totalDuration = cls.per_class_duration * total_classes
            cls.cls = class_room
            classes.append(cls)
            classes_added += 1
            if classes_added == 2:
                class_index += 1
                classes_added = 0
                class_room = ClassRoom.objects.create(name='class '+str(class_index), school_id=1)

    Class.manager.bulk_create(classes)

def create_students(standard, classes, student_index):
    student_count = 15
    current_index = student_index
    students = []
    for i in range(student_count):
        student = Student()
        user = User()
        student.doj = datetime.date(1970, 1, 1)
        user.name = 'Student '+str(current_index)
        user.save()
        student.user = user
        student.ranking = current_index
        student.roll_num = current_index
        student.standard = standard
        student.save()
        student.cls.add(*classes)
        current_index += 1
    return current_index


def create_class_mappings():
    classes = Class.manager.all()
    class_index = 0
    standard = 1
    student_index=1
    class_count = Class.manager.all().count()
    while(class_index < class_count):
        if class_index + 4 < class_count:
            student_index = create_students(standard, classes[class_index:class_index+4], student_index)
            class_index +=4
            standard += 1
        else:
            classlist = classes[class_index:]
            class_index+=len(classlist)+1
            student_index = create_students(standard, classlist, student_index)




def run():
    create_classes_and_class_rooms()
    create_class_mappings()