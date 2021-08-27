import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'My top secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)



class Asset(db.Model):
    __tablename__= 'asset'
    id=db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    serial_number = db.Column(db.Text)
    asset_number = db.Column(db.Text)
    BU = db.Column(db.Text)
    BL = db.Column(db.Text)
    cost = db.Column(db.Float)

    def __init__(self,type,serial_number,asset_number,BU,BL,cost):
        self.type=type
        self.serial_number=serial_number
        self.asset_number=asset_number
        self.BU=BU
        self.BL=BL
        self.cost=cost

    def __repr__(self):
        return  f'Asset type: {self.type} Serial Number: {self.serial_number}'

@app.route("/")
def home():
    # return "Hello, Flask!"
    return render_template('index.html')

# Add a new asset and commit to databse
@app.route('/add', methods=['GET', 'POST'])
def add_asset():
    form=AddForm()
    # if form.is_valid():
    if form.validate_on_submit():
        type = form.type.data
        asset_number = form.asset_number.data
        serial_number = form.serial_number.data
        BU = form.BU.data
        BL = form.BL.data
        cost = form.cost.data
        new_asset = Asset(type,asset_number,serial_number,BL,BU,cost)
        db.session.add(new_asset)
        db.session.commit()
        return redirect(url_for('list_asset'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_asset():
    asset = Asset.query.all()
    return render_template('list_asset.html', asset=asset)


if __name__ == "__main__":
    app.run(debug=True)

