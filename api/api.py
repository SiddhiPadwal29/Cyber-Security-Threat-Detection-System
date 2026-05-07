from flask import jsonify

def security_api():
    return jsonify({
        "threats": 5,
        "status": "Active"
    })
