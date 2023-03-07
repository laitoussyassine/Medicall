from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")


@views.route('dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('form')
def form():
    return render_template("form.html")

@views.route('today')
def today():
    return render_template("today.html")



@views.route('about')
def about():
    return render_template("about.html")

@views.route('urgence')
def urgence():
    return render_template("urgence.html")

@views.route('notification')
def notification():
    return render_template("notification.html")


@views.route('/thankcontact')
def thankcontact():
    return render_template("thankcontact.html")

@views.route('/coming')
def coming():
    return render_template("coming.html")

@views.route('/personal')
def personal():
    return render_template("personal.html")


@views.route('/password')
def password():
    return render_template("password.html")

@views.route('/payment')
def payment():
    return render_template("payment.html")

@views.route('/term')
def term():
    return render_template("term.html")

@views.route('/privacy')
def privacy():
    return render_template("privacy.html")


# @views.route('forget')
# def forget():
#     return render_template("forget.html")





