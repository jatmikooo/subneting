# 🌐 Subnet Calculator Web App

A simple web-based subnet calculator built with Flask. This tool allows users to enter an IP address in CIDR notation and returns useful subnet information.

Live Demo: [https://bwjatmiko.my.id/subneting](https://bwjatmiko.my.id/subneting)

---

## 🧩 Features

- Input CIDR (e.g. `192.168.1.0/24`)
- Calculate subnet mask, IP range, network address, and more
- Web interface with clean HTML template
- Modular code (logic separated from web handler)
- Mountable at any subpath using `DispatcherMiddleware`

---

## 🗂 Project Structure

subneting/
├── app.py # Main app with DispatcherMiddleware
├── subnet_calc.py # Subnet calculation logic
├── templates/
│ └── index.html # Web form and results
├
├── requirements.txt # Python dependencies
└── README.md # This file

## Cara Menjalankan

1. Clone repo:
   git clone https://github.com/jatmikooo/subneting.git
   cd subneting

2. Create virtual environment & install dependencies:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Start the app using Gunicorn:
   gunicorn --bind 127.0.0.1:8001 app:app

4. Open Localhost port 8001
   http://127.0.0.1:8001/

## Contoh Input

- `192.168.1.0/24`
- `10.0.0.0/22`
