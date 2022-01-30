from flask import Flask
from threading import Thread
from loguru import logger
import logging
import os

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
    try:
        logger.info("KEEP_ALIVE Service wird gestartet.")
        server = Thread(target=run)
        server.start()
    except Exception as e:
        logger.error("KEEP_ALIVE Service konnte nicht gestartet werden.")
        logger.error(e)
        return
    else:
        logger.success("KEEP_ALIVE Service gestartet.")
