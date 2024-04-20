--Para sumar meses a una fecha, usaremos ADD_MONTHS().
--P1: es la fecha a la que queremos sumar meses.
--P2: la cantidad de meses a sumar, si pasamos un valor un negativo.
select add_months('05/07/2020', 1) from dual;

-----

--LAST_DAY retorna el �ltimo d�a del mes de la fecha que le entreguemos.
select last_day('25/10/2023') from dual;

-----

--Retorna el n�mero de meses(como valor decimal) de diferencia entre 2 fechas.
--Para tener un valor positivo como resultado, poner siempre la fecha m�s reciente 1ero, despu�s la fecha m�s antigua.
select months_between('23/06/2003','23/09/2002') from dual;

-----

--Retorna la fecha del siguiente d�a(P2) que indiquemos.
--Por ejemplo, si quiero saber qu� d�a ser� el pr�ximo martes, a partir de hoy 25 de octubre de 2023.
--CUIDADO con los d�as MI�RCOLES y S�BADO porque llevan tilde.
select next_day('25/10/2023', 'Martes') from dual;

-----

--La fecha de hoy.
select current_date from dual;

--Fecha + hora, minuto, segundo y mil�sima de segundo + zona horaria.
select current_timestamp from dual;

-----

--Lo mismo que CURRENT_DATE, pero usa la fecha del servidor Oracle.
select sysdate from dual;

--Lo mismo que CURRENT_TIMESTAMP, pero con SYSDATE.
select systimestamp from dual;

-----

--Pasar texto a fecha (el formato se pone en el P2.
select to_date('01-ENE-2023', 'DD-MON-YY') from dual;

--Pasar de fecha a texto.
select to_char('01/10/2023')from dual;

-----

--Extraer una parte a una fecha (P1 la parte a extraer, P2 la fecha.
select extract(day from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(year from sysdate) from dual;

--Si queremos sumar o restar d�as a una fecha, no es necesario usar ninguna funci�n, simplemente se suma/resta a la fecha directamente.
select sysdate + 1 from dual;