# 📰 NewsTrace — Media Network Intelligence Prototype

**Challenge:** NewsTrace Hackathon (Unstop)  
**Date:** October 25–26, 2025  
**Developer:** Saad Khan  & Atufa Hasan

---

## 🚀 Overview

**NewsTrace** is a prototype that automatically collects and analyzes journalist and article data from news outlets.  
It demonstrates how media ecosystems can be mapped using public web data.

The project currently supports scraping, structuring, and visualizing basic journalist information from major news sites.

---

## 🧠 Core Features (Prototype)

- ✅ Flask backend and web dashboard  
- ✅ Web scraping with BeautifulSoup  
- ✅ Extracts article titles, authors, and sections   
- ⚙️ Planned: automatic outlet detection  
- ⚙️ Planned: journalist network graph & clustering  
- ⚙️ Planned: NLP topic extraction  

---

## 🏗️ Architecture

User → Flask Server → Scraper (Requests + BeautifulSoup) → JSON/CSV → Dashboard (HTML/JS)


**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python (Flask)  
**Libraries:** requests, beautifulsoup4, pandas (optional)  
**Storage:** In-memory (JSON) for prototype

---

## 🧩 Folder Structure

NewsTrace/ \
├── app.py\
├── scraper.py\
├── requirements.txt\
├── README.md\
├── templates/\
│ └── index.html\
├── static/\
│ ├── style.css\
│ └── script.js\
└── data/\


---

## ⚙️ How to Run

### 1️⃣ Create a virtual environment

 1- python -m venv venv\
        source venv/bin/activate   # on Mac/Linux\
        .\venv\Scripts\activate    # on Windows\

2-  pip install -r requirements.txt\ (in virtual environment)\
3-  python app.py\
4-  http://127.0.0.1:5000/\

---
## 📈 Future Enhancements (Planned for Hackathon)

Automatic discovery of news outlets (Stage 0)

Full journalist ecosystem mapping (Stage 1)

NLP-based intelligence layer (Stage 2)

Network graph visualization (Stage 3)

Real-time scraping dashboard (Stage 4)

---
## 📸 Prototype Preview

---
## 🧑‍💻 Team

- **Saad Khan** — Project Developer (Backend & Architecture)  
- **Atufa Hasan** — User Experience Designer & Tester  

---
## 📜 License

Open-source prototype created for educational and hackathon use.

