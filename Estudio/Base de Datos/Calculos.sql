--Retorna el valor absoluto de un número (sirve para entregar el positivo de un valor negativo.
select abs(-58) from dual;
select abs(-86) from dual;


-----

--Redondea al valor entero siguiente. NO SIGUE LA REGLA DE APROCIMAR DESDE ".5". 
select ceil(3.94) from dual;
select ceil(3.10) from dual;


-----

--Lo mismo que CEIL, pero al contrario, redondea hacia abajo.
select floor(12.54) from dual;
select floor(12.80) from dual;

-----

--Retorna en resto de una división, lo sobrante cuando una división no es "perfecta", se suele usar con el valor 2 para saber si un número es par o no.
select mod(10,3) from dual;
select mod(10,2) from dual;

-----

--La potencia de un número. El primer parámetro es la base y el segundo el exponente.
select power(2,4) from dual;
select power(2,3) from dual;

-----

--Redondea a la cantidad de decimales expresadas como un número en el 2do parámetro, en caso de que no haya aproximará al número entero directamente.
select round(3.94) from dual;
select round(3.94,1) from dual;

--Si el 2do parámetro es negativo aproximarpa los valores enteros, partiendo por la unidad, decena, centena, etc)
select round(1234,-2) from dual;
select round(1234,-3) from dual;

-----

--Retorna "1" si el parámetro es positivo, "-1" si es negativo (se puede poner ejercicios de calculo en el espacio de parámetro).
select sign(120) from dual;
select sign(-120) from dual;
select sign((120*5/2)-1000) from dual;
select sign((120*18/2)-1000) from dual;

-----

--TRUNC dejará la cantidad de decimales especificadas en el 2do parámetro.
--Si no se pone el 2do parámetro cortará todos los decimales dejando solo el valor entero (no redondea ni aproxima).
select trunc(1234.56) from dual;
select trunc(1234.56,1) from dual;

--En caso de que el 2do parámetro sea negativo, deja en 0 los valores partiendo desde la unidad, decena, centena, etc.
select trunc(1234.56,-1) from dual;

-----

--Muestra la raíz cuadrada del parámetro.
select sqrt(9) from dual;
select sqrt(18) from dual;

-----

--Ejercicios matemáticos:

--1. Obtener nombre y apellido de todos los empleados con id par.
select first_name, last_name from employees
where mod(employee_id,2) = 0;

--2. Cuál es la raíz cuadrada del salario de los empleados que trabajan en el departamento IT.
select sqrt(salary) from employees
inner join departments on departments.department_id = employees.department_id
where department_name = 'IT';

--3. Muestre nombre y salario de los empleados que la raíz cuadrada de su salario sea superior a 100.
select first_name, salary from employees
where sqrt(salary) > 100;