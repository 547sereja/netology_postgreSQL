import psycopg2 as pg
from datetime import datetime

PARAMS = {'database': 'netology_db',
        'user': 'netology_user',
        'password': '2020',
        'host': 'localhost',
        'port': '5432'}


student = {'name': 'bob', 'gpa': 5.56, 'birth': '1988-01-31'}

# cur.execute("""
# insert into Course(course_id, course_name) values(%s, %s);
# """, ('1', 'Python'))


def create_db():  # создает таблицы
    with pg.connect(**PARAMS) as connect:
        cur = connect.cursor()
        # cur.execute('''drop table Student;
        # drop table Course''')
        cur.execute('''
        create table if not exists Student(student_id serial primary key not null,
        name varchar(100) not null,
        gpa numeric(10,2) null,
        birth timestamp with time zone null);
        
        create table if not exists Course(course_id serial primary key not null,
        course_name varchar(100) not null);''')


def add_student(student):  # просто создает студента
    with pg.connect(**PARAMS) as connect:
        cur = connect.cursor()
        cur.execute("""
        insert into Student(name, gpa, birth) values(%s, %s, %s);
        """, (student.get('name'), student.get('gpa'), student.get('birth')))


def get_student(entered_id):
    with pg.connect(**PARAMS) as connect:
        cur = connect.cursor()
        cur.execute('''
        select * from Student where student_id=%s''', (entered_id,))
    print(cur.fetchone())


def get_students(course_id):  # возвращает студентов определенного курса
    with pg.connect(**PARAMS) as connect:
        cur = connect.cursor()
        cur.execute('''
        select * from Course where course_id=%s;''', (course_id,))
    print(cur.fetchall())


def add_students(course_id, students):  # создает студентов и записывает их на курс
    with pg.connect(**PARAMS) as connect:
        cur = connect.cursor()
    pass

# def get_all():
#     with pg.connect(**PARAMS) as connect:
#         cur = connect.cursor()
#         cur.execute('''
#         select * from Student''')
#     print(cur.fetchall())

if __name__ == '__main__':

    student = {'name': 'bob', 'gpa': 5.56, 'birth': '1988-01-31'}
    #add_student(student)
    # get_all()
    get_student(9)
