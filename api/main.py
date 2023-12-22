import uuid
from flask import Flask, request, jsonify
import sqlite
import qrcode

app = Flask(__name__)

api_keys = {
    "1e5ff036": "tmesse"
}


@app.route('/reservation', methods=["POST"])
def create_reservation():
    api_key = request.headers.get("X-API-Key")

    if api_key not in api_keys:
        return jsonify({'error': 'Clé API non valide.'}), 401

    data = request.get_json()
    reservation_id = str(uuid.uuid4())[:8]

    sqlite.create(reservation_id, data["product_id"], data["quantity"])
    print(sqlite.get_all())

    qr = qrcode.make(reservation_id)
    qr.save('qrcode.png')

    return jsonify({'reservation_id': reservation_id}), 201


@app.route('/distribution/<string:reservation_id>')
def check_reservation(reservation_id):
    api_key = request.headers.get("X-API-Key")

    if api_key not in api_keys:
        return jsonify({'error': 'Clé API non valide.'}), 401

    if sqlite.get_from_id(reservation_id):
        return jsonify({'exists': True, 'product_id': sqlite.get_from_id(reservation_id)[1],
                        'quantity': sqlite.get_from_id(reservation_id)[2]}), 200
    else:
        return jsonify({'exists': False}), 404


if __name__ == '__main__':
    app.run(debug=True)
