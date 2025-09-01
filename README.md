# Flask Stock Dashboard

An interactive dashboard for visualizing financial data using the [Marketstack API](https://marketstack.com/).  
The project demonstrates how to connect **Flask** with a REST API, fetch stock data, and render it in a modern dashboard with **Chart.js**.

![Marketstack Dashboard](Marketstack%20Dashboard.jpg)

---

## Features
- Fetches **End of Day (EOD)** stock market data for a chosen ticker (e.g., AAPL, NVDA, MSFT).
- Displays **Close price** and a **5-day Simple Moving Average (SMA)** to identify short-term trends.
- Shows **Volume** (number of shares traded per day).
- Date range selection and ticker input.
- Responsive charts with **dark / light mode toggle**.
- Interactive visualization powered by **Chart.js**.

---

## Technologies
- **[Flask](https://flask.palletsprojects.com/)** – Python web framework  
- **[Requests](https://requests.readthedocs.io/)** – API communication  
- **[Chart.js](https://www.chartjs.org/)** – data visualization on the frontend  

---

## Data
The dashboard uses **financial EOD (End of Day) data** from **Marketstack**:
- **Close** – stock closing price of the day  
- **SMA(5)** – 5-day simple moving average of closing prices  
- **Volume** – number of shares traded per day (market activity)  

These indicators are widely used in **technical analysis** to identify market trends and validate the strength of price moves.

---

## API Key
You can obtain a free API key from [https://marketstack.com/](https://marketstack.com/).  
Simply register, and you will receive an `access_key` which is required for all requests.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-stock-dashboard.git
   cd flask-stock-dashboard
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Project structure
```
flask-stock-dashboard/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── templates/
│   ├── base.html       # base layout (dark/light theme)
│   └── index.html      # dashboard with charts
└── docs/
    └── screenshot.png  # app screenshot
```

---

## Possible extensions
- Add more indicators (SMA20, SMA50, EMA).
- Include candlestick charts (Plotly).
- Export stock data to CSV.
- Support multiple tickers at once.
- Deploy to **Heroku / Vercel**.

---

## License
MIT License – created for learning and demonstration purposes.
