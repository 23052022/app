from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    currency_name = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "self.user_id": self.user_id,
            'self.balance': self.balance,
            'self.currency_name': self.currency_name
        }


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    USD_relative_value = db.Column(db.Numeric, nullable=False)
    available_quantity = db.Column(db.Numeric, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "self.name": self.name,
            'self.USD_relative_value': self.USD_relative_value,
            'self.available_quantity': self.available_quantity,
            'self.date': self.date
        }


class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer(), nullable=False)
    opening_date = db.Column(db.Text, nullable=False)
    closing_date = db.Column(db.Text)
    balance = db.Column(db.Integer, nullable=False)
    interest_rate = db.Column(db.Numeric, nullable=False)
    conditions = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "self.user_id": self.user_id,
            'self.opening_date': self.opening_date,
            'self.closing_date': self.closing_date,
            'self.balance': self.balance,
            "self.interest_rate": self.interest_rate,
            'self.conditions': self.conditions

        }


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    currency_name = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "self.currency_name": self.currency_name,
            'self.rating': self.rating,
            'self.comment': self.comment
        }


class TransactionHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Text, nullable=False)
    operation_type = db.Column(db.Text, nullable=False)
    currency_num_spent = db.Column(db.Numeric, nullable=False)
    currency_num_obtained = db.Column(db.Numeric, nullable=False)
    date_time = db.Column(db.Text, nullable=False)
    account_from_which_the_transaction = db.Column(db.Numeric, nullable=False)
    account_on_which_the_transaction = db.Column(db.Numeric, nullable=False)
    commission = db.Column(db.Numeric, nullable=False)

    def to_dict(self):
        return {
            "self.user_id": self.user_id,
            'self.operation_type': self.operation_type,
            'self.currency_num_spent': self.currency_num_spent,
            'self.currency_num_obtained': self.currency_num_obtained,
            "self.date_time": self.date_time,
            'self.account_from_which_the_transaction': self.account_from_which_the_transaction,
            "self. account_on_which_the_transaction": self.account_on_which_the_transaction,
            'self. commission': self.commission
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    login = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "self.login": self.login,
            'self.password': self.password
        }
