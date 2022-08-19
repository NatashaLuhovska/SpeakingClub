
from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/speaking_club_dates'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120))
    email=db.Column(db.String(120), unique=True)
    phone=db.Column(db.String(120), unique=True)
    topic=db.Column(db.String(150))
    level_en=db.Column(db.String(30))
    weekday=db.Column(db.String(30))

    def __init__(self, name_, email_, phone_, topic_, level_en_,weekday_):
        self.name=name_
        self.email=email_
        self.phone=phone_
        self.topic=topic_
        self.level_en=level_en_
        self.weekday=weekday_



@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")

@app.route('/about/success/', methods=['POST'])

def success():
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['email_name']
        phone = request.form['phone_number']
        topic = request.form['user_topic']
        level_en = request.form['level_en']
        weekday = request.form['weekday']
        print(name, email, phone,topic, level_en,weekday)
        if db.session.query(Data).filter(Data.email==email).count() == 0 and db.session.query(Data).filter(Data.phone==phone).count() == 0:
            data=Data(name, email, phone, topic, level_en, weekday)
            send_email(name, email, phone, topic, level_en, weekday)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template("regn.html")


if __name__=="__main__":
    app.run(debug=True)