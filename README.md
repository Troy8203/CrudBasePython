# Proyecto CRUD con Conexión a Oracle

Este proyecto implementa un sistema básico de gestión de empleados (CRUD) conectado a una base de datos Oracle. Incluye operaciones de creación, lectura, actualización y eliminación de empleados en una tabla de ejemplo.

## Estructura del Proyecto

```
project/
├── .env                         # Archivo de configuración de entorno
├── config.py                    # Configuración del proyecto (lectura de variables .env)
├── main.py                      # Punto de entrada del proyecto
├── requirements.txt             # Dependencias del proyecto
│
├── db/                          
│   └── manager.py               # Clase `DatabaseManager` para gestionar la conexión
│
├── models/
│   └── employee.py              # Definición de operaciones CRUD para empleados
│
└── utils/                        # Funciones de ayuda (opcional)
```

## Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Configurar el Entorno Virtual y dependencias

Para gestionar las dependencias, es recomendable usar un entorno virtual por ello ejecutar la siguiente linea para instalar.

```bash
./install.bat
```

### 3. Configurar el Archivo `.env`

Crea un archivo `.env` o copiar el archivo `.env.example` en la raíz del proyecto con las credenciales de tu base de datos Oracle:

```
DB_USER=db272
DB_PASSWORD=tu_contraseña_secreta
DB_DSN=localhost:1521/XEPDB1
```

### 4. Ejecutar el Proyecto

Puedes ejecutar el proyecto desde `main.py` para probar las funcionalidades CRUD:

```bash
python main.py
```

Pero se recomienda ejecutar con el script `run.bat`:

```bash
./run.bat
```

## Uso

El archivo `main.py` contiene ejemplos básicos para:

1. Crear la tabla `employees` en la base de datos.
2. Insertar registros de empleados.
3. Consultar todos los empleados o un empleado específico.
4. Actualizar un registro de empleado.
5. Eliminar un registro de empleado.

> **Nota**: Asegúrate de que la base de datos Oracle esté en funcionamiento y accesible en el host y puerto especificados en el archivo `.env`.

## Dependencias

- `oracledb`: Conector de Python para la base de datos Oracle.
- `python-dotenv`: Carga de variables de entorno desde el archivo `.env`.