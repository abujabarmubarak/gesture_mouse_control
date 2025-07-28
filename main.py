from hand_tracker import get_hand_landmarks, draw_landmarks
from gesture_control import detect_gesture
import cv2
import mediapipe as mp

def main():
    cap = cv2.VideoCapture(0)
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            landmark_list, processed = get_hand_landmarks(frame)

            if processed:
                draw_landmarks(frame, processed)

            detect_gesture(frame, landmark_list, processed)

            cv2.imshow('Gesture Mouse Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
