import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize Mediapipe Hand Detector
hand_detector = mp.solutions.hands.Hands(min_detection_confidence=0.75, max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

while True:
    # Capture frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a mirror view
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw hand landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                
                # Mark the index finger with a circle
                if id == 8:  # Index finger tip
                    cv2.circle(frame, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)

                # Mark the middle finger with a circle
                if id == 12:  # Middle finger tip
                    cv2.circle(frame, (x, y), 15, (0, 255, 255), cv2.FILLED)
    
    # Display the frame
    cv2.imshow("Virtual Mouse", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
