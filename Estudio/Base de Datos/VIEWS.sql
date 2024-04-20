--Las VISTAS no son más que SELECT's que quedan guardados en un objeto de Oracle llamado VIEW
--te darás cuenta que las vistas son como una especie de tablas virtuales.
create view v_empleados_it as
select first_name, last_name, email, department_name from employees
inner join departments on departments.department_id = employees.department_id
where department_name = 'IT';

--Podemos consultar los datos de una VISTA tal cual como si fuera una tabla.
select * from v_empleados_it where first_name = 'Diana';

--Alterar para permitir cambios en la vista hay que borrar y volver a crear con las modificaciones.
drop view v_empleados_it;