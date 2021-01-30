from myFlaskProject import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Package(db.Model):
    id=db.Column('package_id',db.Integer,primary_key=True)
    packagename=db.Column('package_name',db.String(20),nullable=False)
    users=db.relationship('User',backref='package_info')

class User(db.Model,UserMixin):
    id=db.Column('id',db.Integer,primary_key=True)
    username=db.Column('username',db.String(30),nullable=False)
    email=db.Column('email',db.String(30),nullable=False)
    address=db.Column('address',db.String(100),nullable=False)
    password=db.Column('password',db.String(20),nullable=False)
    points_earned=db.Column('points_earned',db.Integer,default=0)
    books=db.relationship('Book',backref='owner')
    package_id=db.Column('package_id',db.ForeignKey(Package.id))

class Book(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    bookname=db.Column('book_name',db.String(200),nullable=False)
    author=db.Column('author',db.String(200),nullable=False)
    language=db.Column('language',db.String(30),nullable=False)
    mrp_book=db.Column('mrp_book',db.Integer,nullable=False)
    quality_check=db.Column('quality_check',db.Integer,nullable=False,default=0)
    finalprice=db.Column('finalprice',db.Integer,nullable=False,default=0)
    user_id=db.Column('user_id',db.ForeignKey(User.id),nullable=False)
