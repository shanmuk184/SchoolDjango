import datetime
from ..models import Teacher, Subject, School, User
data = """Turing: DOJ: 22 Aug 2017 | Subjects: Math, English | Salary: 18 LPA in hand | Also takes Web lectures.
Dinho: DOJ: 1 Jan 2016 | Subjects: Sports, Health Science | Salary: 25 LPA in hand
Adele: DOJ: 1 Mar 2015 | Subjects: English | Salary: 10 LPA in hand
Freddie: DOJ: 1 Aug 2017 | Subjects: Music, English | Salary: 20 LPA in hand | Also takes Web lectures.
Dalton: DOJ: 1 Mar 2017 | Subjects: Botany, Zoology | Salary: 9 LPA in hand | Also takes Web lectures.
Harish: DOJ: 1 Feb 2017 | Subjects: Math, Science | Salary: 18 LPA in hand
Trump: DOJ: 1 Aug 2017 | Subjects: Political Science, Business Administration, Foreign Affairs | Salary: 8 LPA in hand
Swaraj: DOJ: 1 Sept 2019 | Subjects: Foreign Affairs, Negotiations | Salary: 28 LPA in hand | Also takes Web lectures.
Socrates: DOJ: 1 June 2015 | Subjects: Philosophy, Moral Science | Salary: 11.5 LPA in hand | Also takes Web lectures.
"""
per_class_duration_in_hour = 1
total_classes = 100
total_class_duration_in_min = per_class_duration_in_hour * total_classes
date_mapping = {'Aug':8, 'Jan':1, 'Mar':3,'Feb':2,  'June':6, 'Sept':9}
subject_map = {}
def process_entities(entities):
    doj = [False, False]
    salary = [False, False]
    subjects_tu = [False, False]
    subjects = []
    teacher = Teacher()
    for (index, entity) in enumerate(entities):
        print(entity, end=' ')
        print(index)
        if index == 0:
            user = User(name=entity)
            user.save()
            teacher.user = user
        if salary[0] and not salary[1]:
            salary_parts = entity.split(' ')
            teacher.salary_per_annum = float(salary_parts[0])
            salary[1] = True

        if subjects_tu[0] and not subjects_tu[1]:
            ents = entity.split(' | ')
            subject_ents = ents[0].split(', ')
            for subject in subject_ents:
                if not subject_map.get(subject):
                    subject_map[subject] = Subject.objects.get_or_create(name=subject)[0]
                subjects.append(subject_map[subject])
            subjects_tu[1] = True
            salary[0] = True

        if doj[0] and not doj[1]:
            print('came')
            ents = entity.split(' | ')
            date = ents[0].split(' ')
            date[1] = date_mapping[date[1]]
            year = date[2]
            date[2] = date[0]
            date[0] = year
            teacher.doj = datetime.date(*list(map(int, date)))
            subjects_tu[0] = True
            doj[1] = True

        if entity == 'DOJ':

            doj[0] = True
        if doj[1] and subjects_tu[1] and salary[1]:
            teacher.web_lecture_capability = teacher.Answer.YES
    return (teacher, subjects)
def run():
    lines = data.split('\n')
    mathTrack = []
    tracks = []
    print(len(lines))
    school = School.objects.get(name='django')
    # print(lines)
    for line in lines:
        print(line)
        entities = line.split(': ')

        teachers = []
        (teacher, subjects) = process_entities(entities)
        teacher.school = school
        teacher.save()
        teacher.subjects.add(*subjects)
        print(teacher)