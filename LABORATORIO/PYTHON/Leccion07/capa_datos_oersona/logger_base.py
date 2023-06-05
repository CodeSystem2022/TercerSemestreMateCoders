import logging as log
#seria igual a poner log = logging

#llamamos una configuracion basica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('mensaje a nivel debug')
    log.info('a nivel info')
    log.warning('a nivel warning')
    log.error('nivel error')
    log.critical('a nivel critical')
