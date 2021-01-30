from myFlaskProject.models import Package,User
from flask import render_template,request,redirect,flash,url_for,Blueprint
from myFlaskProject.Users.forms import RegistrationForm,LoginForm,UpdateAccountForm
from myFlaskProject import db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required

users=Blueprint('users',__name__)

@users.route("/signup",methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_passwrd=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,address=form.address.data,
                  password=hashed_passwrd,package_id=form.package.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!You can now login','success')
        return redirect(url_for('users.login'))
    return render_template('signup.html',form=form)


@users.route("/home",methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('users.profile'))
        else:
            flash('Login unsuccessful.Please check username and password','danger')
    return render_template('index.html',form=form)



@users.route("/profile",methods=['POST','GET'])
@login_required
def profile():
    pkid=current_user.package_id
    pkname=db.session.query(Package.packagename).filter(Package.id==pkid).first()
    pckgname=pkname[0]
    if current_user.points_earned>=100:
        flash('You have a 100 reward points! You get a book for free','success')
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        current_user.package_id=form.package.data
        db.session.commit()
        flash('Your account has been updated','success')
        return redirect(url_for('users.profile'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
        form.package.data=pckgname

    return render_template('home.html',form=form,pckgname=pckgname)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.login'))