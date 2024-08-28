from loguru import logger


logger.debug("Um aviso para o desenvolvedor")
logger.info("Informação importante ao processo")
logger.warning("Um aviso que algo vai parar de funcionar")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu um erro que aborta a aplicação")