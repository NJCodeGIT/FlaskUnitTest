import application.dbModel.department as model_context
from application.dbModel.department import Department


class DepartmentRepository:
    def __init__(self):
        pass

    @staticmethod
    def getAll():
        _modelList = model_context.getAll()
        return model_context.departments_schema.dump(_modelList)

    @staticmethod
    def getById(model_id):
        _model: Department = model_context.getById(model_id)
        return model_context.department_schema.dump(_model)

    @staticmethod
    def addNew(json_data):
        _model: Department = model_context.department_schema.load(json_data)
        model_context.addNew(_model)

    @staticmethod
    def update(json_data):
        _model: Department = model_context.department_schema.load(json_data)
        model_context.update(_model)

    @staticmethod
    def delete(json_data):
        _model: Department = model_context.department_schema.load(json_data)
        model_context.delete(_model)
