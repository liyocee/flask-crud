from flask import render_template, flash, url_for, redirect

from app import db
from app.admin import admin
from app.admin.forms import DepartmentForm
from app.models import Department, Employee


@admin.route('/')
def index():
    return render_template('admin/index.html', title='Admin')


@admin.route('/employees', methods=['GET'])
def employees():
    return render_template('admin/employees.html', title='Employees', employees=Employee.query.all())


@admin.route('/departments', methods=['GET'])
def departments():
    return render_template('admin/departments.html', title='Departments', departments=Department.query.all())


@admin.route('/departments/create', methods=['GET', 'POST'])
def create_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            name=form.name.data,
            description=form.description.data
        )

        db.session.add(department)
        db.session.commit()

        flash('Department created succesfully')

        return redirect(url_for('admin.departments'))

    return render_template('admin/create_department.html', title='Create Departments', form=form)
