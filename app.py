from flask_script import Manager

from main import create_app

app_ = create_app('DevConf')
manager = Manager(app_)

if __name__ == '__main__':
    manager.run()
