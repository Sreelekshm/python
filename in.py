BEGIN
    INSERT INTO students (student_id, name, department, age)
    VALUES (p_student_id, p_name, p_department, p_age);
END //

DELIMITER ;

START TRANSACTION;

CALL insert_student(101, 'Arun', 'Computer Science', 21);

SAVEPOINT sp1;

CALL insert_student(102, 'Meera', 'Commerce', 22);

ROLLBACK TO SAVEPOINT sp1;

COMMIT;

SELECT * FROM students;

