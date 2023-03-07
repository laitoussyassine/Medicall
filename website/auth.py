from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Conta,Urgence_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        idNumber = request.form.get('idNumber')

        user = User.query.filter_by(email=email).first()
        user = User.query.filter_by(idNumber=idNumber).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')                

        
    return render_template("login.html", boolean=True)
    


@auth.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        yourname = request.form.get('yourname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        # title = "Thank You!"

        usercontact  =Conta(yourname=yourname, phone=phone, email=email, message=message)
        db.create_all()
        db.session.add(usercontact)
        db.session.commit()
        db.session.rollback()
        # flash('Message envoyer Thank You!', category='success')
        return redirect(url_for('views.thankcontact'))

    return render_template("contact.html")
    # return render_template("contact.html", pagetitle="contact" ,custom_css="Contact")

@auth.route('/thankcontact')
def thankcontact():
    return render_template("thankcontact.html")



@auth.route('/form')
def form():
    return render_template("form.html")

@auth.route('/coming')
def coming():
    return render_template("coming.html")


@auth.route('/start', methods=['GET','POST'])
def start():
    if request.method == 'POST':
        fullName = request.form.get('fullName')
        email = request.form.get('email')
        password = request.form.get('password')
        phoneNumber = request.form.get('phoneNumber')
        idNumber = request.form.get('idNumber')

        user = User.query.filter_by(email=email).first()
        user = User.query.filter_by(idNumber=idNumber).first()
        if user:
            flash('Email or idNumber already exists.', category='error')
        elif len(fullName) < 4:
            flash('full name must be greater than 3 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len (password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif len(phoneNumber) != 10:
            flash('phone number must be 10 characters.', category='error')
        elif len(idNumber) < 2:
            flash('id number must be greater than 1 character.', category='error')
        else:
            new_user =User(fullName=fullName, email=email, password=generate_password_hash(password, method='sha256'), phoneNumber=phoneNumber, idNumber=idNumber)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
           

    return render_template("start.html")


@auth.route('/urgence', methods=['GET','POST'])
def urgence():
    if request.method == 'POST':
        name = request.form.get('name')
        phoneNumber = request.form.get('phoneNumber')
        adress = request.form.get('adress')


        userurgence  =Urgence_user(name=name, phoneNumber=phoneNumber, adress=adress)
        db.create_all()
        db.session.add(userurgence)
        db.session.commit()
        db.session.rollback()
        return redirect(url_for('views.coming'))

    return render_template("urgence.html")
        


@auth.route('/forget')
def forget():
    return render_template("forget.html")



@auth.route('/dashborad')
def dashborad():
    return render_template("dashborad.html")

@auth.route('/personal')
def personal():
    return render_template("personal.html")

@auth.route('/password')
def password():
    return render_template("password.html")

db.create_all()