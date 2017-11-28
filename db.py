from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(200))
    contact_phone = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    status = db.Column(db.Integer)
    created = db.Column(db.DateTime, index=True)
    confirmed = db.Column(db.DateTime, index=True)
    comment = db.Column(db.Text)
    price = db.Column(db.Numeric)
