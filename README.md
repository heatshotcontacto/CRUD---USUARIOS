# Software_CRUD_v2

Sistema CRUD de gestión de usuarios desarrollado en Python (PyQt5) con MySQL como motor de
base de datos, hecho como proyecto académico para la Universidad de Cuenca.

La aplicación permite crear, leer, actualizar y eliminar usuarios a partir de personas ya
registradas en la base de datos: el rol (estudiante, docente o administrativo) y el nombre de
usuario se determinan y generan automáticamente, sin intervención manual.

## Características

- Arquitectura en capas (DAO / Modelo / Validadores / Controlador / UI).
- Generación automática de `nombre_usuario` en formato `primernombre.primerapellido`, con
  normalización de tildes/`ñ` y manejo de colisiones (nombres repetidos).
- Determinación automática del rol según la tabla de especialización a la que pertenece la
  persona (`estudiantes`, `docentes`, `administrativos`).
- Validaciones de contraseña segura, unicidad de usuario, formato de cédula y estado.
- Interfaz gráfica construida en Qt Designer, con 5 pestañas: Buscar Personas, Buscar Usuario,
  Agregar Usuarios, Actualizar Usuarios y Borrar Usuario.

## Tecnologías

- Python 3.11
- PyQt5 5.15.11
- mysql-connector-python 9.3.0
- MySQL 9.7.0

## Estructura del proyecto

```
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
```

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/heatshotcontacto/Software_CRUD_v2.git
   cd Software_CRUD_v2
   ```

2. (Opcional pero recomendado) Crear un entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Crear la base de datos ejecutando el script `database/universidad.sql` en tu motor MySQL.
   **Nota:** este script solo contiene la estructura de las tablas (sin datos de ejemplo); los
   registros de prueba debes cargarlos tú mismo, ya sea manualmente o usando la propia
   aplicación.

5. Configurar tus propias credenciales de conexión en `database/conexion.py` (host, usuario,
   contraseña y nombre de la base de datos). **Importante:** no subas tus credenciales reales
   al repositorio si haces un fork o un commit propio.

6. Ejecutar la aplicación:
   ```
   python main.py
   ```

## Qt Designer (pyqt5-tools)

`pyqt5-tools` permite abrir y editar visualmente el archivo `ui/usuarios.ui`.

```
pip install pyqt5-tools
pyqt5-tools designer
```

Si el comando no es reconocido, el ejecutable de Designer también puede ubicarse en:
```
<entorno_virtual>\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
```

Después de editar el `.ui`, regenera el archivo Python:
```
pyuic5 ui/usuarios.ui -o ui/usuarios_ui.py
```

## Generar ejecutable (PyInstaller)

```
pip install pyinstaller
pyinstaller --clean --onefile --windowed main.py
```

El ejecutable se genera en la carpeta `dist/`.

## Notas técnicas

Se detectó un conflicto de librerías nativas entre PyQt5 y `mysql-connector-python` en Windows
que provocaba el cierre abrupto de la aplicación sin mensaje de error. Se solucionó forzando
al conector a usar su implementación pura en Python, agregando `use_pure=True` en los
parámetros de conexión dentro de `database/conexion.py`.

## Autores

- Michael José Bajaña Espinoza
- Cristian Teodoro Marín Guachichullca
- Alexander Francisco Guamán Congo
- Samuel Felipe Vallejo Morales
