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
    res = {}
    password = event['password']
    hashed_password = event['hashed_password']
    test_pass = bcrypt.verify(password, hashed_password)
    if test_pass is True:
        logger.debug('Hash matches with password')
        res['result'] = True
    else:
        logger.debug('Hash does not match password.')
        res['result'] = False
    return json.dumps(res)