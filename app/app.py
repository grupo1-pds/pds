from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def detect_fall_batch(frames):
    # Processa cada frame com o modelo de detecção de quedas
    results = []
    for _ in frames:
        # O nosso modelo vem aqui
        result = {"fall_detected": False, "confidence": 0.85}
        results.append(result)
    return results

@app.route('/detect_fall_batch', methods=['POST'])
def detect_fall_batch_endpoint():
    if 'webcam_id' not in request.form:
        return jsonify({"error": "No webcam_id provided"}), 400

    # Obtém a lista de frames
    files = request.files.getlist('frames')
    webcam_id = request.form['webcam_id']
    frame_list = []

    for file in files:
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        frame_list.append(img)

    # Processa a lista de frames com o modelo de detecção de quedas
    results = detect_fall_batch(frame_list)

    # Inclui o identificador da webcam no resultado
    response = {
        "webcam_id": webcam_id,
        "results": results
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
