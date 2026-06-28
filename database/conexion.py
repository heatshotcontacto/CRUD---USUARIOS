import mysql.connector
def connectionDB():
    print('Entro a la conexión con MySQL')
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'AQUI PONEN SU CONTRASEÑA',
            database = 'universidad_cuenca',
            charset = 'utf8mb4',
            collation = 'utf8mb4_unicode_ci',
            raise_on_warnings = True,
            use_pure = True
        )
        if connection.is_connected():
            print('Conexión exitosa a la BD')
            return connection
    except mysql.connector.Error as error:
        print(f'No se pudo conectar: {error}')
        return None
    


'''
¿Que es charset = 'utf8mb4'?
Charset (conjunto de caracteres) define qué caracteres 
puede almacenar y transmitir la conexión.
Ejm:
A B C
á é í ó ú
ñ
€
😀

¿Que es collation = 'utf8mb4_unicode_ci'?
Collation define las reglas para comparar y ordenar texto.
Ejm:
Ana
ana 
Ána

¿Que es raise_on_warnings = True?
MySQL puede generar:

Errores → algo falla y la operación no se ejecuta.
Advertencias (warnings) → la operación se ejecuta, pero MySQL detectó algo sospechoso.

Si configuras:
raise_on_warnings=True
las advertencias se convierten en excepciones de Python.
'''
