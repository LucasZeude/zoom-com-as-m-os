import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializar a captura de vídeo da câmera
cap = cv2.VideoCapture(0)

# Inicializar o detector de mãos
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        # Ler um frame da câmera
        success, image = cap.read()
        if not success:
            print("Failed to read from camera.")
            break

        # Converter a imagem para tons de cinza para melhorar o desempenho do detector
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Executar a detecção de mãos no frame atual
        results = hands.process(image)

        # Verificar se pelo menos uma mão foi detectada
        if results.multi_hand_landmarks:
            # Obter as coordenadas dos pontos de referência das mãos (pontos de articulação dos dedos)
            landmarks = results.multi_hand_landmarks[0].landmark
            
            # Obter as coordenadas do polegar e do indicador
            thumb_x, thumb_y = landmarks[mp_hands.HandLandmark.THUMB_TIP].x, landmarks[mp_hands.HandLandmark.THUMB_TIP].y
            index_x, index_y = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            
            # Calcular a distância entre o polegar e o indicador
            distance = math.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)

            # Definir a proporção de zoom com base na distância entre os dedos
            zoom_ratio = 1 - distance

            # Aplicar o zoom na imagem
            resized_image = cv2.resize(image, None, fx=zoom_ratio, fy=zoom_ratio)

            # Exibir a imagem resultante na tela
            cv2.imshow('Zoomed Image', resized_image)

        # Esperar por uma tecla ser pressionada
        if cv2.waitKey(1) == ord('q'):
            break

# Liberar a captura de vídeo e fechar todas as janelas abertas
cap.release()
cv2.destroyAllWindows()

