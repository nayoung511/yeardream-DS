import logging


logging.basicConfig(
    filename='test.log',
    level=logging.INFO
)
logging.debug("디버깅")
logging.info("정보확인")
logging.warning("정보확인")
logging.error("정보확인")
logging.critical("치명적인 에러")
1
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.debug("디버깅")
logger.info("정보확인")
logger.warning("정보확인")
logger.error("정보확인")
logger.critical("치명적인 에러")

import functions
functions.log_warning()