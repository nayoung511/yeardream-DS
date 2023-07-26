import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

logger.debug("디버깅")
logger.info("정보확인")
logger.warning("정보확인")
logger.error("정보확인")
logger.critical("치명적인 에러")


def log_warning():
    logging.warning("functions에서 호출됨")