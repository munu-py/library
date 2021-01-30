from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField,IntegerField
from wtforms.validators import DataRequired

class Bookform(FlaskForm):
    bookname=StringField('Book Name',validators=[DataRequired()])
    author=StringField('Author',validators=[DataRequired()])
    language=StringField('Language',validators=[DataRequired()])
    mrp_book=IntegerField('MRP of Book',validators=[DataRequired()])
    files={(1,'Good as New'),(2,'Medium old'),(3,'Timeworn'),(4,'Poor Quality')}
    quality = RadioField('Quality check', choices=files,coerce=int,validators=[DataRequired()])
    submit = SubmitField('Add')
