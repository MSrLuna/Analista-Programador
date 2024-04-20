--Para sumar meses a una fecha, usaremos ADD_MONTHS().
--P1: es la fecha a la que queremos sumar meses.
--P2: la cantidad de meses a sumar, si pasamos un valor un negativo.
select add_months('05/07/2020', 1) from dual;

-----

--LAST_DAY retorna el último día del mes de la fecha que le entreguemos.
select last_day('25/10/2023') from dual;

-----

--Retorna el número de meses(como valor decimal) de diferencia entre 2 fechas.
--Para tener un valor positivo como resultado, poner siempre la fecha más reciente 1ero, después la fecha más antigua.
select months_between('23/06/2003','23/09/2002') from dual;

-----

--Retorna la fecha del siguiente día(P2) que indiquemos.
--Por ejemplo, si quiero saber qué día será el próximo martes, a partir de hoy 25 de octubre de 2023.
--CUIDADO con los días MIÉRCOLES y SÁBADO porque llevan tilde.
select next_day('25/10/2023', 'Martes') from dual;

-----

--La fecha de hoy.
select current_date from dual;

--Fecha + hora, minuto, segundo y milésima de segundo + zona horaria.
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

--Si queremos sumar o restar días a una fecha, no es necesario usar ninguna función, simplemente se suma/resta a la fecha directamente.
select sysdate + 1 from dual;