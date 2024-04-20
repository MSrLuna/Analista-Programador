--Retorna el valor absoluto de un n�mero (sirve para entregar el positivo de un valor negativo.
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

--Retorna en resto de una divisi�n, lo sobrante cuando una divisi�n no es "perfecta", se suele usar con el valor 2 para saber si un n�mero es par o no.
select mod(10,3) from dual;
select mod(10,2) from dual;

-----

--La potencia de un n�mero. El primer par�metro es la base y el segundo el exponente.
select power(2,4) from dual;
select power(2,3) from dual;

-----

--Redondea a la cantidad de decimales expresadas como un n�mero en el 2do par�metro, en caso de que no haya aproximar� al n�mero entero directamente.
select round(3.94) from dual;
select round(3.94,1) from dual;

--Si el 2do par�metro es negativo aproximarpa los valores enteros, partiendo por la unidad, decena, centena, etc)
select round(1234,-2) from dual;
select round(1234,-3) from dual;

-----

--Retorna "1" si el par�metro es positivo, "-1" si es negativo (se puede poner ejercicios de calculo en el espacio de par�metro).
select sign(120) from dual;
select sign(-120) from dual;
select sign((120*5/2)-1000) from dual;
select sign((120*18/2)-1000) from dual;

-----

--TRUNC dejar� la cantidad de decimales especificadas en el 2do par�metro.
--Si no se pone el 2do par�metro cortar� todos los decimales dejando solo el valor entero (no redondea ni aproxima).
select trunc(1234.56) from dual;
select trunc(1234.56,1) from dual;

--En caso de que el 2do par�metro sea negativo, deja en 0 los valores partiendo desde la unidad, decena, centena, etc.
select trunc(1234.56,-1) from dual;

-----

--Muestra la ra�z cuadrada del par�metro.
select sqrt(9) from dual;
select sqrt(18) from dual;

-----

--Ejercicios matem�ticos:

--1. Obtener nombre y apellido de todos los empleados con id par.
select first_name, last_name from employees
where mod(employee_id,2) = 0;

--2. Cu�l es la ra�z cuadrada del salario de los empleados que trabajan en el departamento IT.
select sqrt(salary) from employees
inner join departments on departments.department_id = employees.department_id
where department_name = 'IT';

--3. Muestre nombre y salario de los empleados que la ra�z cuadrada de su salario sea superior a 100.
select first_name, salary from employees
where sqrt(salary) > 100;