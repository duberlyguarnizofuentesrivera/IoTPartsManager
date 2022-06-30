from flask import Flask, render_template, request, url_for, redirect

from iotmanager import IoTManager
from part import Part
from position import Position
from stand import Stand

app = Flask(__name__)
iotmanager = IoTManager()


# By Duberly Guarnizo. This application requires Flask installed to run!!!

@app.route('/')
def index():
    # IMPORTANT: this is where we implement persistence: we are saving the state of the iotmanager
    # into a JSON file. This is a state serialization technique. By Duberly Guarnizo.
    return render_template('index.html', parts=iotmanager.get_parts())


@app.route('/add_part', methods=['POST'])
def add_part():
    part_id = len(iotmanager.parts) + 1
    name = request.form['part_name']
    category = request.form['part_category']
    stock = request.form['part_stock']
    row = request.form['part_row']
    col = request.form['part_col']
    stand_name = request.form['part_stand']

    position = Position(row, col, Stand(stand_name))
    part = Part(part_id, name, category, stock, position)
    iotmanager.add_part(part)
    iotmanager.json_save('iotmanager.json')
    return redirect(url_for('index'))


@app.route("/remove_part/<int:part_id>")
def remove_part(part_id):
    part = iotmanager.get_part(part_id)
    print("part is: " + str(part))
    iotmanager.remove_part(part)
    iotmanager.json_save('iotmanager.json')
    return redirect(url_for('index'))


@app.route("/load_demo")
def load_demo_data():
    stand1 = Stand('Upper Stand')
    stand2 = Stand('Green Container')
    iotmanager.add_part(Part(1, 'Arduino', 'MCU', 1, Position(1, 1, stand1)))
    iotmanager.add_part(Part(2, 'ESP32', 'MCU', 1, Position(1, 2, stand1)))
    iotmanager.add_part(Part(3, 'Humidity Sensor', 'Sensors', 3, Position(1, 1, stand2)))
    iotmanager.add_part(Part(4, 'Rain Sensor', 'Sensor', 1, Position(1, 2, stand2)))
    iotmanager.add_part(Part(5, 'Yellow led', 'Lights', 2, Position(2, 1, stand2)))
    iotmanager.json_save('iotmanager.json')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
