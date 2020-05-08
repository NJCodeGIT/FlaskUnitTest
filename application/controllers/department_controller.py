from flask import Blueprint, jsonify, request
from application.repository.department_repository import DepartmentRepository

departmentController = Blueprint('departmentController', __name__)


@departmentController.route('/api/showDepartment')
def showAllDepartment():
    repository: DepartmentRepository = DepartmentRepository()
    return jsonify(repository.getAll())


@departmentController.route('/api/showDepartment/<model_id>')
def showDepartment(model_id):
    repository: DepartmentRepository = DepartmentRepository()
    return repository.getById(model_id)


@departmentController.route('/api/addDepartment', methods=['GET', 'POST'])
def addDepartment():
    repository: DepartmentRepository = DepartmentRepository()
    _data = request.get_json()
    repository.addNew(_data)
    return jsonify({'output': 'Department added'})


@departmentController.route('/api/updateDepartment', methods=['GET', 'POST'])
def updateDepartment():
    repository: DepartmentRepository = DepartmentRepository()
    _data = request.get_json()
    repository.update(_data)
    return jsonify({'output': 'Department updated'})


@departmentController.route('/api/deleteDepartment', methods=['GET', 'POST'])
def deleteDepartment():
    repository: DepartmentRepository = DepartmentRepository()
    _data = request.get_json()
    repository.delete(_data)
    return jsonify({'output': 'Department deleted'})
