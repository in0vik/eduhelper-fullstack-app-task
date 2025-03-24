"""
ASGI config for the EduHelper project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduhelper_project.settings')
application = get_asgi_application()
