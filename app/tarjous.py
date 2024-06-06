from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # replace with your actual secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'  # replace with your actual MySQL connection string
db = SQLAlchemy(app)

class Tarjous(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    yritys_nimi = db.Column(db.String(120), nullable=False)
    vastaanottaja1 = db.Column(db.String(120), nullable=False)
    vastaanottaja2 = db.Column(db.String(120))
    tarjoaja = db.Column(db.String(120), nullable=False)
    valmistelija = db.Column(db.String(120), nullable=False)
    viite = db.Column(db.String(120))
    lainaus_luotu = db.Column(db.String(120))
    tarjous_päättyy = db.Column(db.String(120))
    loppusumma = db.Column(db.Integer)
    alv = db.Column(db.Integer)
    tuotteet_ja_palvelut = db.Column(db.Text)
    määrä = db.Column(db.Integer)
    hinta = db.Column(db.Integer)
    yhteenveto = db.Column(db.Text)
    kertasumma = db.Column(db.Integer)
    verottaa = db.Column(db.Integer)
    prosenttialennus = db.Column(db.Integer)
    kaikki_yhteensä = db.Column(db.Integer)
    sopimuksen_kokonaisarvo = db.Column(db.Integer)
    kommentit = db.Column(db.Text)
    ostoehdot = db.Column(db.Text)
    allekirjoitus1 = db.Column(db.String(120))
    allekirjoitus2 = db.Column(db.String(120))
    päiväys = db.Column(db.String(120))
    tulostettu_nimi = db.Column(db.String(120))

    


if __name__ == '__main__':
    app.run(debug=True)

