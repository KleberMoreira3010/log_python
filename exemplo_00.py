from loguru import logger

logger.add("meu_log.log", level="CRITICAL")

def soma(x, y):
    try:
        soma =x + y
        logger.info(f" Você selecionou valores corretos{soma}")
        return soma
    except:
        logger.critical("Você digitol valores inválidos")


soma(2,3)
soma(2,10)
soma(2,"3")    

