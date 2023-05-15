import psycopg2 # Esto es para conectarnos  a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            # creamos una sentencia
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # Placeholder
            entrada = input('Digite los id_persona a buscar (separados por coma): ')
            # creamos una tupla de tuplas
            llaves_primarias = (tuple(entrada.split(', ')),)
            # De esta manera ejecutamos la sentencia
            cursor.execute(sentencia, llaves_primarias)
            # Recuperamos todos los registros que seran una lista con tuplas
            registros = cursor.fetchall()
            #creamos un for
            for registro in registros:
                # mostramos
                print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
