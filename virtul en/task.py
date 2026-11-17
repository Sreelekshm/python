CREATE PROCEDURE insert_student(
    IN p_student_id INT,
    IN p_name VARCHAR(100),
    IN p_department VARCHAR(50),
    IN p_age INT
)
BEGIN
    INSERT INTO students(student_id, name, department, age)
    VALUES(p_student_id, p_name, p_department, p_age);
END //

DELIMITER ;

START TRANSACTION;

CALL insert_student(101, 'Arun', 'Computer Science', 21);

SAVEPOINT sp1;

CALL insert_student(102, 'Meera', 'Commerce', 22);

ROLLBACK TO sp1;

COMMIT;

SELECT * FROM students;


SELECT
    d.dept_name,
    COUNT(DISTINCT s.student_id) AS student_count,
    SUM(e.fee) AS total_revenue
FROM departments d
JOIN students s ON d.dept_name = s.department
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY d.dept_name
HAVING COUNT(DISTINCT s.student_id) > 1;


SELECT
    s.name,
    s.department,
    COUNT(e.course) AS total_courses,
    SUM(e.fee) AS total_fee_paid
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name, s.department
HAVING COUNT(e.course) > 1;


CREATE VIEW student_report AS
SELECT
    s.name AS student_name,
    s.department AS department_name,
    e.course,
    e.fee
FROM students s
JOIN enrollments e ON s.student_id = e.student_id;


SELECT
    student_name,
    department_name,
    SUM(fee) AS total_fee
FROM student_report
GROUP BY student_name, department_name
HAVING SUM(fee) > 50000;


INSERT INTO students(student_id, name, department, age)
VALUES(103, 'Rahul', 'Computer Science', 23);

SELECT * FROM students;