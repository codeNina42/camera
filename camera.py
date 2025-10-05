import cv2

def open_camera():
    cam = cv2.VideoCapture(0)  # 0 = default webcam
    cv2.namedWindow("Camera")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Closing camera...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = f"photo_{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved!")
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

open_camera()
