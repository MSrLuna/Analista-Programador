-- Crear una tabla: Define una nueva tabla en la base de datos con columnas específicas y sus tipos de datos.

CREATE TABLE nombre_tabla (
    columna1 tipo_dato,
    columna2 tipo_dato,
    -- ...
);

-- Insertar datos: Agrega nuevos registros a una tabla especificando los valores para cada columna.

INSERT INTO nombre_tabla (columna1, columna2, ...)
VALUES (valor1, valor2, ...);

-- Seleccionar datos: Recupera información de una o varias tablas basada en condiciones especificadas.

SELECT columna1, columna2
FROM nombre_tabla
WHERE condicion;

-- Actualizar datos: Modifica los valores de una o varias filas en una tabla según ciertas condiciones.

UPDATE nombre_tabla
SET columna1 = nuevo_valor
WHERE condicion;

-- Eliminar datos: Elimina filas de una tabla basándose en condiciones especificadas.

DELETE FROM nombre_tabla
WHERE condicion;

-- Crear índice: Crea un índice en una columna de una tabla para mejorar el rendimiento de las consultas.

CREATE INDEX nombre_indice
ON nombre_tabla (columna);

-- Crear vista: Define una vista virtual que actúa como una tabla derivada de una o más tablas existentes.

CREATE VIEW nombre_vista AS
SELECT columna1, columna2
FROM nombre_tabla
WHERE condicion;

-- Ejemplo de JOIN (unión): Combina filas de dos o más tablas basándose en una condición de relación.

SELECT t1.columna, t2.columna
FROM tabla1 t1
INNER JOIN tabla2 t2 ON t1.id = t2.id;

-- Funciones de agregación: Realizan cálculos en conjuntos de datos, como SUM (suma), AVG (promedio), COUNT (conteo), etc.

SELECT AVG(columna) AS promedio
FROM nombre_tabla;

-- Agrupar datos: Agrupa filas basándose en los valores de una columna y realiza operaciones de agregación en cada grupo.

SELECT columna, COUNT(*)
FROM nombre_tabla
GROUP BY columna;
