import psycopg2 # Esto es para conectarnos  a Postgre

# creamos un objeto para la conexion conexion
#conexion = psycopg2.connect(
#    user='postgres',
#   password='admin',
#    host='127.0.0.1',
#    port='5432',
#    database='test_bd'
#)

# recuperamos registros ejecutor
#cursor = conexion.cursor()
# creamos una sentencia
#sentencia = 'SELECT * FROM persona'
# De esta manera ejecutamos la sentencia
#cursor.execute(sentencia)
# Recuperamos todos los registros que seran una lista con tuplas
#registros = cursor.fetchall()
# mostramos
#print(registros)
# cerramos la conexion y el cursor
#cursor.close()
#conexion.close()

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # de esta manera ejecutamos la sentencia
            registros = cursor.fetchall()
            print(f'Los registros son: {registros}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# http: