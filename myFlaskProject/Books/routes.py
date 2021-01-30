from myFlaskProject.models import Book
from flask import render_template,request,redirect,flash,url_for,Blueprint
from myFlaskProject.Books.forms import Bookform
from myFlaskProject import db
from flask_login import current_user,login_required

books=Blueprint('books',__name__)

@books.route("/bookadd",methods=['POST','GET'])
@login_required
def bookadd():
    form=Bookform()
    if form.validate_on_submit():
        print(form.quality.data)
        mrp=form.mrp_book.data
        qlty=form.quality.data
        if qlty==1:
            q='Good as New'
        elif qlty==2:
            q='Medium old'
        elif qlty==3:
            q='Timeworn'
        else:
            q='Poor Quality'
        if qlty==1:
            fp=0.95*mrp
        elif qlty==2:
            fp=0.9*mrp
        elif qlty==3:
            fp=0.85*mrp
        else:
            fp=0.8*mrp
        print(fp)
        flash('Your book has been added','success')
        book=Book(bookname=form.bookname.data,author=form.author.data,language=form.language.data
                  ,mrp_book=form.mrp_book.data,quality_check=q,finalprice=fp,user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('users.profile'))
    return render_template('bookadd.html',form=form)

@books.route("/library")
@login_required
def library():
    page=request.args.get('page',1,type=int)
    books=Book.query.paginate(page=page,per_page=3)
    return render_template('library.html',books=books)

@books.route("/mylibrary")
@login_required
def mylibrary():
    books=db.session.query(Book).filter(Book.user_id==current_user.id).all()
    return render_template('mylibrary.html',books=books)

@books.route("/mylibrary/delete/<int:book_id>",methods=['POST'])
@login_required
def delete_book(book_id):
    book=Book.query.get_or_404(book_id)
    print(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Your book has been deleted!','success')
    return redirect(url_for('books.mylibrary'))

@books.route("/library/buybook/<int:book_id>",methods=['POST'])
@login_required
def buy_book(book_id):
    book=Book.query.get_or_404(book_id)
    points=current_user.points_earned
    packageid=current_user.package_id
    if packageid==1:
        points_to_be_added=10
    elif packageid==2:
        points_to_be_added=20
    elif packageid==3:
        points_to_be_added=30
    else:
        points_to_be_added=0
    total_points=points+points_to_be_added
    print(total_points)
    current_user.points_earned=total_points
    db.session.delete(book)
    db.session.commit()
    flash('Your purchase is successfull!','success')
    return redirect(url_for('books.library'))