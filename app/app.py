from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def detectFallBatch(frames):
    results = []
    for frame in frames:
        # Aqui entra o nosso modelo
        result = {"fall_detected": False, "confidence": 0.85}
        results.append(result)
    return results

def processFrames(files):
    frames = []
    for file in files:
        try:
            fileBytes = np.frombuffer(file.read(), np.uint8)
            img = cv2.imdecode(fileBytes, cv2.IMREAD_COLOR)
            frames.append(img)
        except Exception as e:
            raise ValueError(f"Erro ao processar frame: {e}")
    return frames

@app.route('/detect_fall_batch', methods=['POST'])
def detectFallBatchEndpoint():
    if 'webcam_id' not in request.form:
        return jsonify({"error": "No webcam_id provided"}), 400

    files = request.files.getlist('frames')
    if not files:
        return jsonify({"error": "No frames provided"}), 400

    try:
        frames = processFrames(files)
        results = detectFallBatch(frames)
        response = {"webcam_id": request.form['webcam_id'], "results": results}
        return jsonify(response)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
