SET SERVEROUTPUT ON;

--A diferencia de las funciones, que su gracia está en RETORNAR UN VALOR, los procedimientos NO hacer RETURN.
--Si bien pueden hacer que un parámetro de salida vuelva con un valor dado, no es igual que hacer RETURN.
--Para qué sirven los procedimientos? Se usan principalmente para ejecutar muchas sentencias SQL.
--Por ejemplo: podríamos hacer un procediemiento que se encargará de hacer una venta de productos.
--Piensa en esto: hacer una venta no es solamente hacer un insert en una tabla vewnta
--y además, por qué no, actualizar el stock del producto que está en otra tabla. Quizás también se desee dejar un registro en
--otra tabla distinta sobre el proceso que está ocurriendo.. Podríamos resolver todo esto en programación, pero Oracle te da
--la posibilidad de dejar que la BD se encargue de hacer todo esto.

--En palabras más simples, un procedimiento se creará típicamente cuando necesitemos ejecutar más de una sentencia para un
--mismo proceso, como lo sería hacer una venta, que puede incluir hacer muchos INSERTS y UPDATES.

--creat table producto(id number generated always as identity primary key, nombre varchar2(40) not null, precio number not null, stock number not null);

--Para crear un procedimiento usaremos la siguiente expresión: CREATE OR REPLACE PROCEDURE nombreProcedimiento() AS.
--Los paréntesis nos sirven para indicar si el procedimiento recibirá parámetro(s)..

--Cambiar nombres como recomendación (opcional).
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

--Ejercicio 2: crear el procedimiento llamado p_actualizar_precio que recibiendo por parámetro el ID y el precio nuevo.

create or replace procedure p_actualizar_precio(p_id number, p_precio number) as

begin
    update producto set precio = (p_precio) where id = (p_id);
end;
/

execute p_actualizar_precio(3, 500);

select * from producto;

--Ejercicio 3: crear el procedimiento llamado p_actualizar_precio que recibiendo por parámetro el nombre y el precio nuevo.
--Primero, verificar que el nombre recibido por parámetro exista en la BD. Si no existe, entragar un mensaje de error con DBMS.
--Si es que sí existe el producto según el nombre entregado, hacer la actualización.

create or replace procedure p_actualizar_precio(p_nombre varchar2, p_precio number) as

idProducto number;

begin
    --A partir del nombre que nos llegue por parámetro hacemos un SELECT.. así podemos verificar si existe en nuestra tabla.
    --Si el SELECT NO RETORNA ninguna fila (o sea, no hay ningún producto con ese nombre), va a lanzar una exception.
    --Las EXCEPTION's son graves porque detienen el funcionamiento de nuestro programa.. entonces tenemos que capturarlas.
    --Cuando ocurre una exception, Oracle saltará a la línea que captura las excepciones.
    select id into idProducto from producto where nombre = p_nombre;
    update producto set precio = p_precio where id = idProducto;
    
    exception 
        --Como EXCEPTION hay muchas, hay que especificar con WHEN THEN la exception específica que estás usando.
        when no_data_found then
            dbms_output.put_line('No exite el producto ' || p_nombre);
end;
/

execute p_actualizar_precio('Tómate', 300);

select * from producto;

--Ejercicio 4: agregar a p_actualizar precio la validación de que no puede actualizar a más de $10.000.

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

execute p_actualizar_precio('Tómate', 300);

select * from producto;