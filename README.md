# DISASTER_MANAGEMENT_SYSTEM
![image](https://github.com/user-attachments/assets/99f09c62-6655-4640-9162-122f34c46735)

# 🌍 Disaster Management System (Flask + HTML/CSS + GPS)

A smart and intuitive **Disaster Management System** built using **Flask** for the backend and **HTML/CSS** for the frontend.  
This project helps authorities and citizens to **track, manage, and respond to disasters** by offering real-time location support, resource tracking, volunteer info, and donation integration — all in one interface.

> 🧠 Designed with tech enthusiasts and social impact in mind!

---

## 🚀 Features

✅ **Responsive Home Interface**  
✅ **Live GPS Location Tracker** using browser geolocation  
✅ **View & Add Disasters**  
✅ **Volunteer & Resource Management**  
✅ **Emergency Contact Directory**  
✅ **Donations Page** for public support  
✅ Built using **Python (Flask)** + **HTML/CSS**

---

## 📁 Project Structure


Disaster_Management_System/
│
├── app.py # Flask application
├── static/
│ └── style.css # Styling for HTML pages
├── templates/
│ ├── index.html # Home page with GPS
│ ├── add-disaster.html
│ ├── disasters.html
│ ├── emergency-contacts.html
│ ├── resources.html
│ ├── volunteers.html
│ └── donations.html
└── README.md # This file


> 📝 HTML templates are stored in the `templates/` folder as Flask expects. Static assets like CSS should be inside `static/`.

---

## 🛠️ Technologies Used

- **Python 3**  
- **Flask** – for routing and backend  
- **HTML5 + CSS3** – for frontend UI  
- **Browser Geolocation API** – to fetch live GPS coordinates

---

## 💻 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/disaster-management-system.git
cd disaster-management-system
---

2. **Install Flask (if not already)**

bash
Copy
Edit
pip install flask
Run the app

bash
Copy
Edit
python app.py
Open in browser

Visit: http://127.0.0.1:5000

🌐 GPS Integration
Uses navigator.geolocation in the browser

Displays:

Current latitude & longitude

Last known location

Optional: exact address (with reverse geocoding if extended)

 Future Enhancements
Add disaster database storage (e.g. SQLite)

Admin authentication system

RESTful API for mobile integration

Volunteer registration & login

SMS alerts via Twilio

Integrate real-time maps using Leaflet/Mapbox

Made For
This project is made for:

Social impact hackathons

Disaster relief automation ideas

Anyone wanting to mix Flask + Location + UI


### Contributing
Pull requests and suggestions are welcome!
Let’s build something impactful together. 💙
