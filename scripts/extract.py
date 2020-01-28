import datetime
a = """Turing: DOJ: 22 Aug 2017 | Subjects: Math, English | Salary: 18 LPA in hand | Also takes Web lectures.
Dinho: DOJ: 1 Jan 2016 | Subjects: Sports, Health Science | Salary: 25 LPA in hand
Adele:  DOJ: 1 Mar 2015 | Subjects: English | Salary: 10 LPA in hand
Freddie: DOJ: 1 Aug 2017 | Subjects: Music, English | Salary: 20 LPA in hand | Also takes Web lectures.
Dalton: DOJ: 1 Mar 2017 | Subjects: Botany, Zoology | Salary: 9 LPA in hand | Also takes Web lectures.
Harish: DOJ: 1 Feb 2017 | Subjects: Math, Science | Salary: 18 LPA in hand
Trump: DOJ: 1 Aug 2017 | Subjects: Political Science, Business Administration, Foreign Affairs | Salary: 8 LPA in hand
Swaraj: DOJ: 1 Sept 2019 | Subjects: Foreign Affairs, Negotiations | Salary: 28 LPA in hand | Also takes Web lectures.
Socrates: DOJ: 1 June 2015 | Subjects: Philosophy, Moral Science | Salary: 11.5 LPA in hand | Also takes Web lectures."""
lines = a.split('\n')
months = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'June':6,
    'July':7,
    'Aug':8,
    'Sept':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
}
for line in lines:
    if not line:
        continue
    all_entities = line.split(' | ')
    nameAndDoj = all_entities[0].split(': ')
    name = nameAndDoj[0]
    Doj = nameAndDoj[2]
    dArr = Doj.split(' ')
    dArr[1] = months[dArr[1]]
    date = datetime.date(int(dArr[2]), dArr[1], int(dArr[0]))
    subjects = all_entities[1]
    subjects = subjects.split(': ')[1]
    salary = all_entities[2]
    salary = salary.split(': ')[1]
    if len(all_entities) > 3:
        web_lecture_capability = 'yes'
    else:
        web_lecture_capability = 'no'
    # print('{} {} {} {} {}'.format(name, date, subjects, salary, web_lecture_capability))
    print('{} {} {}'.format(subjects, name, salary))

