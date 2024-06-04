from flask import render_template , request  , redirect# type:ignore
from config import db
import requests
from requests.auth import HTTPBasicAuth
from models.article_model import Article
from models.user_model import Users 



def index():
    articles = Article.query.all()
    users = Users.query.all()

    return render_template('index.html' , title="HOME PAGE" , articles=articles , users=users)


def add_post():
    return render_template('post.html' , title="ADD POST")


def create():
    form = request.form
    title = form['title']
    author = form['author']
    description = form ['description']

    article = Article(title=title, author=author, description=description)
    db.session.add(article)
    db.session.commit()

    return redirect('/')

def view(article_id):
    article = Article.query.filter_by(id=article_id).first()
    if article is None:
        return redirect('/')
    return render_template('view.html' , article=article)


def update(article_id):
    article = Article.query.filter_by(id=article_id).first()
    if article is None:
        return redirect('/')
    if request.method == "GET":
      return render_template('update.html' , article=article , title="UPDATE POST")
    elif request.method == "POST":
        form = request.form
        title = form['title']
        author = form['author']
        description = form ['description']
        article.title = title
        article.author = author
        article.description = description
        db.session.commit()
        return redirect('/')
    return render_template('update.html' , article=article , title="updated succesfully")

def delete(article_id):
    if request.method == 'POST' :
        if request.form['_method'] == 'DELETE':
            articles = Article.query.get(article_id)
            db.session.delete(articles)
            db.session.commit()
            return redirect('/')   


