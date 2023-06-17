from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log

class PersonaDAO:
    '''
    DAO significa: Data access object
    CRUD = create(insertar) read(seleccionar) update(actualizar) delete
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'


    # Definimos los metodos de la clase

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                persona = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return persona

    @classmethod
    def insertar(cls,persona):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

       @classmethod
    def actualizar(cls,persona):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona Actulizada: {persona}')
                return cursor.rowcount

         @classmethod
    def eliminar(cls,persona):
         with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Persona Actulizada: {persona}')
                return cursor.rowcount


if __name__ == '__main__':
    persona1 = Persona(nombre='Fede',apellido='Romero',email='prometeo@gmail.com')
    personas_inserteadas  = PersonaDAO.insertar(persona1)
    log.debug(personas_inserteadas)
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)