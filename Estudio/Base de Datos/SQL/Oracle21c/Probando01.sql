create table cliente (id int GENERATED always AS IDENTITY primary key, nombre varchar2(40) not null, apellido varchar2(40));
create table vehiculo (id int generated always as identity primary key, patente varchar2(6) not null, color varchar2(20));

alter table vehiculo add cliente_id int;

insert into cliente (nombre, apellido) values ('Emerson', 'Soto');
insert into cliente (nombre, apellido) values ('Iván', 'Lechuga');
insert into cliente (nombre, apellido) values ('Luis', 'Peralta');

insert into vehiculo (patente, color, cliente_id) values ('LLJJ80', 'Azul', 2);
insert into vehiculo (patente, color, cliente_id) values ('RRTP42', 'Blanco', 3);
insert into vehiculo (patente, color, cliente_id) values ('KBLP64', 'Rojo', 1);
insert into vehiculo (patente, color, cliente_id) values ('CDFB21', 'Gris', 2);

SELECT * FROM vehiculo;
SELECT * FROM cliente where id = 3;

select * from cliente
inner join vehiculo on vehiculo.cliente_id = cliente.id;