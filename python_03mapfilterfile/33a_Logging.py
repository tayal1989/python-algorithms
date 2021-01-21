import logging

# logging.basicConfig(filename="mylog.log", level = logging.ERROR)    # Only critical and error message are visible if level is ERROR
# logging.basicConfig(filename="mylog.log", level = logging.DEBUG)    # All messages are visible if level is DEBUG
logging.basicConfig(filename="mylog.log", level = logging.CRITICAL)    # Only critical message are visible if level is DEBUG
logging.info("Information")
logging.error("Error")
logging.critical("Critical")
logging.debug("Debug")
logging.warn("Warning")
