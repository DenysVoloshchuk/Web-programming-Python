import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '18JTtCHXI3'
WTF_CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')