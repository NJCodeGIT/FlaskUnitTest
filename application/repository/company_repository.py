import application.dbModel.company as model_context
from application.dbModel.company import Company


class CompanyRepository:
    def __init__(self):
        pass

    @staticmethod
    def getAll():
        _modelList = model_context.getAll()
        return model_context.companies_schema.dump(_modelList)

    @staticmethod
    def getById(model_id):
        _model: Company = model_context.getById(model_id)
        return model_context.company_schema.dump(_model)

    @staticmethod
    def addNew(json_data):
        _model: Company = model_context.company_schema.load(json_data)
        model_context.addNew(_model)

    @staticmethod
    def update(json_data):
        _model: Company = model_context.company_schema.load(json_data)
        model_context.update(_model)

    @staticmethod
    def delete(json_data):
        _model: Company = model_context.company_schema.load(json_data)
        model_context.delete(_model)
