from flask import Flask
from threading import Thread
from loguru import logger
import logging
import os

# This File only exists because of Z00NI's hosting

app = Flask('')

from flask.logging import default_handler

logging.getLogger('werkzeug').disabled = True
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

@app.route('/')
def main():
    return "running"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    logger.level("KEEP_ALIVE", no=10, color="<white>")
    logger.level("KEEP_ALIVE_ERROR", no=30, color="<red>")
    try:
        server = Thread(target=run)
        server.start()
    except Exception as e:
        logger.log("KEEP_ALIVE_ERROR", "Service konnte nicht gestartet werden.")
        logger.log("KEEP_ALIVE_ERROR", e)
        return False
    else:
        logger.log("KEEP_ALIVE", "Service gestartet.")
        return True
