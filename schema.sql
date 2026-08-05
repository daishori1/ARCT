CREATE DATABASE score;

-- i drop the previus  table student to add new field  "career" and use auto increment in the id  and the time stamp auto field  ,
-- adding the courses TABLE  --

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--careers--
CREATE TABLE careers (id_career INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
 career_name VARCHAR(50), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);  
 -- example of correct insert with the new parameters --
--INSERT INTO public.careers (career_name) VALUES ('career test');--

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
--courses--
CREATE TABLE courses 
(id_course INTEGER GENERATED ALWAYS  AS IDENTITY PRIMARY KEY , 
course_name VARCHAR(40), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
-- example of correct insert with the new parameters --
--INSERT INTO public.courses ('name',)--

------------------------------------------------------------------------------------------------------------------------------------------------------------------
--studenst--
CREATE TABLE students (id_student INTEGER  GENERATED  ALWAYS AS IDENTITY PRIMARY KEY , 
name VARCHAR (40)  NOT NULL , email VARCHAR(30) UNIQUE ,  id_career INTEGER NOT NULL FOREIGN KEY 
(id_career) REFERENCES careers(id_career), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
-- example of correct insert with the new parameters --
--INSERT INTO public.students (name,email,id_career) VALUES ('jonh doe','jonh.doe@testliketest.com',1);--

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
---professors---
--same structure like students -- 
CREATE TABLE professors (id_professor INTEGER  GENERATED  ALWAYS AS IDENTITY PRIMARY KEY , 
name VARCHAR (40)  NOT NULL , email VARCHAR(30) UNIQUE ,  id_career INTEGER NOT NULL, 
FOREIGN KEY (id_career) REFERENCES careers(id_career) , register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
-- example of correct insert with the new parameters --
--INSERT INTO public.professors (name,email,career) VALUES ('test','test.doe@testliketest.com',1);--

-----------------------------------------------
--enrollments--

CREATE TABLE enrollments(id_enrollment INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY , 
id_student INTEGER NOT NULL , FOREIGN KEY (id_student) REFERENCES students(id_student), 
id_professor INTEGER NOT NULL , FOREIGN KEY (id_professor) REFERENCES professors(id_professor),
id_course INTEGER NOT NULL , FOREIGN KEY (id_course) REFERENCES courses(id_course), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP); 
-- example of correct insert with the new parameters --
--INSERT INTO public.enrollments (id_students,id_professor,id_course) VALUES (1,1,1);--

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

