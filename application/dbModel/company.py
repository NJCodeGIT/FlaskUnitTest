from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load

db = SQLAlchemy()
ma = Marshmallow()


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text)
    salary = db.Column(db.Integer)


class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company

    id = ma.auto_field()
    name = ma.auto_field()
    age = ma.auto_field()
    address = ma.auto_field()
    salary = ma.auto_field()

    @post_load
    def make_company(self, data, **kwargs):
        return Company(**data)


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)


def getAll():
    _modelList = Company.query.all()
    return _modelList


def getById(model_id):
    _model: Company = Company.query.filter_by(id=model_id).first()
    return _model


def addNew(model: Company):
    db.session.add(model)
    db.session.commit()


def update(model: Company):
    _model: Company = Company.query.filter_by(id=model.id).first()
    _model.name = model.name
    _model.age = model.age
    _model.address = model.address
    _model.salary = model.salary
    db.session.commit()


def delete(model: Company):
    _model: Company = Company.query.filter_by(id=model.id).first()
    db.session.delete(_model)
    db.session.commit()
