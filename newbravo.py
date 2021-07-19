table = '''
CREATE TABLE courses (
'course_code' VARCHAR(20) NOT NULL,
'course_name' VARCHAR(50) NOT NULL,
PRIMARY KEY(course_code)
);

CREATE TABLE students (
'id' VARCHAR(9) NOT NULL,
'name' VARCHAR(50) NOT NULL,
'gender' VARCHAR(10) NOT NULL,
'yearlevel' INT(1) NOT NULL,
'course' VARCHAR(20) NOT NULL,
PRIMARY KEY(id)
FOREIGN KEY (course) REFERENCES courses(course_code)
)
'''

