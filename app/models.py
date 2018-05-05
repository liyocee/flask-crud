from app import db


class Employee(db.Model):
    """
    Create an employee table
    """
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), unique=True, index=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))

    def __repr__(self):
        return '<Employee: {}>'.format(self.first_name)


class Department(db.Model):
    """
    Creates a Department table
    """
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.TEXT)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)
