import logging

# Configuración del logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Crear el objeto logger
log = logging.getLogger(__name__)
