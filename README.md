# Acunetix-API-delete-targets

![DALL·E 2023-08-25 10 45 14](https://github.com/jarvarbin/Acunetix-API-delete-targets/assets/93614373/a5fd0f0c-b838-4b0a-aeec-81eb01432f5a)


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



