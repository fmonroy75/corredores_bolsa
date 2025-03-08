# Proyecto: Aplicación Corredores de Bolsa


## Proyecto
Crearán una plataforma que simula el funcionamiento de una bolsa de valores. Los
usuarios podrán crear cuentas, comprar y vender acciones, ver gráficos históricos de
precios, y recibir noticias financieras relevantes.
No te preocupes, esta será la primera etapa del proyecto, además no estarás sol@, se ha
designado un equipo que te hará entrega de la información necesaria para proceder con
el desarrollo del proyecto: información detallada del proyecto, diagrama de flujo, modelo
físico y wireframes al final del documento.
Requerimientos funcionales del sistema:
### Frontend Responsive:
○ Crear una interfaz adaptable a dispositivos móviles, tabletas y escritorios.
○ Vistas de control donde los usuarios puedan ver sus portafolios y realizar
transacciones.
### Modelo de Datos:
○ Usuarios: Cada usuario tiene id, nombre, email, contraseña, y un saldo inicial para
realizar operaciones, este debe asignarse de forma automática al momento del
registro, se sugiere que sea con un valor de 100 USD. Existirán dos tipos de usuario
“REGULAR” y “ADMIN” el cual es el encargado de actualizar los precios.
○ Acciones: Incluye id, símbolo, nombre de la empresa, precio actual, y cambios en
el precio.
○ Transacciones: Registro compras, ventas de acciones, cantidad, precio, fecha de la
transacción, y id del usuario.
### Funcionalidades:
○ Compra de acciones: Permitir a los usuarios comprar acciones utilizando su saldo
disponible.
○ Venta de acciones: Permitir a los usuarios vender acciones de su portafolio.
○ Actualización de Precios: Simular cambios en los precios de las acciones en
intervalos regulares.
○ Visualización del Portafolio: Mostrar el portafolio de inversiones del usuario,
incluyendo las acciones que posee y su valor actual.
○ Historial de Transacciones: Ver un registro detallado de todas las transacciones
realizadas.
### Datos semilla::
○ Incluir datos de ejemplo en un archivo `.sql`, `.csv`, o `.json` para pruebas
iniciales.


## Características del Proyecto

### 1. Instalación y Configuración del Ambiente de Desarrollo

- **PostgreSQL**: Configuración como sistema de base de datos.
- **Ambiente virtual de Python**: Aislamiento del entorno de desarrollo.
- **Paquetes necesarios**: Instalación de dependencias para trabajar con Django.
- **Aplicación Django**: Implementación de la lógica del sitio web.

### 2. Modelo de Datos

- **Modelo relacional**: Diseño de tablas relacionadas para inmuebles y sus atributos.
- **Conexión a PostgreSQL**: Configuración de la base de datos en `settings.py`.
- **Llaves primarias y foráneas**: Implementación para garantizar integridad referencial.

### 3. Operaciones CRUD en Django

- **Crear**: Añadir nuevos registros.
- **Leer**: Listar registros almacenados.
- **Actualizar**: Modificar información existente.
- **Eliminar**: Borrar registros específicos.



## 🚀 Configuración Inicial

```bash
# Instalar dependencias
pip install django

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```


## Tecnologías Utilizadas

- **Backend**: Implementación de operaciones CRUD mediante el patrón MVC.
- **Frontend**: Desarrollo de vistas personalizadas utilizando HTML, CSS y/o frameworks de diseño.
- **Base de Datos**: Uso de un modelo previamente diseñado y poblado con datos relevantes.
- **Framework**: Django.


## Instrucciones de Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/fmonroy75/corredores_bolsa.git
   ```

2. Instalar dependencias:

```bash
  pip install -r requirements.txt
```

3. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

## 👥Autor:

- [Francisco Monroy](https://github.com/fmonroy75)
