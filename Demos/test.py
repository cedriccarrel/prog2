#einnahmen (
#		sparziel FLOAT, sparzeitraum INTEGER, hashtagsparen TEXT,
#		einnahmefirma FLOAT, einnahmebetrag FLOAT, einnahmedatum FLOAT,
#		einnahmedauerauftrag TEXT, einnahmehashtag TEXT, einnahmebeschreibung TEXT
#	)
	
#personalien (
#		name TEXT, vorname TEXT, situation TEXT, email TEXT, passwort TEXT, username TEXT, 
#		telefonnummer INTEGER, passwortvergessen TEXT
#	)

from flask import Flask
from flask_mail import Message, Mail
from app.forms import ResetPasswordRequestForm

app = Flask(__name__)

#E-Mail Konfiguration

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'testotester525@gmail.com',
    MAIL_PASSWORD = 'Test123?',
))

mail = Mail(app)




"""
@app.route("/")
def index():

    
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form) 

