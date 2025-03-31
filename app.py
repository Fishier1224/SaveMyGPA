from flask import Flask, request, render_template
from gpacalc import calculate_gpa_scenarios

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        df = calculate_gpa_scenarios(
            current_gpa=data["current_gpa"],
            current_units=data["current_units"],
            desired_gpa=data["desired_gpa"],
            max_future_units=data["max_future_units"],
            college_A=data["college_A"],
            college_A_minus=data["college_A_minus"]
        )

        return df.to_html(index=False)
    except Exception as e:
        return str(e), 500
