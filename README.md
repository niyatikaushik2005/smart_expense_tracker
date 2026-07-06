# SmartExpense — AI-Powered Company Expense Intelligence Platform

A full-stack expense tracking and forecasting platform built for small businesses and startups. SmartExpense goes beyond simple expense logging — it uses machine learning to detect anomalies in spending patterns and forecast future expenses, helping companies make smarter financial decisions.

---

## Features

### Backend API
- JWT-based authentication (register, login) with bcrypt password hashing
- Expense logging with category tagging (salaries, marketing, operations, etc.)
- RESTful API built with FastAPI and auto-generated Swagger documentation

### ML Intelligence
- **Anomaly Detection** — flags unusual spikes in spending using Isolation Forest
- **Expense Forecasting** — predicts future expenses using Facebook Prophet time series model

### Frontend Dashboard
- Clean, minimal dashboard built with HTML, CSS, and vanilla JavaScript
- Interactive charts powered by Chart.js
- Real-time spending insights and forecast visualization

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Python |
| Database | MongoDB Atlas |
| Authentication | PyJWT, bcrypt, passlib |
| ML | scikit-learn (Isolation Forest), Prophet |
| Frontend | HTML, CSS, Chart.js |
| Deployment | Render |

---

## Project Structure

```
smartexpense/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── database.py          # MongoDB connection
│   ├── models/
│   │   ├── user.py          # Pydantic models for auth
│   │   └── expense.py       # Pydantic models for expenses
│   ├── routes/
│   │   ├── auth.py          # Register, login endpoints
│   │   ├── expenses.py      # Expense CRUD endpoints
│   │   └── analytics.py     # Forecasting, anomaly endpoints
│   ├── ml/
│   │   ├── forecasting.py   # Prophet time series forecasting
│   │   └── anomaly.py       # Isolation Forest anomaly detection
│   └── utils/
│       └── jwt_handler.py   # JWT token creation and verification
├── frontend/
│   ├── index.html           # Login/Register page
│   ├── dashboard.html       # Main dashboard
│   ├── style.css            # Styling
│   └── app.js               # API calls and chart rendering
├── .env                     # Environment variables (not committed)
└── requirements.txt         # Python dependencies
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- MongoDB Atlas account (free tier works)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smartexpense.git
cd smartexpense

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file inside the `backend/` folder:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0
SECRET_KEY=your_secret_key_here
```

### Run the API

```bash
cd backend
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation.

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |

### Expenses (coming soon)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses/add` | Add a new expense |
| GET | `/expenses/` | Get all expenses |
| DELETE | `/expenses/{id}` | Delete an expense |

### Analytics (coming soon)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/analytics/summary` | Monthly spending summary |
| GET | `/analytics/anomalies` | Detect spending anomalies |
| GET | `/analytics/forecast` | Forecast future expenses |

---

## How the ML Works

### Anomaly Detection
Uses **Isolation Forest** from scikit-learn. The model trains on historical expense data and assigns an anomaly score to each new expense. Expenses that deviate significantly from historical patterns (e.g., marketing spend 3x the monthly average) are flagged automatically.

### Expense Forecasting
Uses **Facebook Prophet**, a time series forecasting model designed for business data with seasonality. Given 3+ months of expense history by category, Prophet predicts the next 3 months of spending with confidence intervals.

---

## Why This Project

Most expense tracking tools (Splitwise, QuickBooks) focus on logging and reporting. SmartExpense adds a predictive layer — helping small businesses anticipate budget overruns before they happen and catch unusual spending automatically.

---

## Status

🟡 In Progress — Auth complete(w/o middleware), expense routes and ML layer in development.

---

## Author

**Niyati Kaushik**  
B.Tech CSE, Jaypee Institute of Information Technology  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourusername)
