# 📝 Mini Task Tracker (Pure Python + Tailwind CSS)

A **simple task management web app** built using only the Python standard library for the backend and **Tailwind CSS (via CDN)** for the frontend.  
No frameworks, no external dependencies — runs anywhere you have Python.

---

## 📌 Features
- ✅ Add new tasks
- 📝 View all tasks
- 🔄 Mark tasks as complete/incomplete
- ❌ Delete tasks
- 💾 Data saved in a `JSON` file (persistent storage)
- 🎨 Clean UI with Tailwind CSS

---

## 📂 Project Structure
mini-task-tracker/
├─ app/
│ ├─ server.py # Main HTTP server
│ ├─ routes.py # URL routes & controller logic
│ ├─ storage.py # Load/save tasks to JSON
│ ├─ html.py # Simple template rendering
│ ├─ validators.py # Form input validation
│ └─ utils.py # Helpers (IDs, parsing, HTTP response)
│
├─ templates/
│ ├─ base.html
│ ├─ index.html
│ └─ components/
│ └─ task_row.html
│
├─ data/
│ └─ tasks.json # Task data storage
│
├─ run.sh # Script to run the server
└─ README.md

---

## 🚀 Getting Started

### 1️⃣ Requirements
- Python **3.8+**
- No external libraries needed

### 2️⃣ Install
Clone the repository:
```bash
git clone https://github.com/yourusername/mini-task-tracker.git
cd mini-task-tracker
