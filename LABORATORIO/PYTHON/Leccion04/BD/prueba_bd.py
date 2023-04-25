import psycopg2 # Esto es para conectarnos  a Postgre

# creamos un objeto para la conexion
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

# recuperamos registros ejecutor
cursor = conexion.cursor()
# creamos una sentencia
sentencia = 'SELECT * FROM persona'
# De esta manera ejecutamos la sentencia
cursor.execute(sentencia)
# Recuperamos todos los registros que seran una lista con tuplas
registros = cursor.fetchall()
# mostramos
print(registros)

# cerramos la conexion y el cursor
cursor.close()
conexion.close()




