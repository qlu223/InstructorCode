DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS classes;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    major TEXT
);

CREATE TABLE classes (
    class_id INT,
    section INT,
    class_name TEXT NOT NULL,
    instructor TEXT,
    -- Might be too advanced for software design students to catch, but will be helpful in comparing answers
    PRIMARY KEY (class_id, section)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    class_id INT,
    section INT,
    grade CHAR(2),
    -- Might be too advanced for software design students to catch, but will be helpful in comparing answers 
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id, section) REFERENCES classes(class_id, section)
);