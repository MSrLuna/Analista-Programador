SET SERVEROUTPUT ON;

--A diferencia de las funciones, que su gracia est� en RETORNAR UN VALOR, los procedimientos NO hacer RETURN.
--Si bien pueden hacer que un par�metro de salida vuelva con un valor dado, no es igual que hacer RETURN.
--Para qu� sirven los procedimientos? Se usan principalmente para ejecutar muchas sentencias SQL.
--Por ejemplo: podr�amos hacer un procediemiento que se encargar� de hacer una venta de productos.
--Piensa en esto: hacer una venta no es solamente hacer un insert en una tabla vewnta
--y adem�s, por qu� no, actualizar el stock del producto que est� en otra tabla. Quiz�s tambi�n se desee dejar un registro en
--otra tabla distinta sobre el proceso que est� ocurriendo.. Podr�amos resolver todo esto en programaci�n, pero Oracle te da
--la posibilidad de dejar que la BD se encargue de hacer todo esto.

--En palabras m�s simples, un procedimiento se crear� t�picamente cuando necesitemos ejecutar m�s de una sentencia para un
--mismo proceso, como lo ser�a hacer una venta, que puede incluir hacer muchos INSERTS y UPDATES.

--creat table producto(id number generated always as identity primary key, nombre varchar2(40) not null, precio number not null, stock number not null);

--Para crear un procedimiento usaremos la siguiente expresi�n: CREATE OR REPLACE PROCEDURE nombreProcedimiento() AS.
--Los par�ntesis nos sirven para indicar si el procedimiento recibir� par�metro(s)..

--Cambiar nombres como recomendaci�n (opcional).
create or replace procedure p_insertar_producto(p_nombre varchar2, p_precio number, p_stock number) as

begin
    insert into producto(nombre, precio, stock) values (p_nombre, p_precio, p_stock);
end;
/

--Para llamar y ejecutar un procedimiento ateponemos la palabra EXECUTE.
execute p_insertar_producto('Lechuga', 1000, 200);

--Comprobamos.
select * from producto;

--Ejercicio 1: modificar el procedimiento p_insertar_producto para que NO inserte producto que superen los $10.000.
--Si el precio entregado es superior a los $10.000 responder con un mensaje DBMS_OUTPUT indicando el problema.

create or replace procedure p_insertar_producto(p_nombre varchar2, p_precio number, p_stock number) as

begin
    if p_precio > 10000 then
        dbms_output.put_line('Precio muy alto');
    else
        insert into producto(nombre, precio, stock) values (p_nombre, p_precio, p_stock);
    end if;
end;
/

execute p_insertar_producto('Apio', 13000, 200);

--Ejercicio 2: crear el procedimiento llamado p_actualizar_precio que recibiendo por par�metro el ID y el precio nuevo.

create or replace procedure p_actualizar_precio(p_id number, p_precio number) as

begin
    update producto set precio = (p_precio) where id = (p_id);
end;
/

execute p_actualizar_precio(3, 500);

select * from producto;

--Ejercicio 3: crear el procedimiento llamado p_actualizar_precio que recibiendo por par�metro el nombre y el precio nuevo.
--Primero, verificar que el nombre recibido por par�metro exista en la BD. Si no existe, entragar un mensaje de error con DBMS.
--Si es que s� existe el producto seg�n el nombre entregado, hacer la actualizaci�n.

create or replace procedure p_actualizar_precio(p_nombre varchar2, p_precio number) as

idProducto number;

begin
    --A partir del nombre que nos llegue por par�metro hacemos un SELECT.. as� podemos verificar si existe en nuestra tabla.
    --Si el SELECT NO RETORNA ninguna fila (o sea, no hay ning�n producto con ese nombre), va a lanzar una exception.
    --Las EXCEPTION's son graves porque detienen el funcionamiento de nuestro programa.. entonces tenemos que capturarlas.
    --Cuando ocurre una exception, Oracle saltar� a la l�nea que captura las excepciones.
    select id into idProducto from producto where nombre = p_nombre;
    update producto set precio = p_precio where id = idProducto;
    
    exception 
        --Como EXCEPTION hay muchas, hay que especificar con WHEN THEN la exception espec�fica que est�s usando.
        when no_data_found then
            dbms_output.put_line('No exite el producto ' || p_nombre);
end;
/

execute p_actualizar_precio('T�mate', 300);

select * from producto;

--Ejercicio 4: agregar a p_actualizar precio la validaci�n de que no puede actualizar a m�s de $10.000.

create or replace procedure p_actualizar_precio(p_nombre varchar2, p_precio number) as

idProducto number;

begin
    if p_precio > 10000 then
        dbms_output.put_line('Precio muy alto');
    else
        select id into idProducto from producto where nombre = p_nombre;
        update producto set precio = p_precio where id = idProducto;
    end if;

    exception 
        when no_data_found then
            dbms_output.put_line('No exite el producto ' || p_nombre);
end;
/

execute p_actualizar_precio('T�mate', 300);

select * from producto;