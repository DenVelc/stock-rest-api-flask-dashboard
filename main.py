from flask import Flask, render_template, request, jsonify
import requests, os, datetime as dt

app = Flask(__name__)

API_KEY = os.getenv("MARKETSTACK_KEY", "YOUR API KEY HERE")

def fetch_eod(symbol, date_from, date_to):
    if not API_KEY:
        raise RuntimeError("Missing API key on server.")
    url = "http://api.marketstack.com/v1/eod"  # free tier = http
    params = {
        "access_key": API_KEY,
        "symbols": symbol,
        "date_from": date_from,
        "date_to": date_to,
        "limit": 1000
    }
    r = requests.get(url, params=params, timeout=20)
    print("DEBUG URL:", r.url, "STATUS:", r.status_code)
    j = r.json()
    if "error" in j:
        raise RuntimeError(j["error"].get("message", str(j["error"])))
    data = j.get("data", [])
    data.sort(key=lambda x: x.get("date",""))
    return data

@app.route("/")
def index():
    today = dt.date.today()
    start = today - dt.timedelta(days=30)
    return render_template("index.html",
        symbol=request.args.get("symbol", "AAPL").upper(),
        date_from=request.args.get("date_from", start.isoformat()),
        date_to=request.args.get("date_to", today.isoformat())
    )

@app.route("/api/eod")
def api_eod():
    symbol = request.args.get("symbol", "AAPL").upper()
    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")
    try:
        data = fetch_eod(symbol, date_from, date_to)
        labels = [d["date"][:10] for d in data]
        close  = [d.get("close") for d in data]
        volume = [d.get("volume") for d in data]
        # SMA5
        def sma(v, w=5):
            out, s, q = [], 0.0, []
            for x in v:
                q.append(x); s += x
                if len(q) > w: s -= q.pop(0)
                out.append(s/len(q))
            return out
        return jsonify({
            "labels": labels, "close": close, "volume": volume,
            "sma5": sma(close, 5) if close else [], "count": len(labels), "symbol": symbol
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
