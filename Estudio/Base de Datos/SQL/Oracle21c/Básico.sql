select count(employee_id), job_id from employees
group by job_id;

select job_id from employees
group by job_id;|

select count(employee_id) from employees
where job_id like 'IT_PROG';

--Distinct recibe una columna, ignorará los datos repetidos y solo tomará en cuenta el priero de ellos--
select distinct(job_id) from employees
group by job_id;

-----

--SUM, COUNT, MAX, MIN, AVG, DISTINCT, HAVING--
--Mostrar promedio de salario de cada trabajo--
select avg(salary), job_id from employees
group by job_id;

--Mostrar la cantidad de empleados por nombre de departamento (mostrar nombre de departamento y cantidad)--
select count(employee_id), department_name from employees
inner join departments on departments.department_id = employees.department_id
group by department_name;

--Mostrar nombre de ciudad y mostrar el salario máximo de cada ciudad--
select max(salary), city from employees
inner join departments on departments.department_id = employees.department_id
inner join locations on locations.location_id = departments.location_id
group by city;

--Cantidad de empleados y cantidad de departamentos de todas las ciudades--
select city, count(employees.employee_id), count(distinct(departments.department_id)) from employees
inner join departments on departments.department_id = employees.department_id
inner join locations on locations.location_id = departments.location_id
group by city;

--Mostrar nombre de departamento y cantidad de empleados, siempre y cuando la cantidad de empleados sea superior a 4--
select count(employee_id), department_name from employees
inner join departments on departments.department_id = employees.department_id
group by department_name
having count(employee_id) > 4;

--Mostrar solo nombres que estén repetidos--
select count(first_name), first_name from employees
group by first_name
having count(first_name) > 1;