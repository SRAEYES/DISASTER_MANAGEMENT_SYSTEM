from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

# Sample data for demonstration
disasters = [
    {"id": 1, "name": "Flood", "location": "City A", "severity": "High"},
    {"id": 2, "name": "Earthquake", "location": "City B", "severity": "Critical"},
]

resources = [
    {"id": 1, "name": "Water Bottles", "quantity": 500, "location": "Warehouse A"},
    {"id": 2, "name": "First Aid Kits", "quantity": 200, "location": "Warehouse B"},
]

volunteers = [
    {"id": 1, "name": "Alice Johnson", "role": "Medic", "contact": "alice@example.com"},
    {"id": 2, "name": "Bob Smith", "role": "Rescuer", "contact": "bob@example.com"},
]

emergency_contacts = [
    {"id": 1, "name": "Fire Department", "contact": "123-456-7890"},
    {"id": 2, "name": "Medical Services", "contact": "098-765-4321"},
]

donations = []  # List to store donations

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# View disasters
@app.route('/disasters')
def view_disasters():
    return render_template('disasters.html', disasters=disasters)

# Add disaster
@app.route('/add-disaster', methods=['GET', 'POST'])
def add_disaster():
    if request.method == 'POST':
        new_disaster = {
            "id": len(disasters) + 1,
            "name": request.form['name'],
            "location": request.form['location'],
            "severity": request.form['severity']
        }
        disasters.append(new_disaster)
        flash("Disaster added successfully!")
        return redirect(url_for('view_disasters'))
    return render_template('add_disaster.html')

# View resources
@app.route('/resources')
def view_resources():
    return render_template('resources.html', resources=resources)

# View volunteers
@app.route('/volunteers')
def view_volunteers():
    return render_template('volunteers.html', volunteers=volunteers)

# View emergency contacts
@app.route('/emergency-contacts')
def view_emergency_contacts():
    return render_template('emergency_contacts.html', contacts=emergency_contacts)

# Donation page
@app.route('/donations', methods=['GET', 'POST'])
def donations_page():
    if request.method == 'POST':
        donation = {
            "type": request.form['type'],
            "amount": request.form['amount'],
            "description": request.form['description']
        }
        donations.append(donation)
        flash("Donation added successfully!")
        return redirect(url_for('donations_page'))
    return render_template('donations.html', donations=donations)

# Add routes for other functionalities here...

if __name__ == '__main__':
    app.run(debug=True)
