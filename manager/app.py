
import logging
from logging.handlers import TimedRotatingFileHandler
from modules.command_line import cli

log_handler = TimedRotatingFileHandler("app.log", when="w0", backupCount=5)
logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(module)s-%(lineno)04d %(levelname)8s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG, handlers=[log_handler])


if __name__ == "__main__":
    cli()