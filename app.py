from flask import Flask
from flask import request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
import models
from models import Account, Rating, Deposit, Currency, TransactionHistory, User
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('db_connect')
db.init_app(app)
migrate = Migrate(app, db)


@app.get('/currency/<currency_UPS>')
def currency_list(currency_UPS):
    res = Currency.query.filter_by(name=currency_UPS).all()
    return [it.to_dict() for it in res]

@app.get('/currency/<currency_UPS>/rating')
def currency_rating(currency_UPS):
    res = Rating.query.filter_by(currency_name=currency_UPS).all()
    return [it.to_dict() for it in res]

@app.get('/currency')
def all_currency_rating():
    res = Currency.query.all()
    return [it.to_dict() for it in res]


@app.get('/currency/trade/main:<currency_UPS1>/second:<currency_UPS2>')
def course_ups1_to_ups2(currency_UPS1, currency_UPS2):
    date_now = datetime.datetime.now().strftime("%d-%m-%Y")
    res = Currency.query.filter_by(name=currency_UPS1, date=date_now).first()
    res1 = Currency.query.filter_by(name=currency_UPS2, date=date_now).first()
    return {'exchange': f"res.USD_relative_value / res1.USD_relative_value"}




@app.get('/user/<user_id>')
def login_get(user_id):
    res = User.query.filter_by(login=user_id).first()
    return res


@app.post('/currency/trade/<currency_UPS1>/<currency_UPS2>')
def exchange(currency_UPS1, currency_UPS2):


    req = request.json
    date_now = datetime.datetime.now().strftime("%d-%m-%Y")
    amount = req['data']['amount']
    user_id = 1
    user_balance1 = Account.query.filter_by(user_id=user_id, currency_name=currency_UPS1).first()
    user_balance2 = Account.query.filter_by(user_id=user_id, currency_name=currency_UPS2).first()
    cur1_USD_relative_value = Currency.query.filter_by(name=currency_UPS1, date=date_now).first()
    cur2_USD_relative_value = Currency.query.filter_by(name=currency_UPS2, date=date_now).first()

    need_cur2 = amount * cur1_USD_relative_value.USD_relative_value / cur2_USD_relative_value.USD_relative_value


    if user_balance2.balance > need_cur2 and cur1_USD_relative_value.available_quantity > amount:
        user_balance2.balance = user_balance2.balance - need_cur2
        cur1_USD_relative_value.available_quantity = cur1_USD_relative_value.available_quantity + need_cur2
        cur2_USD_relative_value.available_quantity = cur2_USD_relative_value.available_quantity - amount
        user_balance1.balance = user_balance1.balance + amount

        db.session.add(user_balance2)
        db.session.add(cur1_USD_relative_value)
        db.session.add(cur2_USD_relative_value)
        db.session.add(user_balance1)
        db.session.commit()

        return "ok"
    else:
        return 'Error'


@app.post('/currency/<name>/review')
def currency_review_post(name):
    req = request.json
    cur_name = req['data']['currency_name']
    rating = req['data']['rating']
    comment = req['data']['comment']

    review = Rating(currency_name=name, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    return 'OK'


@app.put('/currency/<name>/review')
def currency_review_put(name):
    return f'Review currency {name}, PUT method'


@app.delete('/currency/<name>/review')
def currency_review_gelete(name):
    return f'Review currency {name}, DELETE method'



@app.post('/user/transfer')
def transfer():
   pass


@app.get('/user/<user>/history')
def user_history(user):

    res = TransactionHistory.query.filter_by(user_id=user).all()
    return [it.to_dict() for it in res]



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
