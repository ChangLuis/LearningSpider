from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from lottery_nums import lottery_infos

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Lottery_base(db.Model):
    __lotterytable__ = "lottery"

    id = db.Column(db.Integer,primary_key = True)
    period = db.Column(db.Integer)
    period_date = db.Column(db.String(6))
    num1 = db.Column(db.String(2))
    num2 = db.Column(db.String(2))
    num3 = db.Column(db.String(2))
    num4 = db.Column(db.String(2))
    num5 = db.Column(db.String(2))

    def __init__(self,id,period,period_date,num1,num2,num3,num4,num5):
        self.id = id
        self.period = period
        self.period_date = period_date
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

db.create_all()

def create_data(data):
    restore_data = Lottery_base(**data)
    restore_data.save_to_db()

with app.app_context():
    for lottery_info in lottery_infos:
        create_data(lottery_info)