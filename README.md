# Parcial-2
Ejercicio de Recolección y Acopio - Parcial #2

# Manual de Usuario - Sistema de Gestión de Recolección y acopio de Residuos.

Este manual de usuario proporciona una guía detallada sobre cómo utilizar el Sistema de Recolección y acopio de Residuos. El sistema permite registrar empleados, crear camiones de recolección y realizar la recolección de residuos.

## Requisitos Previos

- Python 3.x instalado en el sistema.
- Conocimientos básicos de programación en Python.
- Unittest (Prueba Unitaria)
- Visual Studio Code (Editor de Código)

## Configuración del Entorno

1. Clona o descarga el repositorio del Sistema de Recolección y acopio de Residuos.
2. Abre una terminal y navega hasta el directorio raíz del proyecto.

## Pasos para Utilizar el Sistema

1. Ejecutar el programa principal:
   ```
   python main.py
   ```

2. Inicia Programa:
   - Cuando se te pida debes presionar la opción 1. Si, 2. No, para iniciar el programa.

3. Crear camiones de recolección: 
   - Cuando se te solicite, ingresa el modelo y el ID del camión que deseas crear.
   - Se te pedirá que registres los empleados asociados a ese camión, 
   - ingresa los datos del conductor del camión, incluyendo el ID, nombre y edad.
   - A continuación, ingresa los datos de los dos acompañantes del camión, también especificando su ID, nombre y edad.
   - Repite estos pasos para cada camión y sus respectivos empleados.

4. Establecer Geolocalización:
   - Digita la Latitud, Longitud y Día de recolección.
   
5. Realizar recolección de residuos:
   - Digita la cantidad de residuo que se va a recolectar (vidrio, papel, metal).
   - Observa el mensaje que muestra la recolección realizada en la latitud y longitud especificada.
   - Agrega todo el residuo recolectado (vidrio, papel, metal) que el camión tomó en el día específico.

6. Finalizar turno:
   - Cuando hayas terminado de utilizar el sistema, selecciona la opción para no seguir el programa.
   - El sistema mostrará un mensaje indicando que es hora de descansar.
   - Mostrará los residuos (vidrio, papel, metal) totales recolectados, observa el mensaje

7. Cierre
   - Despedida de la plataforma
   - Inicio de las pruebas unitarias de funcionamiento

## Visualización de Datos
- El ID de los empleados será registrado y se podrá observar de manera clara.
- No olvides visualizar cada uno de los componentes que la consola despliega.

## Planteamiento del UML para la lógica
![image](https://github.com/alejofontalvo/Parcial-2/assets/102882477/118a5ce8-126f-43fb-9fa0-a41a018820f5)

## Recuento Total de Residuos

- Para obtener el recuento total de residuos recogidos en un día específico, se deben haber finalizado los turnos de recolección.
- Selecciona la opción de no agregar más residuos para hallar el recuento total de residuos de vidrio, papel o metal.
- El sistema mostrará el recuento total de residuos recogidos en ese día.

## Soporte

Si encuentras algún problema o tienes alguna pregunta sobre el sistema, no dudes en contactarnos a través de [email protected]

¡Gracias por utilizar el Sistema de Gestión de Residuos! Esperamos que esta herramienta te ayude a optimizar la recolección y gestión de residuos en tu área.
