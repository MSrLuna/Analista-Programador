--dual es una tabla del sistema, en realidad no tiene ning�n valor y sirve para probar funciones con datos que no existen en ning�n sistema.

--CHR retorna a partir de un n�mero su representaci�n alfab�tica, de acuerdo a la tabla ascii.
select chr(72), chr(111), chr(108), chr(97) from dual;

--concat solo solo una palabra hay que usar CONCAT para concadenar hasta 2 datos, para m�s datos se puede meter concats a otros concat para unirlos.
select concat(concat(concat(chr(97),chr(100)),concat(chr(105),chr(111))),chr(115)) from dual;

--Los ingenieros de Oracle tambi�n inventaron el s�mbolo || que cumple la funci�n de pegar textos (como el "+" en python).
select chr(97)||chr(100)||chr(105)||chr(111)||chr(115) from dual;

-----

--La columna o valor que le pase se mostrar� solo con la primera letra en may�scula.
select initcap('hola')from dual;
select initcap(email)from employees;

--Min�culas.
select lower('Pedro')from dual;
select lower(email)from employees;

select email from employees;

--May�sculas.
select upper('Pedro')from dual;
select upper(last_name)from employees;

-----

--Si el n�mero del segundo par�metro es mayor a la cantidad de caracteres del primer par�metro, repetir� los caracteres del tercer par�metro hasta completar lo que falta para llegar al valor del segundo par�metro.
--Ejmplo: "-fin" tiene 4 caracteres, pero el segundo par�metro tiene 10, de 4 a 10 hay 6 d�gitos, entonces el tercer par�metro rellenar� hasta llegar igual a 10.
--LPAD = Left Pad, RPAD = Right Pad.
select lpad('-fin',10,'�')from dual;
select rpad('fin-',10,'�')from dual;

select lpad(first_name, 10, 'Hola ') from employees
where first_name = 'David';

select rpad(first_name,24,' es terrible pollo')from employees
where first_name = 'David';

-----

--Borrar espacios en blanco:
select '     Pedro     ' from dual;

--Izquierda LTRIM.
select ltrim('     Pedro     ') from dual;

--Derecha RTRIM.
select rtrim('     Pedro     ') from dual;

--Ambos lados TRIM.
select trim('     Pedro     ') from dual;

-----

--Cambiar nombre columna "AS (nombre)"
select trim('     Pedro     ')as x from dual;

-----

--REPLACE busca los c�racteres del primer par�metro que coincidan con el segundo par�metro y los reemplaza con los del tercer par�metro.
select replace('xxx.google.cl', 'x', 'w') from dual;

--Es sensible a may�sculas y min�sculas.
select replace('Amanda', 'a', 'o') from dual;

--No es necesario reemplazar por la misma cantidad de caracteres, incluso dejando un STR vaci�.
select replace('Paralelepipedo', 'le', 'x') from dual;
select replace('Paralelepipedo', 'le', '') from dual;

-----

--LENGTH saca la cantidad de caracteres que hay en un par�metro.
select length('Paralelepipedo') from dual;

select length('Franco Luna') from dual;

select length(first_name), first_name from employees
where first_name = 'Elizabeth';

-----

--SUBSTR cortar� una cantidad de caracteres del primer par�metro dependiendo del segundo par�metro(donde empieza) y del tercer par�metro(cu�ntos sacar).
select substr('World of Warcraft', 1, 5) from dual;
select substr('World of Warcraft', 7, 2) from dual;
select substr('World of Warcraft', 10, 8) from dual;

--Mostrar solo los �ltimos 2 caracteres del email de los empleados.
select email from employees;
select substr(email, -2), email from employees;
select substr(email, length(email)-1, 2), email from employees;

-----

--INSTR busca en el 1er par�metro la cadena del 2do par�metro, cuando la encuentra retorna la posici�n en la que encotr� la coincidencia por primera vez.
select instr('Benjam�n Campos', 'Campos') from dual;

-----

--Imaginemos ahora que quisi�ramos reemplazar de todo un texto m�s de un caracter a la vez.
--Ejemplo: cambiar las vocales por n�mero... a->1, e->2, i->3, o->4, u->5.
--Con REPLACE no podr�amos hacer esto en una sola funci�n, habr�a que llamar a REPLACE por cada vocal.
select translate('Ciudad', 'aeiou', '12345') from dual;

--Ejercicio: Cambiar todas las vocales por n�meros de los nombres de los empleados que trabajan como IT_PROG.
select translate(first_name, 'aeiou', '12345'), job_id from employees
where job_id = 'IT_PROG';
--Hacer que afecte tambi�n las may�sculas.
select translate(first_name, 'aAeEiIoOuU', '1122334455'), job_id from employees
where job_id = 'IT_PROG';