-- Esta l?nea habilita la salida de datos con DBMS_OUTPUT y solo la ejecutaremos una vez, por cada ocasi?n que abramos SQLDeveloper
SET SERVEROUTPUT ON;

-- Los bloques an?nimos NO TIENEN NOMBRE (por eso son an?nimos).
-- Su utilidad se hace presente cuando necesitas resolver algo que NO podr?as hacerlo simplemente usando QUERYS, pero que
-- tampoco vas a seguir utilizando m?s adelante (como para hacer una funci?n o un procedimiento).

-- Estructura de los bloques an?nimos
-- PARTE 1 (opcional): si es necesario, aqu? se declaran las variables que se utilizar?n dentro del bloque an?nimo
DECLARE
    -- Para declarar una variable, primero indicamos el nombre de la variable, despu?s el tipo y finalmente (si queremos) un valor.
    -- Para asignar un valor, usaremos el s?mbolo := y no el s?mbolo =
    -- Toda la l?nea debe terminar con ;
    num1 NUMBER := 10;
    num2 NUMBER := 20;
    resultado NUMBER;
-- PARTE 2: todo bloque debe tener un comienzo y un final (BEGIN y END)
BEGIN
    -- Aqu? dentro es donde vamos a programar..
    resultado := num1 + num2;
    -- Para imprimir este valor, vamos a usar el comando DBMS_OUTPUT.put_line() que espera que le pasemos un texto o n?mero
    -- Este DBMS_OUTPUT.put_line() es el equivalente a PRINT de Python
    DBMS_OUTPUT.put_line('El resultado de la suma es: ' || resultado);
END;
/
-- Este slash ser? ?til si dentro de esta misma hoja de trabajo tenemos m?s de un bloque programado..

-- Los bloques tambi?n nos pueden servir para ir guardando datos singulares que vengan de una tabla
-- Cu?l es el objetivo de tener un SELECT dentro de un Bloque An?nimo?? Poder guardar un dato en una variable
DECLARE
    nombre VARCHAR2(40) := '';
BEGIN
    -- Si utilizamos un SELECT dentro de un bloque an?nimo, estamos OBLIGADOS a guardar el dato de una columna en una variable
    -- La ?nica raz?n por la que pondr?amos un SELECT dentro de un bloque an?nimo es para hacer esto
    -- CUIDADO! Recuerda que una variable solo es capaz de guardar UN VALOR. As? que tu SELECT debe retornar solo UNA FILA.
    SELECT first_name INTO nombre FROM employees WHERE employee_id = 120;
    DBMS_OUTPUT.put_line('Hola ' || UPPER(nombre));
END;
/

-- Podr?amos hacer un bloque an?nimo para actualizar datos de una tabla.

-- EJERCICIOS!!
-- Hacer un bloque an?nimo que sume 2 n?meros entregados como variables

-- Hacer un bloque an?nimo que, recibiendo como variables 3 notas, calcule el promedio final

-- Crear un bloque que retorne la cantidad de caracteres de un nombre declarado


-- Ciclos iterativos dentro de un bloque an?nimo
BEGIN
    -- Los ciclos FOR en Oracle funcionan muy parecidos a los ciclos FOR de Python
    -- La instrucci?n 1..5 indica que la variable i comenzar? el primer ciclo con el valor 1 y se ir? sumando 1 por cada ciclo
    -- hasta que llegue al valor 5. Despu?s de eso, se terminar? el ciclo.
    -- IMPORTANTE! En Python definimos el inicio y t?rmino de un bloque (como if, for, while, etc.) por el espacio tabulado
    -- que existe desde el margen. En ORACLE NO FUNCIONA DE ESA MANERA.
    -- Para determinar d?nde inicia el FOR, est? marcado por la palabra LOOP. Y termina donde pongamos END LOOP;
    FOR i IN 1..5 LOOP
        DBMS_OUTPUT.put_line(i);
    END LOOP;
END;
/

-- Recorriendo desde el 1 hasta al 10, mostrar solo los n?meros que sean PAR (resolver con MOD 2)








