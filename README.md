# 🧪 Chemical Equipment Parameter Visualizer

A hybrid **Web + Desktop** data analytics application for visualizing chemical equipment parameters from CSV files.

This system allows users to upload equipment datasets, perform automatic analysis using Python, and visualize results through interactive dashboards.

---

## 🚀 Features

* 📁 CSV file upload
* 📊 Automatic data analysis using Pandas
* 📈 Summary statistics (count, averages)
* 📉 Equipment type distribution chart
* 🗂 Upload history stored in database
* 🌐 Web dashboard (React + Chart.js)
* 💻 Desktop application (PyQt5 + Matplotlib)

---

## 🧠 Tech Stack

| Layer        | Technology                            |
| ------------ | ------------------------------------- |
| Backend      | Django, Django REST Framework, Pandas |
| Web Frontend | React.js, Chart.js                    |
| Desktop App  | PyQt5, Matplotlib                     |
| Database     | SQLite                                |

---

## 🏗 System Architecture

CSV File → Django Backend API → Data Processing → Database → Web & Desktop Visualization

---

## ⚙️ Setup Instructions

### 1️⃣ Backend

```bash
cd backend
pip install django djangorestframework pandas reportlab
python manage.py runserver
```

---

### 2️⃣ Web Frontend

```bash
cd web-frontend
npm install
npm start
```

Open: [http://localhost:3000](http://localhost:3000)

---

### 3️⃣ Desktop App

```bash
cd desktop-app
pip install pyqt5 requests matplotlib
python desktop_app.py
```

---

## 📊 How the System Works

1. User uploads CSV file containing equipment parameters
2. Django backend reads data using Pandas
3. System calculates:

   * Total equipment count
   * Average flowrate
   * Average pressure
   * Average temperature
   * Equipment type distribution
4. Data is stored in database
5. Web & Desktop apps visualize results

---

## 🎥 Demo Video

(Add your demo video link here)

---

## 📌 Author

Anchita Jain

Just tell me ✨
