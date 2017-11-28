from flask import Flask, render_template
from db import db, Orders
from datetime import datetime, timedelta
from score import get_color_of_score


app = Flask(__name__)

POSTGRES = {
    'user': 'score',
    'pw': 'Rysherat2',
    'db': 'shop',
    'host': 'shopscore.devman.org',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def score():
    with app.app_context():
        today_orders = Orders.query.filter(
            Orders.created >= datetime.today().date())
        today_orders_count = today_orders.count()
        unprocessed_orders = today_orders.filter(Orders.confirmed.is_(None))
        unprocessed_orders_count = unprocessed_orders.count()
        processed_orders_count = today_orders_count - unprocessed_orders_count
        if unprocessed_orders_count is not 0:
            order_with_max_time = unprocessed_orders.order_by(
                (datetime.today()-Orders.created).desc()).first()
            max_waiting_time = datetime.today() - order_with_max_time.created
        else:
            max_waiting_time = timedelta(minutes=0)
        color_of_score = get_color_of_score(max_waiting_time)
        max_time_without_microseconds = max_waiting_time - timedelta(
            microseconds=max_waiting_time.microseconds)
    return render_template('score.html',
                           maxtime=max_time_without_microseconds,
                           color=color_of_score,
                           unprocessed_orders_count=unprocessed_orders_count,
                           processed_orders_count=processed_orders_count)


if __name__ == "__main__":
    app.run()
