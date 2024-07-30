import cv2
import requests
import numpy as np

# Identificador único da webcam
deviceId = '1'

# URL da API
url = 'http://localhost:5000/detect_fall'

cap = cv2.VideoCapture("rtsp://192.168.0.46:8080/h264_ulaw.sdp")#Essa parte pode mudar se quiser testar com algo , estou pensando em comprar uma camera barat(20 conto) pra testar

if not cap.isOpened():
    print("Não abriu")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não tem frame")
        break

    # Codifica a imagem em JPEG
    _, img_encoded = cv2.imencode('.jpg', frame)
    

    # Converte a imagem para bytes
    img_bytes = img_encoded.tobytes()

    # Envia a imagem para a API com o identificador do dispositivo
    response = requests.post(url, files={'image': img_bytes}, data={'deviceId': deviceId})

    # Verifica a resposta da API
    if response.ok:
        print(response.json())
    else:
        print('Falha ao enviar a imagem para a API')

    cv2.imshow("Imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
