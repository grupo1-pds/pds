import cv2
import requests
import numpy as np
import time

# Configurações
WEBCAM_ID = 'webcam_1'
API_URL = 'http://localhost:5000/detect_fall_batch'
CAPTURE_DURATION = 10

def captureFrames(cap, duration):
    frames = []
    startTime = time.time()
    while time.time() - startTime < duration:
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Não foi possível ler o frame da câmera")
        
        _, imgEncoded = cv2.imencode('.jpg', frame)
        frames.append(imgEncoded.tobytes())
        
        cv2.imshow("Imagem", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return [], True

    return frames, False

def sendFramesToAPI(frames, webcamId, url):
    files = [('frames', (f'frame_{i}.jpg', frame, 'image/jpeg')) for i, frame in enumerate(frames)]
    try:
        response = requests.post(url, files=files, data={'webcam_id': webcamId})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Erro ao enviar frames para a API: {e}")

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Não foi possível abrir a câmera")
        return

    try:
        while True:
            try:
                frames, quit = captureFrames(cap, CAPTURE_DURATION)
                if quit:
                    break
                result = sendFramesToAPI(frames, WEBCAM_ID, API_URL)
                print(result)
            except RuntimeError as e:
                print(e)
                break

            # Verifica se a tecla 'q' foi pressionada para sair
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
