from flask import render_template , request  , redirect# type:ignore
from config import db
from models.user_model import Users


def index_user():
    users = Users.query.all()
    return render_template('index_user.html' , title="HOME PAGE" , users=users)


def add_user():
    return render_template('user.html' , title="ADD USER")


def create_user():
    form = request.form
    name = form['name']
    email = form['email']
    phone = form ['phone']

    user = Users(name=name, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

def view_user(user_id):
    users = Users.query.filter_by(id=user_id).first()
    if users is None:
        return redirect('/')
    return render_template('view_user.html' , users=users)


def update_user(user_id):
    users = Users.query.filter_by(id=user_id).first()
    if users is None:
        return redirect('/')
    if request.method == "GET":
      return render_template('update_user.html' , users=users , title="UPDATE POST")
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        phone = form ['phone']
        users.name = name
        users.email = email
        users.phone = phone
        db.session.commit()
        return redirect('/')
    return render_template('update_user.html' , users=users , title="updated succesfully")

def delete_user(user_id):
    if request.method == 'POST' :
        if request.form['_method'] == 'DELETE':
            user = Users.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return redirect('/')   


