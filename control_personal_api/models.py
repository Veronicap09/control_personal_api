from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    puesto = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Empleado {self.nombre}>'