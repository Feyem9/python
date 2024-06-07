from flask import render_template , session , redirect #type:ignore

def index():
    return render_template('index_page.html')

def account():

    if 'auth' in session:
        
        return render_template('account.html')
    return redirect('/auth/login')