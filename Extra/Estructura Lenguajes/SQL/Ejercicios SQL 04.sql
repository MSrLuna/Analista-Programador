--EJERCICIOS.

--1. CUÁL ES LA RAÍZ CUADRADA DEL SALARIO DE NEENA KOCHHAR. REDONDEAR CIFRA A UN VALOR ENTERO.
select round(sqrt(salary)) from employees
where first_name = 'Neena' and last_name = 'Kochhar';

--2. OBTÉN EL SEGUNDO NOMBRE DE TU NOMBRE COMPLETO. TRANSFÓRMALO TODO A MAYÚSCULAS.
select upper(extract('Adriel' from 'Franco Adriel Luna Angulo')) from dual;

--3. CUÁNTOS MESES HAN PASADO DESDE EL FAMOSO TERROMOTO 27F ?? CORTAR EL VALOR PARA QUE SOLO SEA ENTERO.
select floor(months_between(sysdate, '27/FEB/2010')) from dual;

--4. CUÁL FUE EL ÚLTIMO DÍA DEL MES DE LA FECHA DE CONTRATACIÓN DE DANIEL FAVIET.
select first_name, last_name, last_day(hire_date) from employees
where first_name = 'Daniel' and last_name = 'Faviet';

--5. CUÁNTOS MESES FALTAN PARA EL PRÓXIMO MUNDIAL (19 de julio de 2026)?? REDONDEAR EL VALOR DEL MES AL PRIMER DECIMAL.
select round(months_between('19/JUL/2026', sysdate), 1) from dual;

--6. MOSTRAR LAS FECHAS DE TÉRMINO DE TRABAJO QUE CAIGAN EN DÍAS PAR.
select to_date(end_date) from job_history
where mod(extract(day from end_date), 2)=0;

--7. CONCATENE EL NOMBRE + _ + CIUDAD DE LOS EMPLEADOS QUE TRABAJAN EN IT.
select concat(first_name, concat('_', city)) from employees
inner join departments on departments.department_id = employees.department_id
inner join locations on locations.location_id = departments.location_id
where departments.department_id = 'IT';