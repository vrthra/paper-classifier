import os
import csv
from flask import Flask, render_template, send_from_directory, jsonify, request

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

PDF_DIR = os.environ.get("PDF_DIR", os.path.join(os.path.dirname(__file__), "pdfs"))
CSV_FILE = os.path.join(os.path.dirname(__file__), "classifications.csv")


def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["pdf_name", "deeper", "smarter", "swifter", "seeds"])


def load_csv():
    ensure_csv()
    data = {}
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["pdf_name"]] = {
                "deeper": row["deeper"] == "True",
                "smarter": row["smarter"] == "True",
                "swifter": row["swifter"] == "True",
                "seeds": row["seeds"] == "True",
            }
    return data


def save_csv(data):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["pdf_name", "deeper", "smarter", "swifter", "seeds"])
        for pdf_name, checks in sorted(data.items()):
            writer.writerow([pdf_name, checks["deeper"], checks["smarter"], checks["swifter"], checks["seeds"]])


@app.route("/")
def index():
    pdfs = sorted([f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")])
    return render_template("index.html", pdfs=pdfs)


@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)


@app.route("/api/classifications", methods=["GET"])
def get_classifications():
    return jsonify(load_csv())


@app.route("/api/classify", methods=["POST"])
def classify():
    body = request.json
    pdf_name = body["pdf_name"]
    data = load_csv()
    data[pdf_name] = {
        "deeper": body.get("deeper", False),
        "smarter": body.get("smarter", False),
        "swifter": body.get("swifter", False),
        "seeds": body.get("seeds", False),
    }
    save_csv(data)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    os.makedirs(PDF_DIR, exist_ok=True)
    ensure_csv()
    app.run(debug=True, port=5000)
