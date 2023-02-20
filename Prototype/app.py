from flask import Flask, render_template, request
import random
import serial

app = Flask(__name__)
# arduino = serial.Serial('COM3', 9600)  # replace 'COM3' with the correct port for your Arduino

@app.route('/', methods=['GET', 'POST'])
def select_hour():
    selected_hour = None
    if request.method == 'POST':
        start_hour = int(request.form['start_hour'])
        end_hour = int(request.form['end_hour'])
        duration = int(request.form['duration'])
        if start_hour >= end_hour:
            error_message = 'Invalid input: start hour must be before end hour.'
        elif duration > (end_hour - start_hour):
            error_message = 'Invalid input: the duration is too long for the selected range.'
        else:
            selected_hour = random.randint(start_hour, end_hour - duration)
            # arduino.write(f'"starttime":{start_hour}'.encode())  # send start time to Arduino
            return render_template('index.html', selected_hour=selected_hour)

    return render_template('index.html', selected_hour=selected_hour)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
