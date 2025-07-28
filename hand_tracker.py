import cv2
import mediapipe as mp
import pyautogui

screen_width, screen_height = pyautogui.size()
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1)
draw_utils = mp.solutions.drawing_utils

def get_hand_landmarks(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed = hands.process(frame_rgb)
    landmark_list = []
    if processed.multi_hand_landmarks:
        for lm in processed.multi_hand_landmarks[0].landmark:
            landmark_list.append((lm.x, lm.y))
    return landmark_list, processed

def draw_landmarks(frame, processed):
    if processed.multi_hand_landmarks:
        draw_utils.draw_landmarks(frame, processed.multi_hand_landmarks[0], mpHands.HAND_CONNECTIONS)

def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        index_finger_tip = processed.multi_hand_landmarks[0].landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
        return index_finger_tip
    return None

def move_mouse(index_finger_tip):
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width)
        y = int(index_finger_tip.y / 2 * screen_height)
        pyautogui.moveTo(x, y)
