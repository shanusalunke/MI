from django.conf import settings
settings.configure()

from django.core.mail import EmailMessage
email = EmailMessage('Hello', 'World', to=['salunkeshanu91@gmail.com'])
email.send()


