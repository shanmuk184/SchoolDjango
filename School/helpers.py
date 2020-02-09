from .models import  Student, Teacher, ClassRoom, Subject, SubjectMapping
from django.core.serializers import json
from django.db.models import Count
from django.db import connection
class ModelHelper(object):
    def getClassesInsideSchool(self, school_id=None):
        '''
        Since School filtering is done inside manager, Leaving school_id for now.
        Tabular preview of the classroom, subjects being taught in those classrooms, teachers using the same.
        '''
        return SubjectMapping.objects.all()

    # def serialize_plain_queryset()
    def search_students_basedon_teacher_name(self, teacher_name='Turing'):
        students = Student.manager.filter(cls__subjects__teacher__name=teacher_name).distinct()
        return list(students)

    def get_num_students_and_sum_of_teachers_with_salary_gt_twelve(self, salary_limit = 12.0):
        """
        Django aggregation uses joins instead of subquery.
         So double aggregation fails and gives unexpected value.
         This is wirking with sqlite perfectly. But heroku is giving me trouble.
        """
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(salary_per_annum), num_students FROM
            (SELECT COUNT(DISTINCT "School_student".id) AS num_students
             FROM "School_student", "School_classroom", "School_subjectmapping", "School_teacher"
             WHERE "School_subjectmapping".cls_id = "School_classroom".id
             AND "School_student".cls_id = "School_classroom".id
             AND "School_subjectmapping".teacher_id = "School_teacher".id
             AND "School_teacher".salary_per_annum > """+str(salary_limit)+
             """) as num_students, "School_teacher"
             WHERE "School_teacher".salary_per_annum > """+str(salary_limit))
            return cursor.fetchone()



    def get_total_duration_of_subject_teachers_more_than_one(self, salary_limit = 12.0):
        '''
        Right now I am printing subject details

        '''
        return Subject.objects.annotate(
            teacher_count = Count('classes', distinct=True),
            student_count = Count('classes__cls__student__id', distinct=True),
            class_count=Count('classes', distinct=True)).filter(teacher_count__gt=1)