import logging
import sys

logger = logging.getLogger("api-tests")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.handlers = [handler]

__all__ = ["logger"]