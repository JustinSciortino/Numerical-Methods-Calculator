from flask import Flask, render_template, request, jsonify, url_for
import lessons

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    lesson = data.get('lesson')
    sub_calculator = data.get('sub_calculator')

    if lesson == 'lesson1' and sub_calculator == 'bisection':
        function = data.get('function')
        a = data.get('a')
        b = data.get('b')
        tolerance = data.get('tolerance')
        max_iterations = data.get('max_iterations')

        # Call the Bisection function with the provided arguments
        #result = bisection_function(function, a, b, tolerance, max_iterations)

        return jsonify({'result': result})

    # Handle other lessons and calculators as needed
    return jsonify({'result': 'Invalid request'})
def perform_numerical_calculation(lesson, sub_calculator):
    # Implement your numerical methods logic here
    # Use the lesson and sub_calculator parameters to determine the specific calculation to perform
    # Replace this with your actual numerical methods logic
    result = 42.0  # Placeholder result
    return result

if __name__ == '__main__':
    app.run(debug=True)
