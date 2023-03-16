import cv2
import mediapipe as mp
import pyautogui

# Inicializa o detector de mãos do MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Define a escala de zoom
zoom_scale = 1.0

# Loop principal
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # Lê um frame da câmera
        success, image = cap.read()
        if not success:
            break

        # Converte a imagem para RGB e a processa com o detector de mãos
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Desenha os pontos das mãos na imagem
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Calcula a distância entre os dedos indicador e polegar
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

                # Atualiza a escala de zoom com base na distância entre os dedos
                zoom_scale += (distance - 0.1) / 500
                zoom_scale = max(0.0, min(zoom_scale, 2.0))

                # Aplica o zoom na tela
                resized_image = cv2.resize(image, None, fx=zoom_scale, fy=zoom_scale)

            # Exibir a imagem resultante na tela
            cv2.imshow('Zoomed Image', resized_image)

        # Sai do loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()