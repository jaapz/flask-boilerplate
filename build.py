import subprocess
import sys
import os

from pynt import task

_curpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(_curpath)

from app import db


@task()
def clean_db():
    """ Remove test database. """
    db_path = '/tmp/myhealth.db'
    if os.path.exists(db_path):
        print 'Removing database...'
        os.remove(db_path)


@task(clean_db)
def setup_db():
    """ Initiate the database. """
    db.create_all()


@task(clean_db)
def tests():
    """ Run ALL the tests! """
    subprocess.call(['py.test', 'tests/', '-v'])


@task()
def server():
    """ Run the development server, don't use this in production! """
    subprocess.call(['./server.py'])
