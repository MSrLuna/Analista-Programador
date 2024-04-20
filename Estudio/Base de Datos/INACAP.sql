--Estructura de los bloques anónimos.
--PT 1 (opcional): Aquí se declaran las variables que se utilizarán dentro del bloque anónimo.
declare
    --Para declarar una variable primero indicamos el nombre de la variable, después el tipo y finalmente (si queremos) un valor.
    --Para asignar un valor, usaremos un ":=" ya que "=" es comparación.
    --Toda línea debe terminar con ";".
    nombre varchar2(40);
    nombre varchar2(40):='';
    
    num1 number := 10;
    num2 number := 20;
--PT 2: Todo bloque debe tener un comienzo y un final(BEGIN y END).
begin
    --Aquí es donde vamos a programar.
    
end
/  --Este slash será útil si dentro de esta misma hoja de trabajo tenemos más de un bloque programado.