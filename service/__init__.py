"""
Service Package
"""
from flask import Flask
from service import routes
from service.common import log_handlers

app = Flask(__name__)
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
