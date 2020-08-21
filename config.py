import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '24680-never-guess-13579'
