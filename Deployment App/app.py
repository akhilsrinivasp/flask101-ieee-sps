from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qecdnmhteytuxb:3828e0a4e30123f1028d45826780df72ebfe8c855c03faf698cf88fde82ce484@ec2-34-235-31-124.compute-1.amazonaws.com:5432/dd76ac8qchq4b1'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class ShoppingList(db.Model):
    __tablename__ = 'shopping_list'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(80), unique=True)
    quantity=db.Column(db.Integer)
    note=db.Column(db.String(100), nullable=True)
    
@app.route('/', methods = ['GET', 'POST'])
def note():
    if request.method=='GET':
        items=db.session.query(ShoppingList).all()
        return render_template('index.html', items=items)
    elif request.method=='POST':
        name=request.form['name']
        quantity=request.form['quantity']
        note=request.form['note']
        item=ShoppingList(name=name, quantity=quantity, note=note)
        db.session.add(item)
        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:item_id>', methods = ['GET', 'POST'])
def delete_item(item_id):
    if request.method=='GET':
        item=db.session.query(ShoppingList).filter(ShoppingList.id==item_id).first()
        db.session.delete(item)
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True,
            port=5001
            )