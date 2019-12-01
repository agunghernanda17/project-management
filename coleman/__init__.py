
#import pymysql

#pymysql.install_as_MySQLdb()

'''
Jika menggunakan webserver yang sudah include database seperti WAMP atau XAMPP,
maka akan membutuhkan mysqlclient.
salah satu alternatif untuk mengatasi dependency ini adalah dengan  menginstall
modul pymysql.
step2nya
1. import pymysql pada __init__.py di direktory yang berada dengan settings.py
2. kemudian ketik pymysql.install_as_MySQLdb()
3. dengan melakukan kedua step diatas maka error yang muncul ttg mysqlclient saat melakukan makemigrate bisa diatasi

jika menemukan masalah error seperti mysqlclient 1.3.13 or newer is required; you have 0.9.3
maka cara mengatasinya adalah

This is how I fixed it.

Go to your django/db/backends/mysql installation dir. Check your path in the error message.

I'm using pipenv so my path is:

/home/username/.local/share/virtualenvs/project-env/lib/python3.7/site-packages/django/db/backends/mysql

Open file base.py and search for:

version = Database.version_info
Put a pass inside if and comment line:

raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.version)

Like this.

if version < (1, 3, 13):
   pass
   '''
#   raise ImproperlyConfigured(
#       'mysqlclient 1.3.13 or newer is required; you have %s.'
#       % Database.__version__
#   )
'''
Save, close this file and open operations.py.

Search for:

query = query.decode(errors='replace')
and change decode to encode

query = query.encode(errors='replace')
Now, try to run the server.

'''

