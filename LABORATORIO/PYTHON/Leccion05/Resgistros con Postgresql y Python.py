# Leccion 05 Registros con Postgresql y capa_datos_persona

# 5.1 Uso de with y psycopg2
#import psycopg2
#conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
#try:
#    with conexion:
#        with conexion.cursor() as cursor:
#            sentencia = 'SELECT * FROM persona'
#            cursor.execute(sentencia)
#            registros = cursor.fetchall()
#            print(registros)
#except Exception as e:
#    print(f'Ocurrió un error: {e}')
#finally:
#    conexion.close()

# http://www.pyscog.org/doc/usage.html


# 5.2 Función fetchone en psycopg2 "recuperar un registro con fetchone"
#import psycopg2
#conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd'
#try:
#    with conexion:
#        with conexion.cursor() as cursor:
#            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#            _  # Placeholder
#            id_persona = input('Digite un numero para el id_persona:')
#            cursor.execute(sentencia, (id_persona,))  # De esta manera ejecutamos la sentencia
#            registros = cursor.fetchone()
             # Recuperamos todos los registros que serán una lista
#            print(registros)
#except Exception as e:
#    print(f'Ocurrio un error: {e}')
#finally:
#conexion.close()
# 5.3 Función fechall en psycopg2 Parte 1 y 2
#import psycopg2
#
#conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

#try:
#    with conexion:
#        with conexion.cursor() as cursor:
#            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)'
#            _  # Placeholder
#            # id_persona =input ('Digite un numero para el id_persona:')
#            cursor.execute(sentencia, (id_persona,))  # De esta manera ejecutamos la sentencia
#            registros = cursor.fetchall()
#            _  # Recuperamos todos los registros que serán una lista
#            for registro in registros:
#
#            print(registro)
#except Exception as e:
#    print(f'Ocurrió un error: {e}')
#finally:

#conexion.close()

# Parte 2
#import psycopg2

#conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

#try:
#    with conexion:
#        with conexion.cursor() as cursor:
#            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#            _  # Placeholder
#            entrada = input('Digite los id_persona a buscar( separados por coma):')
#            llaves_primarias = (tuple(entrada.split(',')),)
#            cursor.execute(sentencia, llaves_primarias)  # De esta manera ejecutamos la sentencia
#            registros = cursor.fetchall()
#            _  # Recuperamos todos los registros que serán una lista
#            for registro in registros:
#
#             print(registro)
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.4 Insertar un registro con psycopg2
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd'
#                             )
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'INSERT INTO persona (nombre,apellido,email)VALUE (%s,%s,%s,)'
#             valores = ('Carlos', 'Lara', 'clara@mail.com')
#             _  # Es una tupla
#             # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#             cursor.execute(sentencia, valores)  # De esta manera ejecutamos la sentencia
#             registros_insertados = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#             prin(f'Los registros insertados son:{registros_insertados}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.5 Insertar varios registros
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
#
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'INSERT INTO persona (nombre,apellido,email)VALUE (%s,%s,%s,)'
#             valores = (
#                 ('Carlos', 'Lara', 'clara@mail.com')
#                 ('Marcos', 'Canto', 'mcant@mail.com')
#                 ('Marcerlo', 'Cuenca', 'cuencaM@mail.com')
# # Es una tupla de tuplas
#  # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#                 cursor.executemany(sentencia, valores)
#             # De esta manera ejecutamos la sentencia
#             registros_insertados = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#             prin(f'Los registros insertados son:{registros_insertados}')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#
# conexion.close()
# # 5.6 Actualizar o modificar un registro
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
#
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s ,email=%s WHERE id_persona=%s'
#             valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1)
#             _  # Es una tupla
#             # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#             cursor.executemany(sentencia, valores)  # De esta manera ejecutamos la sentencia
#             registros_actualizado = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#             prin(f'Los registros actualizados son:{registros_actualizado}')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.7 Actualizar o modificar varios registros
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
#
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s ,email=%s WHERE id_persona=%s'
#             valores = ()
#
#         ('Juan ', 'Perez', 'jperez@mail.com', 4)
#         ('Romina', 'Ayala', 'ayalar@mail.com', 5))_
#         # Es una tupla de tuplas
#
#         # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#         cursor.executemany(sentencia, valores)
#         # De esta manera ejecutamos la sentencia
#         registros_actualizado = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#         prin(f'Los registros actualizados son:{registros_actualizado}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.8 Eliminar un registro
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd'
#                             )
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s ,email=%s WHERE id_persona=%s'
#             valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1)
#             _  # Es una tupla
#             # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#             cursor.executemany(sentencia, valores)  # De esta manera ejecutamos la sentencia
#             registros_actualizado = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#             prin(f'Los registros actualizados son:{registros_actualizado}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.7 Actualizar o modificar varios registros
#
# import psycopg2
#
# conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd'
#                             )
#
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'DELETE FROM persona WHERE id_persona=%s'
#             entrada = input('Digite el numero de registro a elimnar:')
#
#             valores = (entrada,)
#             Es
#             una
#             tupla
#             de
#             valores
#         ('Juan ', 'Perez', 'jperez@mail.com', 4)
#         ('Romina', 'Ayala', 'ayalar@mail.com', 5))_
#         # Es una tupla de tuplas
#
#         # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
#         cursor.executemany(sentencia, valores)
#         # De esta manera ejecutamos la sentencia
#         registros_eliminados = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
#         prin(f'Los registros actualizados son:{registros_eliminados}')
# except Exception as e:
#     print(f'Ocurrio un error: {e}')
# finally:
#
# conexion.close()
#
# # 5.9 Eliminar varios registros
import psycopg2
conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Digite el numerosde registro a elimnar(separados por coma)')

            valores = (tuple, (entrada.split(','),))  # Es una tupla de tuplas
            # Es una tupla de tuplas

            # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
            cursor.executemany(sentencia, valores)  # De esta manera ejecutamos la sentencia
            registros_eliminados = cursor.rowcount_  # Recuperamos todos los registros que seran una lista
            prin(f'Los registros actualizados son:{registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
