from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load

db = SQLAlchemy()
ma = Marshmallow()


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    inchargeid = db.Column(db.Integer, nullable=False)


class DepartmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Department

    id = ma.auto_field()
    name = ma.auto_field()
    inchargeid = ma.auto_field()

    @post_load
    def make_department(self, data, **kwargs):
        return Department(**data)

    # # Smart hyperlinking
    # _links = ma.Hyperlinks(
    #     {"self": ma.URLFor("company_detail", id="<id>"), "collection": ma.URLFor("company")}
    # )


department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)


def getAll():
    _modelList = Department.query.all()
    return _modelList


def getById(model_id):
    _model: Department = Department.query.filter_by(id=model_id).first()
    return _model


def addNew(model: Department):
    db.session.add(model)
    db.session.commit()


def update(model: Department):
    _model: Department = Department.query.filter_by(id=model.id).first()
    _model.name = model.name
    _model.inchargeid = model.inchargeid
    db.session.commit()


def delete(model: Department):
    _model: Department = Department.query.filter_by(id=model.id).first()
    db.session.delete(_model)
    db.session.commit()
