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


class UserClass:
    def __init__(self, class_id=uuid.uuid4(), class_name=None, meta_info=None):
        self.class_id = class_id
        self.class_name = class_name
        if meta_info is None:
            self.meta_info = {}
        else:
            self.meta_info = meta_info

    def getId(self):
        return self.class_id

    def getUserClass(self):
        return {'class_name': self.class_name, 'meta_info': self.meta_info}

    def updateUserClass(self, **kwargs):
        for key, val in kwargs.items():
            if 'class_id' in key:
                logger.error('class_id cannot be modified.')
            else:
                setattr(self, key, val)
