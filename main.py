import cv2
import time

def main():

    cap = cv2.VideoCapture(0)
    img_num = 0

    while(True):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (900,795))
        frame = cv2.flip(frame, 1)
        cv2.imshow("frame", frame)
        name = "E:/Hand Motions/" + str(img_num) + ".png"
        cv2.imwrite(name, frame)
        img_num+=1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.3)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()