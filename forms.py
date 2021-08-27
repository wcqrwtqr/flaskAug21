from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField

class AddForm(FlaskForm):
    type = StringField('Asst Type')
    asset_number = StringField('Asset number')
    serial_number= StringField('SN')
    BU = StringField('BU')
    BL = StringField('BL')
    cost = FloatField('Cost')
    submit = SubmitField('Add Asset')

# class DeleteForm(FlaskForm):
#     id = IntegerField('ID number of puppy to remove')
#     submit = SubmitField('Remove Puppy')

