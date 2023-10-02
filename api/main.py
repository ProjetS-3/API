from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Remplacer par db
reservations = {

}


@app.route('/reservation', methods=["POST"])
def create_reservation():
    data = request.get_json()
    product_id = data['product_id']

    reservation_id = str(uuid.uuid4())[:8]

    reservations[reservation_id] = data

    print(reservations)

    return jsonify({'reservation_id': reservation_id}), 201

@app.route('/distribution/<string:reservation_id>')
def check_reservation(reservation_id):
    if reservation_id in reservations:
        return jsonify({'message': 'Reservation valide'}), 200
    else:
        return jsonify({'message': 'Reservation non valide'}), 404


if __name__ == '__main__':
    app.run(debug=True)
