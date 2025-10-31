# app.py
from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

def calculate_bmi_value(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if height <= 0 or weight <= 0:
            return None
        bmi = weight / (height * height)
        bmi = round(bmi, 2)
        return bmi
    except Exception:
        return None

def bmi_category(bmi):
    if bmi is None:
        return "Invalid"
    if bmi < 18.5:
        return "Underweight"
    if bmi < 24.9:
        return "Normal weight"
    if bmi < 29.9:
        return "Overweight"
    return "Obese"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    weight = request.form.get("weight")
    height = request.form.get("height")
    bmi = calculate_bmi_value(weight, height)
    category = bmi_category(bmi)
    # re-render page with result displayed via template variables
    return render_template("index.html", bmi=bmi, category=category)

# JSON API for automation / Jenkins
@app.route("/api/bmi", methods=["POST"])
def api_bmi():
    """
    Accepts JSON: { "weight": 70, "height": 1.75 }
    Returns JSON: { "bmi": 22.86, "category": "Normal weight" }
    """
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    weight = data.get("weight")
    height = data.get("height")
    bmi = calculate_bmi_value(weight, height)
    if bmi is None:
        return jsonify({"error": "Invalid weight/height"}), 400

    return jsonify({"bmi": bmi, "category": bmi_category(bmi)}), 200

if __name__ == "__main__":
    # For development only. In production use gunicorn or similar.
    app.run(host="0.0.0.0", port=5000, debug=True)
