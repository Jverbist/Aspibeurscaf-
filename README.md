# 📈 Aspi Beurs Café — Dynamic Drink Pricing System

A full-featured, real-time bar pricing application that simulates a stock market. Built with **FastAPI**, **SQLite**, **Bootstrap**, and **Chart.js**, it allows a bar to dynamically adjust prices based on demand and sales.

---

## 🔧 Features

- 📊 Real-time pricing that reacts to sales
- 🎨 Live chart with color-coded drinks
- 🖤 Dark mode dashboard view
- 🔄 Auto-refreshing dashboard every 5 seconds
- 👨‍💼 Admin panel with basic auth
- 🧹 Reset price or price history
- 🔒 Per-drink price floor enforcement
- 🐳 Deployable via Docker

---

## 📁 Project Structure

```
aspibeurscafe/
├── backend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
├── main.py
├── models.py
├── crud.py
├── database.py
├── schemas.py
├── templates/
│   └── index.html
│   └── manage.html
├── static/
├── data/
│   └── stock_cafe.db
```

---

## 🚀 Setup & Deployment

### 1. ✅ Install Docker

Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed.

---

### 2. ✅ File Placement

- Put your code (`main.py`, `models.py`, etc.) in the root `aspibeurscafe/`
- Place `Dockerfile`, `docker-compose.yml`, and `requirements.txt` inside `aspibeurscafe/backend/`

---

### 3. ✅ Build and Run

```bash
cd aspibeurscafe/backend
docker compose up --build
```

Open in browser: [http://localhost:8000](http://localhost:8000)

---

## 👩‍💻 Admin Interface

Visit: [http://localhost:8000/manage](http://localhost:8000/manage)  
Default login:  
- Username: `admin`  
- Password: `password`

Actions:
- ✅ Sell a drink
- 🔄 Reset all prices

---

## 📈 Public Dashboard

Visit: [http://localhost:8000](http://localhost:8000)

- Auto-refreshes every 5 seconds
- Shows live price lines or scatter per drink
- Price labels shown on last point
- Reset chart history button available

---

## 🛠 Customization Tips

### Change Drink Seed Data

Edit the `startup_event` in `main.py`:

```python
@app.on_event("startup")
def startup_event():
    drinks = [
        {"name": "Stella", "base_price": 2.5, "min_price": 2.0},
        ...
    ]
```

---

### Change Basic Auth

Edit `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `main.py`:

```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"
```

---

### Reset Database (Wipe Everything)

```bash
rm data/stock_cafe.db
docker compose down
docker compose up --build
```

---

## 🧪 API Endpoints

- `/api/prices` — Live prices (used for dashboard)
- `/api/history/{drink_id}` — Price history for one drink
- `/api/history/all` — All drinks' history (for grouped chart)
- `/api/history/flat` — Flat JSON for scatter charts
- `/sell` — POST with `drink_id`
- `/reset` — Reset all prices
- `/reset-history` — Reset price history (chart only)

---

## 🧠 Technologies

- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTML, Bootstrap, Chart.js
- **Containerization**: Docker, Docker Compose

---

## 📸 Visual Overview

- Dark-mode market dashboard
- Real-time line or dot plots
- Clean table-based admin UI

---

## 📦 Production Tips

- Use PostgreSQL instead of SQLite for multi-user access
- Secure with OAuth (FastAPI Security)
- Use nginx reverse proxy for TLS/SSL and domain routing

---

Enjoy your real-time bar economy 🍻