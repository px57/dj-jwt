
import mailchimp_transactional as MailchimpTransactional

from kernel.interfaces.service import ServiceManager

from datetime import datetime, timedelta

import jwt

class Service(ServiceManager):

    def __init__(self):
        super().__init__()
        print('ChildClass')

    def authenticate(self, *args, **kwargs):
        """
        Send mail method.
        """
        user = kwargs.get('user')

        print ('Authenticate')
        print (kwargs)
        config = self.get_config()
        access_payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=config['JWT_ACCESS_TOKEN_EXPIRES']),
            'iat': datetime.utcnow(),
        }
        access_token = jwt.encode(access_payload, config['JWT_SECRET'], algorithm=config['JWT_ALGORITHM'])

        self.res.jwt_token = access_token