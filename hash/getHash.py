import logging
import sys
from passlib.hash import bcrypt
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def lambda_handler(event, context):
    password = event['password']
    logger.info('Hashing password.')
    pw_hash = bcrypt.hash(password)
    res = {'hashed_password': pw_hash}
    return json.dumps(res)

