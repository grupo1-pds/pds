import cv2
import requests
import numpy as np
import time

# Id webcam
webcam_id = 'webcam_1'

# URL da API
url = 'http://localhost:5000/detect_fall_batch'

# Tempo de captura pra enviar pra API
capture_duration = 10

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Não abriu")
    exit()

while True:
    frames = []
    start_time = time.time()
    while time.time() - start_time < capture_duration:
        ret, frame = cap.read()
        if not ret:
            print("Não tem frame")
            break
        
        _, img_encoded = cv2.imencode('.jpg', frame)
        
        frames.append(img_encoded.tobytes())

        cv2.imshow("Imagem", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    files = [('frames', (f'frame_{i}.jpg', frames[i], 'image/jpeg')) for i in range(len(frames))]

    # Envia a lista de frames para a API com o id da webcam
    response = requests.post(url, files=files, data={'webcam_id': webcam_id})

    if response.ok:
        print(response.json())
    else:
        print('Falha ao enviar a batch de frames para a API: ', response.text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
