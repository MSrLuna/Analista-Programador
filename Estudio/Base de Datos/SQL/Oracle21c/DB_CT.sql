CREATE TABLE nombre_tabla (
    columna1 TIPO_DATO1,
    columna2 TIPO_DATO2,
    ...
);

ALTER TABLE nombre_tabla
ADD nueva_columna TIPO_DATO;

ALTER TABLE nombre_tabla
MODIFY columna_existente NUEVO_TIPO_DATO;

ALTER TABLE nombre_tabla
DROP COLUMN columna_existente;

DROP TABLE nombre_tabla;

ALTER TABLE nombre_tabla
RENAME TO nuevo_nombre_tabla;

DESCRIBE nombre_tabla;

SELECT table_name FROM user_tables;

SELECT column_name, data_type
FROM user_tab_columns
WHERE table_name = 'nombre_tabla';

CREATE INDEX nombre_indice
ON nombre_tabla (columna);

DROP INDEX nombre_indice;

LOCK TABLE nombre_tabla IN EXCLUSIVE MODE;

SELECT * FROM nombre_tabla
INNER JOIN nombre_tabla2 on nombre_tabla2.nombre_columna = nombre_tabla.nombre_columna;