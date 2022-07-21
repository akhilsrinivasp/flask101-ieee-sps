from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
from about import about_blueprint
print(about_blueprint)
app.register_blueprint(about_blueprint)

class ShoppingList(db.Model):
    __tablename__ = 'shopping_list'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True)
    quantity=db.Column(db.Integer)
    note=db.Column(db.String(100), nullable=True)
    
@app.route('/')
def note():
    items=db.session.query(ShoppingList).all()
    if items is None or len(items) == 0: 
        return """<h1> No items in the list </h1>"""
    return render_template('index.html', items=items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True,
            port=8082)