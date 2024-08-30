from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Update this with your actual MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://karthik:karthik%40007@localhost/karthikfarms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.BigInteger, nullable=False)
    address = db.Column(db.Text, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('male', 'female', 'others'), nullable=False)
    item = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.String(20), nullable=False)
    transaction_id = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('buyform.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Fetch data from the form
    name = request.form['name']
    number = request.form['number']
    address = request.form['address']
    pincode = request.form['pincode']
    gender = request.form['gender']
    item = request.form['item']
    quantity = request.form['quantity']
    transaction_id = request.form['transaction_id']
    
    # Create a new order entry
    new_order = Order(
        name=name,
        number=number,
        address=address,
        pincode=pincode,
        gender=gender,
        item=item,
        quantity=quantity,
        transaction_id=transaction_id
    )
    
    # Add to session and commit
    db.session.add(new_order)
    db.session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    db.create_all()  # This line will create the table in the database if it doesn't exist
    app.run(debug=True)
