-- Las funciones SIEMPRE RETORNAN UN VALOR. Esto quiere decir, que NO sirven para devolver los resultados de una consulta.
-- Como retornan un valor, sirven para obtener SOLO UN VALOR a partir de algo que le pasemos.
-- Por ejemplo, ya manejamos el uso de funciones que est?n pre programadas por Oracle, como INSTR, TRANSLATE, REPLACE, SUBSTR,
-- POWER, SQRT, etc.. Las funciones que nosotros crearemos son EXACTAMENTE IGUALES.. deber?n retornar UN VALOR.
-- Pueden ser usadas cuando se necesite obtener UN valor, por ejemplo en una columan de un SELECT, en un WHERE, en un IF, etc.

-- Para crear una funci?n usaremos las palabras CREATE FUNCTION nombreFuncion
-- Adem?s, si la funci?n recibe par?metros, deben ponerse dentro de par?ntesis que ir?n justo despu?s del nombre de la funci?n
-- Los par?metros siguen el orden de toda variable en Oracle: nombreVariable tipoDato
CREATE OR REPLACE FUNCTION f_incrementar_10(numero NUMBER)
-- Despu?s de los par?metros, usaremos las palabras RETURN tipoDato IS, donde tipoDato ser? el tipo de dato que retornar?
-- la funci?n que estemos creando.. por ejemplo, para esta funci?n, qu? tipo de dato debemos decir que retorna??
RETURN NUMBER IS
-- Despu?s de IS y antes de BEGIN podemos crear todas las variables que queramos.. es similiar a lo que ir?a entre
-- DECLARE y BEGIN en un bloque an?nimo
-- Cuando termines de declarar tus variables, o si no declaras ninguna, debes poner ahora la palabra BEGIN
BEGIN
    -- TODAS las funciones deben tener un RETURN al final de la l?gica del c?digo
    RETURN numero + 10;
END;
/

SELECT f_incrementar_10(40) FROM dual;

-- EJERCICIO: Inventar una funci?n que concatene 2 palabras (SIN USAR CONCAT, pero s? puede usar ||)
CREATE OR REPLACE FUNCTION f_concatenar (texto1 VARCHAR2, texto2 VARCHAR2)
RETURN VARCHAR2 IS
BEGIN
    RETURN texto1 || texto2;
END;
/

SELECT f_concatenar('Ya hice la evaluaci?n docente. ', 'Evalu? muy bien a mi profesor') FROM dual;

-- EJERCICIO: crear una funci?n que retorne el cuadrado de un n?mero (NO USAR POWER).
CREATE OR REPLACE FUNCTION f_cuadrado_numero (numero NUMBER)
RETURN NUMBER IS
BEGIN
    RETURN numero * numero;
END;
/

SELECT f_cuadrado_numero(5) FROM dual;

-- EJERCICIO: crear una funci?n que retorne "ES PAR" si el n?mero recibido es par, o "IMPAR" si no lo es (usar MOD).
CREATE OR REPLACE FUNCTION f_espar (numero NUMBER)
RETURN VARCHAR2 IS
BEGIN
    IF MOD(numero, 2) = 0 THEN
        RETURN 'ES PAR';
    ELSE
        RETURN 'IMPAR';
    END IF;
END;
/

SELECT f_espar(11) FROM dual;

-- EJERCICIO: recibiendo por par?metro un nombre completo (nombre y apellido), retornar solo la inicial del nombre en may?scula
-- PARTE 2: retornar la inicial del nombre y el apellido (cualquiera que se le entregue)
CREATE OR REPLACE FUNCTION f_iniciales(nombreCompleto VARCHAR2)
RETURN VARCHAR2 IS
    posicionBlanco NUMBER;
BEGIN
    SELECT INSTR(nombreCompleto, ' ') + 1 INTO posicionBlanco FROM dual;
    RETURN UPPER(SUBSTR(nombreCompleto, 1, 1) || SUBSTR(nombreCompleto, posicionBlanco, 1));
END;
/

SELECT f_iniciales('francisco pinol') FROM dual;








