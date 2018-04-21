import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a stream handler
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class User:
    def __init__(self, user_name=None, password_hash=None, email=None, is_active=True, class_id=None, class_meta=None,
                 recovery_id=None, recovery_meta=None):
        self.user_name = user_name
        self.password_hash = password_hash
        self.email = email
        self.is_active = is_active

        # These are stubbed out for future usage as user classes are implemented
        self.class_id = class_id
        self.class_meta = class_meta

        # These are stubbed out for future usage as recovery classes are implemented
        self.recovery_id = recovery_id
        self.recovery_meta = recovery_meta

    def getUser(self):
        return {'password_hash': self.password_hash, 'email': self.email, 'is_active': self.is_active,
                'class_id': self.class_id, 'class_meta': self.class_meta, 'recovery_id': self.recovery_id,
                'recovery_meta': self.recovery_meta}

    def getUserName(self):
        return self.user_name

    def updateUser(self, **kwargs):
        for key, val in kwargs.items():
            if 'user_name' in key:
                logger.error('user_name cannot be modified.')
            else:
                setattr(self, key, val)
