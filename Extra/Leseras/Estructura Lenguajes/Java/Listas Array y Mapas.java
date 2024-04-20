import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Listas (ArrayList)
List<String> frutas = new ArrayList<>();
frutas.add("manzana");
frutas.add("banana");
System.out.println(frutas.get(0));  // Acceso al primer elemento

// Diccionarios (Map)
Map<String, Object> persona = new HashMap<>();
persona.put("nombre", "Carlos");
persona.put("edad", 30);
System.out.println(persona.get("nombre"));  // Acceso al valor por clave

//En Java, las listas se implementan utilizando la interfaz List (por ejemplo, ArrayList), y los diccionarios se implementan utilizando la interfaz Map (por ejemplo, HashMap).
//Puedes acceder a elementos de una lista utilizando índices numéricos y a elementos de un diccionario utilizando claves.