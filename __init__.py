import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from application.controllers.company_controller import companyController
from application.controllers.department_controller import departmentController

def create_app(test_config=False):
    app = Flask(__name__, instance_relative_config=True)

    POSTGRES = {
        'user': 'ldbswjguyrzxdb',
        'pw': '55f3f4cad8fd63c13c5f9e81d671e938dd212d61bd49c12efe67a913e1ac2814',
        'db': 'd81ij84pjg8ali',
        'host': 'ec2-54-210-128-153.compute-1.amazonaws.com',
        'port': '5432',
    }

    DB_URL = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    # logging.basicConfig(filename='demo.log', level=logging.DEBUG)
    logging.basicConfig(filename='demo.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    logging.info('Registering controllers - starting')

    app.register_blueprint(companyController)
    app.register_blueprint(departmentController)

    logging.info('Registering controllers - completed')

    if __name__ == '__main__':
        app.run()

    return app

current_app = create_app()
