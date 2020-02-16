from app import create_app, db
from flask_script import Manager, Server
from app.models import User,Pitch,Comment
from flask_migrate import Migrate, MigrateCommand



# Creating app instance
app = create_app('production')
app = create_app('development')
app = create_app('production')

# create manager instance
manager = Manager(app)

# create migrate instance
migrate = Migrate(app,db)

manager.add_command('server', Server)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """
    Run unitests
    Returns:

    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User, Comment=Comment, Pitch=Pitch)

if__name__=='__main__':
    manager.run()