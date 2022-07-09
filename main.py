from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///search.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Websites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_site = db.Column(db.String(256), primary_key=False)
    title = db.Column(db.String(256), primary_key=False)
    about = db.Column(db.Text, primary_key=False)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search', methods=['POST', 'GET'])
def ndex():
    q = request.args.get('q')

    if q:
        websites = Websites.query.filter(Websites.title.contains(q) | Websites.about.contains(q))
        return render_template('ser.html', data=websites)
    else:
        websites = Websites.query.order_by(Websites.title).all()

    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def ad():
    if request.method == "POST":
        title = request.form['Title']
        about = request.form['About']
        url_site = request.form['Url_site']

        websites = Websites(title=title, about=about, url_site=url_site)

        try:
            db.session.add(websites)
            db.session.commit()
            return redirect('/search')
        except:
            return "Ошибка добавления"

    return render_template('add.html')


@app.route('/ser', methods=['POST', 'GET'])
def ser():
    q = request.args.get('q')

    if q:
        websites = Websites.query.filter(Websites.titel.contains(q) | Websites.about.contains(q))
        return render_template('ser.html', data=websites)
    else:
        websites = Websites.query.order_by(Websites.title).all()

    return render_template('ser.html', data=websites)


def serch(mes):
    pass


if __name__ == '__main__':
    app.run(debug=True)
