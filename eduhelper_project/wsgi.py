"""
WSGI config for the EduHelper project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduhelper_project.settings')
application = get_wsgi_application()
