from flask import Flask, render_template, redirect, make_response, request, session, abort
from data import db_session
from data.Jobs import Jobs
from data.users import User
from forms.news import NewsForm
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, current_user, login_required
import datetime

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


'''@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    db_sess = db_session.create_session()
    jobs = Jobs()
    return render_template('jobs.html', title='Добавление работы')'''


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
