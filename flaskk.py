from flask import Flask, render_template, escape, abort, request

# import sys
# sys.path.append('../ORM')
# from ORM.app import db, app
# from ORM.models import Card, User, Category, Product, Feedback, OrderUser, OrderHistory
from service import *

# app = Flask(__name__)

descr=['description of this wonderful book in progress']*6
name_pr=['C.P. Company 971-021','Louis Vuitton: Catwalk','Louis Vuitton: Celebrating Monogram','Hello, My Name Is Paul','A Denim Story: Inspirations From Bellbottoms To Boyfriends','Skira']
link_img=['CP Company.jpg','LouviusVuitton.jpg','Lv.jpg','PaulSmith.jpg','Rizzoli.jpg','Basquiat.jpg']
products=[]
# card0=/addCard(number='123', valid_thru='29/09', holder_name='Store', cvc=100)

for i in range(len(descr)):
    products.append(Product(name=name_pr[i], description=descr[i], img=link_img[i]))
feedbacks=[]
products_three=products[:3]
# print(products[0].description)
@app.route('/')
def homepage():
    return render_template('HomePage.html', items = products_three)

@app.route('/About', methods=['GET', 'POST'])
def about():
    if request.method=='POST':
        login = request.form.get('login')
        text =request.form.get('review')
        if login !='' and text!='':
            fb=addFeedback(login,text)
    feedbacks=getFeedback()
    return render_template('About.html', feedbacks=feedbacks)
#
@app.route('/Catalog')
def catalog():
    return render_template('Catalog.html', items = products)
#
@app.route('/Product/<item>')
def product(item):
    item=escape(item)
    for el in products:
        if el.name==item:
            return render_template('Product.html',item = el)
@app.route('/Account/<user>')
def user(user):
    user=escape(user)
    return render_template('User.html', user=el)
@app.route('/Account', methods=['GET', 'POST'])
def account():
    if request.method=='POST':
        name= request.form.get('name')
        name=''
        login=request.form.get('login')
        passw=request.form.get('password')
        if name!='':
            addUser(Card(number='323', valid_thru='28/09', holder_name='Sttore', cvc=100),login = login,password= passw,FIO= name)
        else:
            users=getUsers()
            for el in users:
                if el.login==login:
                    return render_template('User.html', user=el)

 

    return render_template('Account.html')


if __name__=='__main__':
    app.run(debug=True)
