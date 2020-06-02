from flask import Flask
from flask_mail import Message, Mail

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

@app.route("/")
def index():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["simeon_soli@msn.com"]
                  )
    mail.send(msg)

"""def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    mail.send(msg)"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)