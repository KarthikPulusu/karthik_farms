# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='My Website')

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="karthik",        # Replace with your MySQL username
    password="karthik@007",    # Replace with your MySQL password
    database="karthikfarms" # Replace with your database name
)

# Route to display the form
@app.route('/')
def form():
    return render_template('buyform.html')  # Updated to match your HTML file name

# Route to handle form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    number = request.form['number']
    address = request.form['address']
    pincode = request.form['pincode']
    gender = request.form['gender']
    item = request.form['item']
    quantity = request.form['quantity']
    transaction_id = request.form['transaction_id']

    cursor = db.cursor()
    query = """
        INSERT INTO orders (name, number, address, pincode, gender, item, quantity, transaction_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, number, address, pincode, gender, item, quantity, transaction_id))
    db.commit()
    cursor.close()

    return "Order saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)

