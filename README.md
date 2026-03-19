Sistema de Gestión de Pedidos en Python
📌 Descripción

Este proyecto consiste en el desarrollo de un sistema en Python que permite registrar clientes, productos y pedidos, con el fin de llevar un control estructurado de las ventas realizadas durante una jornada.

El sistema automatiza el cálculo de los totales por pedido y genera un reporte consolidado al finalizar la ejecución.

🎯 Objetivo

Optimizar el proceso de registro de pedidos, evitando errores manuales y permitiendo obtener información clara sobre:

Clientes registrados

Productos vendidos

Ingresos generados

Reportes finales

🧱 Tecnologías utilizadas

Python

Diccionarios

Tuplas

⚙️ Estructura del sistema
1. Registro de Clientes

Permite almacenar clientes en un diccionario con:

ID

Nombre

Correo

2. Registro de Productos

Los productos se almacenan como tuplas:
(product_id, nombre, precio)

3. Creación de Pedidos

Relaciona:

Cliente

Producto

Cantidad

Calcula automáticamente:
total = precio * cantidad

4. Consulta de Pedidos

Muestra:

Cliente

Producto

Cantidad

Total

5. Cálculo de Ingresos

Suma todos los pedidos realizados.

6. Reporte Final

Incluye:

Total de pedidos

Total de ingresos

Pedidos por cliente

Productos vendidos

🚫 Restricciones cumplidas

No se utilizaron listas

Solo se usaron diccionarios y tuplas

Todas las funciones reciben parámetros

Todas las funciones retornan valores

▶️ Ejecución

Ejecutar el archivo en Python:

python sistema_pedidos.py
👥 Integrantes del equipo

- Natalia Romerin Rincon
- Jefri Calderin Ortiz
- Valery Rhenals Reales

📊 Resultado esperado

El sistema mostrará:

Lista de pedidos

Total de ingresos

Reporte final estructurado

✅ Conclusión

El sistema mejora la organización de pedidos, reduce errores humanos y facilita la toma de decisiones mediante reportes claros.
