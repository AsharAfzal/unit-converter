from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        length = float(request.form['length'])
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']
        
        # Conversion factors
        conversion_factors = {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34,
            'feet': 0.3048,
            'inches': 0.0254
        }
        
        if unit_from not in conversion_factors or unit_to not in conversion_factors:
            return jsonify({'error': 'Invalid unit'}), 400
        
        # Convert from input unit to meters first, then to target unit
        meters = length * conversion_factors[unit_from]
        result = meters / conversion_factors[unit_to]

        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
