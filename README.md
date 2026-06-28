# Sistema de Gestión de Usuarios — Universidad de Cuenca

Proyecto académico que integra dos asignaturas: **Bases de Datos** (diseño e implementación
del modelo relacional completo de la institución) y **Programación** (desarrollo de un
sistema CRUD en Python con interfaz gráfica para la gestión de la tabla `usuarios`).

## Descripción general

La Universidad de Cuenca requiere un sistema para gestionar el acceso de su comunidad
académica (estudiantes, docentes y administrativos) a su plataforma tecnológica. La base de
datos almacena la ficha completa de cada persona, sus roles, los servicios tecnológicos que
ofrece la universidad, y el registro de accesos y reservas a dichos servicios.

La aplicación desarrollada en Python consume esa base de datos y permite **crear, leer,
actualizar y eliminar usuarios**, con la particularidad de que un usuario no se registra con
datos nuevos: se *activa* a partir de una persona que ya existe en la tabla `personas`,
heredando su cédula y determinando su rol automáticamente según en qué tabla de
especialización (estudiantes, docentes o administrativos) se encuentre.

## Tecnologías utilizadas

| Categoría | Herramienta |
|---|---|
| Lenguaje | Python 3.11 |
| Interfaz gráfica | PyQt5 5.15.11 (diseñada en Qt Designer) |
| Base de datos | MySQL 9.7.0 |
| Conector | mysql-connector-python 9.3.0 |
| Modelado de datos | ERD Plus |
| Empaquetado | PyInstaller |
| IDE | Visual Studio Code |

## Estructura del proyecto

Software_CRUD_v2/
│
├── controllers/
│   └── usuario_controller.py      # Lógica que conecta UI ↔ DAO
│
├── dao/
│   └── usuario_dao.py             # Operaciones CRUD contra la BD
│
├── database/
│   ├── conexion.py                # Conexión a la BD
│   └── universidad.sql            # Script SQL
│
├── models/
│   └── usuario.py                 # Clase/modelo de datos Usuario
│
├── resources/
│   ├── icons/                     # Íconos .png / .svg
│   └── style.qss                  # Hoja de estilos Qt
│
├── ui/
│   ├── usuarios_ui.py             # Generado desde el .ui (pyuic5/pyside6)
│   └── usuarios.ui                # Diseño Qt Designer (solo visual)
│
├── validators/
│   └── usuario_validator.py       # Todas las validaciones
│
├── main.py                        # Punto de entrada de la aplicación
├── README.md                      # Información general del proyecto
└── requirements.txt               # Dependencias del proyecto

## Modelo de base de datos

La base de datos `universidad_cuenca` está normalizada al menos hasta 3FN e incluye:

- **Geografía**: `pais`, `provincia`, `canton`, `parroquia`
- **Personas**: `personas` (ficha base) con especializaciones en `estudiantes`, `docentes`,
  `administrativos`
- **Académico**: `carreras`, `area`
- **Acceso al sistema**: `roles`, `usuarios`
- **Servicios tecnológicos**: `tipo_servicio`, `servicios_tecnologicos`, `accesos`, `reservas`

La tabla `usuarios` se relaciona con `personas` (por `cedula`, `UNIQUE`) y con `roles` (por
`codigo_rol`), y tiene una restricción `CHECK` que limita `roles.nombre_rol` únicamente a
`'estudiante'`, `'docente'` o `'administrativo'`.

## Funcionalidad del CRUD

La aplicación cuenta con 5 pestañas:

1. **Buscar Personas** — lista todas las personas registradas (cédula, nombres, apellidos,
   correo) indicando si ya tienen un usuario creado o no. Existe porque no se puede crear un
   usuario sin conocer de antemano la cédula de la persona.
2. **Buscar Usuario** — consulta un usuario puntual o lista todos los registrados.
3. **Agregar Usuarios** — se ingresa una cédula; el sistema busca a la persona en `personas`,
   determina su rol automáticamente, y genera el nombre de usuario y la fecha de creación.
   Solo se solicitan la contraseña y el estado.
4. **Actualizar Usuarios** — se busca por nombre de usuario; únicamente se permite modificar
   la contraseña y el estado (los demás datos pertenecen a otras tablas y no se editan desde
   aquí).
5. **Borrar Usuario** — elimina un registro, con confirmación previa.

### Generación automática de nombre de usuario

El nombre de usuario se construye como `primernombre.primerapellido`, normalizado a minúsculas
y sin tildes/`ñ` (ej. *Bajaña* → `bajana`). Si el nombre ya existe, se agrega un número
incremental al final (`samuel.vallejo`, `samuel.vallejo1`, `samuel.vallejo2`...), para soportar
personas con nombre y apellido idénticos.

## Validaciones implementadas

- Contraseña segura: mínimo 8 caracteres, una mayúscula, una minúscula y un número.
- Nombre de usuario único, verificado contra la base de datos.
- Cédula con formato válido (10 dígitos numéricos).
- Estado restringido a `activo` / `inactivo`.
- Verificación de que la persona exista y no tenga ya un usuario antes de crear uno nuevo.
- Validación en tiempo real en los campos de entrada.
- Manejo de errores de conexión y de integridad referencial, sin que la aplicación se cierre
  de forma abrupta.

## Manejo de errores destacado

Durante el desarrollo se identificó un conflicto a nivel de librerías nativas entre PyQt5 y
`mysql-connector-python` en Windows, que provocaba el cierre abrupto de la aplicación sin
mostrar ningún error en consola. Se resolvió forzando al conector de MySQL a usar su
implementación pura en Python (`use_pure=True` en la conexión), evitando así el conflicto de
extensiones en C de ambas librerías.

## Instalación y ejecución

1. Instalar las dependencias:
pip install -r requirements.txt
2. Crear la base de datos ejecutando `database/universidad.sql` en MySQL.
3. Configurar las credenciales de conexión en `database/conexion.py`.
4. Ejecutar la aplicación:
python main.py

## Qt Designer (pyqt5-tools)

`pyqt5-tools` incluye el ejecutable de Qt Designer, necesario para abrir y editar el archivo
`ui/usuarios.ui` visualmente.

1. Instalarlo (ya viene incluido en `requirements.txt`, pero también se puede instalar solo):
pip install pyqt5-tools
2. Abrir Qt Designer desde la terminal:
pyqt5-tools designer
Si ese comando no es reconocido, el ejecutable también se puede ubicar manualmente en:
<carpeta_del_entorno>\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
3. Tras editar el `.ui`, regenerar el archivo Python correspondiente:
pyuic5 ui/usuarios.ui -o ui/usuarios_ui.py

## Generar el ejecutable

pip install pyinstaller pyinstaller --clean --onefile --windowed main.py
El ejecutable resultante queda en la carpeta `dist/`.

## Autores

- Michael José Bajaña Espinoza
- Cristian Teodoro Marín Guachichullca
- Alexander Francisco Guamán Congo
- Samuel Felipe Vallejo Morales

Universidad de Cuenca — Proyecto Final de Bases de Datos y Programación.
