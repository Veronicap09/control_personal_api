from flask import Blueprint, request, jsonify
from models import db, Empleado

bp = Blueprint('api', __name__)

@bp.route('/empleados', methods=['POST'])
def agregar_empleado():
    data = request.get_json()
    nuevo_empleado = Empleado(nombre=data['nombre'], puesto=data['puesto'])
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({'mensaje': 'Empleado agregado', 'id': nuevo_empleado.id}), 201

@bp.route('/empleados', methods=['GET'])
def listar_empleados():
    empleados = Empleado.query.all()
    return jsonify([{'id': emp.id, 'nombre': emp.nombre, 'puesto': emp.puesto} for emp in empleados]), 200

@bp.errorhandler(404)
def not_found(error):
    return jsonify({'mensaje': 'Recurso no encontrado'}), 404

@bp.errorhandler(500)
def internal_error(error):
    return jsonify({'mensaje': 'Error interno del servidor'}), 500