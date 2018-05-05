from flask import render_template, flash, url_for, redirect

from app import db
from app.home import home
from app.home.forms import EmployeeRegistrationForm
from app.models import Employee


@home.route('/', methods=['GET'])
def index():
    return render_template('home/index.html', title='Welcome')


@home.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle registration of employees
    """
    form = EmployeeRegistrationForm()
    if form.validate_on_submit():
        employee = Employee(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )
        # Save employee to the database
        db.session.add(employee)
        db.session.commit()

        flash('You have successfully added an employee, yeay!')

        return redirect(url_for('admin.employees'))

    return render_template('home/register.html', form=form, title='Welcome')
