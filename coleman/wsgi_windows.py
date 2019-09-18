#ganti line ini sesuai path di server
activate_this = 'A:/project/project/django/django_project_management/Scripts/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

#ganti line ini sesuai path di server
# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('A:/project/project/django/django_project_management/Lib/site-packages')

#ganti line ini sesuai path di server
# Add the app's directory to the PYTHONPATH
sys.path.append('A:/project/project/django/django-coleman-master')
sys.path.append('A:/project/project/django/django-coleman-master/coleman')

os.environ['DJANGO_SETTINGS_MODULE'] = 'coleman.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coleman.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()