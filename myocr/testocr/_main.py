from Module_1 import voice as vc
import cv2
import sys


def startvideo(mode):
    # Load Camera
    count = 0
    #mode=3
    cap = cv2.VideoCapture(0)
    counter = 0
    while True:
        if (counter % 5 != 0):
            continue
        ret, frame = cap.read()
        nm = "frame"+".jpg"
        cv2.imwrite(nm, frame)
        count += 1
        # if (mode == 1):
        #     from Module_3 import Image_Captioning
        #     print("Live CAptioning")
        #     print(Image_Captioning.caption_this_image(nm))
        #     vc.voice(Image_Captioning.caption_this_image(nm))
        #     print("Dombo")
        # elif (mode == 3):
        from Module_2 import OCR
        OCR.ocr(nm)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 49:
            mode = 1
        elif key == 50:
            mode = 2
        elif key == 51:
            mode = 3
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

startvideo(3)