--Estructura de los bloques an�nimos.
--PT 1 (opcional): Aqu� se declaran las variables que se utilizar�n dentro del bloque an�nimo.
declare
    --Para declarar una variable primero indicamos el nombre de la variable, despu�s el tipo y finalmente (si queremos) un valor.
    --Para asignar un valor, usaremos un ":=" ya que "=" es comparaci�n.
    --Toda l�nea debe terminar con ";".
    nombre varchar2(40);
    nombre varchar2(40):='';
    
    num1 number := 10;
    num2 number := 20;
--PT 2: Todo bloque debe tener un comienzo y un final(BEGIN y END).
begin
    --Aqu� es donde vamos a programar.
    
end
/  --Este slash ser� �til si dentro de esta misma hoja de trabajo tenemos m�s de un bloque programado.