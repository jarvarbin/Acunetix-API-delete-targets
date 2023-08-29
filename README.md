# Acunetix-API-delete-targets

```
o
 \_/\o
( Oo)                    \|/
(_=-)  .===O-  ~~A~C~U~N~E-T-I-X -K.O-
/   \_/U'                /|\
||  |_/
\\  |
{K ||
 | PP
 | ||
 (__\\
Acunetix killer

```

## 🎯 Monitoreo y Eliminación de Targets 🧹
Este script está diseñado para gestionar targets en un sistema, permitiendo eliminar aquellos que no han sido escaneados o aquellos que son antiguos basados en una fecha límite.

## 🛠️ Requisitos
Bibliotecas Python:
- requests
- json
- datetime
- dateutil
- sys
- URL de la API y clave de autenticación.
## 🚀 Uso
📌 Llena las variables api_url y api_key con la URL de la API y tu clave de autenticación respectivamente.

- api_url = 'FILL ME'
- api_key = 'FILL ME'

##  ⏰ Configura el tiempo límite ajustando el valor en weeks para determinar la antigüedad de los targets a eliminar.

- one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
- Ejecuta el script. Esto consultará los targets y eliminará aquellos que sean antiguos o que no hayan sido escaneados.

## 📝 Notas
💡 Si encuentras targets sin fecha de escaneo, puedes pasar un argumento al ejecutar el script para forzar su eliminación.

💡 Por defecto, el script está configurado para eliminar targets que tienen más de una semana de antigüedad.

##  ❗ Advertencia
🚫 Manipular o eliminar targets puede tener impactos en tu sistema o aplicación. Asegúrate de entender completamente las acciones que el script realiza antes de ejecutarlo.

## 
## ----------------------------------------------------------------------


## English

## 🎯 Monitoring and Removal of Targets 🧹
This script is designed to manage targets within a system, allowing for the removal of those that have not been scanned or those that are old based on a set date.

## 🛠️ Requirements
Python Libraries:

requests
json
datetime
dateutil
sys
API URL and authentication key.

## 🚀 Usage
📌 Fill the variables api_url and api_key with the API URL and your authentication key respectively.

api_url = 'FILL ME'
api_key = 'FILL ME'
⏰ Set the time limit by adjusting the value in weeks to determine the age of the targets to be removed.
one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
Run the script. This will query the targets and remove those that are old or have not been scanned.
## 📝 Notes
💡 If you come across targets with no scan date, you can pass an argument when running the script to force their removal.

💡 By default, the script is set to remove targets that are over a week old.

## ❗ Warning
🚫 Manipulating or removing targets can have impacts on your system or application. Ensure you fully understand the actions the script takes before running it.
