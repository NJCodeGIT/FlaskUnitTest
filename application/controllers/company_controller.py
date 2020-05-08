from flask import Blueprint, jsonify, request
from application.repository.company_repository import CompanyRepository

companyController = Blueprint('companyController', __name__)


@companyController.route('/')
def index():
    return "Dev changes"


@companyController.route('/failure')
def failureCase():
    return 10 / 'A'


@companyController.route('/api/showCompany')
def showAllCompany():
    repository: CompanyRepository = CompanyRepository()
    return jsonify(repository.getAll())


@companyController.route('/api/showCompany/<model_id>')
def showCompany(model_id):
    repository: CompanyRepository = CompanyRepository()
    return repository.getById(model_id)


@companyController.route('/api/addCompany', methods=['GET', 'POST'])
def addCompany():
    repository: CompanyRepository = CompanyRepository()
    _data = request.get_json()
    repository.addNew(_data)
    return jsonify({'output': 'Company added'})


@companyController.route('/api/updateCompany', methods=['GET', 'POST'])
def updateCompany():
    repository: CompanyRepository = CompanyRepository()
    _data = request.get_json()
    repository.update(_data)
    return jsonify({'output': 'Company updated'})


@companyController.route('/api/deleteCompany', methods=['GET', 'POST'])
def deleteCompany():
    repository: CompanyRepository = CompanyRepository()
    _data = request.get_json()
    repository.delete(_data)
    return jsonify({'output': 'Company deleted'})
