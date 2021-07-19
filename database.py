import sqlite3

conn = sqlite3.connect("newbravo.db")
cur = conn.cursor()


def allStudent():
    cur.execute('''SELECT * FROM students''')
    students = cur.fetchall()
    students = [list(i) for i in students]
    return students


def allCourses():
    cur.execute('''SELECT * FROM courses''')
    courses = cur.fetchall()
    courses = [list(i) for i in courses]
    return courses


def allCourseCode():
    cur.execute('''SELECT course_code FROM courses''')
    cc = cur.fetchall()
    cc = [list(i) for i in cc]

    # extracting course_code
    for i in range(len(cc)):
        cc[i] = cc[i][0]

    return cc


def existingID():
    cur.execute('''SELECT id FROM students''')
    id = cur.fetchall()
    id = [list(i) for i in id]

    for i in range(len(id)):
        id[i] = id[i][0]

    return id


def recordNewStudent(id, name, gender, year, course):
    cur.execute('''
    INSERT INTO students(id, name, gender, yearlevel, course)
    VALUES(?,?,?,?,?)
    ''', (id, name, gender, year, course))
    conn.commit()


def updateStudent(id, name, gender, year, course):
    cur.execute('''
    UPDATE students
    SET name=?,gender=?,yearlevel=?,course=?
    WHERE id=?
    ''', (name, gender, year, course, id))
    conn.commit()


def searchResult(input):
    try:
        key = input.lower()
    except:
        key = input

    data = allStudent()

    result = []
    for i in data:
        items = [i[0], i[1].lower()]
        for j in items:
            if key in j:
                result.append(i)
    return result


def deleteStudent(id):
    cur.execute('''
    DELETE FROM students
    WHERE id = ?
    ''', (id,))
    conn.commit()


def existingcode():
    cur.execute('''SELECT course_code FROM courses''')
    id = cur.fetchall()
    id = [list(i) for i in id]

    for i in range(len(id)):
        id[i] = id[i][0]

    return id





def recordNewCourse(code, name):
    cur.execute('''
        INSERT INTO courses(course_code, course_name)
        VALUES(?,?)
        ''', (code, name))
    conn.commit()


def updateCourse(code, name):
    cur.execute('''
    UPDATE courses
    SET course_name=?
    WHERE course_code=?
    ''', (name, code))
    conn.commit()

def deleteCourse(code):
    cur.execute('''
    DELETE FROM courses
    WHERE course_code = ?
    ''', (code,))
    conn.commit()
