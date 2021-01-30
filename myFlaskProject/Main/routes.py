from flask import render_template,Blueprint

main=Blueprint('main',__name__)

@main.route("/aboutus")
def about():
    return render_template('aboutus.html')