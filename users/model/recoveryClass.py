import uuid
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


class RecoveryClass:
    def __init__(self, recovery_id=uuid.uuid4(), recovery_name=None, meta_info=None):
        self.recovery_id = recovery_id
        self.recovery_name = recovery_name
        if meta_info is None:
            self.meta_info = {}
        else:
            self.meta_info = meta_info

    def getId(self):
        return self.recovery_id

    def getRecoveryClass(self):
        return {'recovery_name': self.recovery_name, 'meta_info': self.meta_info}

    def updateRecoveryClass(self, **kwargs):
        for key, val in kwargs.items():
            if 'recovery_id' in key:
                logger.error('recovery_id cannot be changed.')
            else:
                setattr(self, key, val)
