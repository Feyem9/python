from flask import render_template , redirect , request , session #type:ignore
from models.user_model import Users
from werkzeug.security import generate_password_hash , check_password_hash # type:ignore
from config import db


def login():
    return render_template('/auth/login.html')


def register():
    return render_template('/auth/register.html')

def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = Users.query.filter_by(email=email).first()
    if user != user :
        return redirect('/auth/login' , message='please register before login')
    elif check_password_hash(user.password , password) == False:
        return redirect('/auth/login')

    session['auth'] = {
        "id" : user.id , 
        "username": user.username
    }
    return redirect('/account')


def register_post():

    email = request.form.get('email')
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_Password')

    # print(request.form)
    if password != confirm_password:
        return redirect('/auth/register')
    
    user = Users.query.filter_by(email=email).first()
    if user:
        return redirect('/auth/register')
    
    new_user = Users(email=email , name=name , username=username , password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return redirect('/auth/login')


def logout():

    if 'auth' in session:
        session.pop('auth' , None)
    return redirect('/auth/login')