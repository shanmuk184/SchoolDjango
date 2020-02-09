from .models import  Student, Teacher
from django.core.serializers import json
from django.db.models import Count
from django.db import connection
class ModelHelper(object):
    def getClassesInsideSchool(self, school_id=None):
        '''
        Since School filtering is done inside manager, Leaving school_id for now.
        Tabular preview of the classroom, subjects being taught in those classrooms, teachers using the same.
        '''
        return Student.manager.all()

    # def serialize_plain_queryset()
    def search_students_basedon_teacher_name(self, teacher_name='Turing'):
        students = Student.manager.filter(cls__taught_by__user__name=teacher_name).distinct()
        return list(students)
    #
    # def get_num_students_and_sum_of_teachers_with_salary_gt_twelve(self, salary_limit = 12.0):
    #     """
    #     Django aggregation uses joins instead of subquery.
    #      So double aggregation fails and gives unexpected value
    #     """
    #     with connection.cursor() as cursor:
    #         cursor.execute("""SELECT SUM(salary_per_annum), num_students FROM
    #         (SELECT COUNT(DISTINCT School_student.id) AS num_students
    #          FROM School_student, School_student_cls, School_Class, School_teacher
    #          WHERE School_student_cls.class_id == School_class.id
    #          AND School_student_cls.student_id == School_student.id
    #          AND School_class.taught_by_id == School_teacher.id
    #          AND School_teacher.salary_per_annum > """+str(salary_limit)+
    #          """) as num_students, School_teacher
    #          WHERE School_teacher.salary_per_annum > """+str(salary_limit))
    #         return cursor.fetchone()



    def get_total_duration_of_subject_teachers_more_than_one(self, salary_limit = 12.0):
        '''
        Right now I am printing subject details

        '''
        return list( Teacher.objects.annotate(
            subject_count = Count('subjects', distinct=True),
            student_count = Count('subjects__classes__students__id', distinct=True),
            class_count=Count('subjects__classes', distinct=True))
            .filter(subject_count__gt=1).values())