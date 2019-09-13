from django.core.mail import send_mail

from trench.backends import AbstractMessageDispatcher
from trench.settings import api_settings


class BasicEmailBackend(AbstractMessageDispatcher):
    def dispatch_message(self, *args, **kwargs):
        """Sends an email with verification code"""

        code = self.create_code()

        send_mail(
            'Your verification code',
            f'Your verification code is {code}',
            api_settings.FROM_EMAIL,
            [self.to],
            fail_silently=False,
        )

        return {'message', 'Email message with MFA code has been sent'}
