from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def detect_fall(image):
    # Serviço de detecção de queda
    return {"fall_detected": False, "confidence": 0.85}

@app.route('/detect_fall', methods=['POST'])
def detect_fall_endpoint():
    if 'image' not in request.files or 'deviceId' not in request.form:
        return jsonify({"error": "No image or deviceId provided"}), 400

    file = request.files['image']
    deviceId = request.form['deviceId']
    file_bytes = np.fromstring(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    result = detect_fall(img)

    result['deviceId'] = deviceId

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
