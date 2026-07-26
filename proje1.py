import cv2
import numpy as np

pic = cv2.imread("C:/Users/Sena/OneDrive/Desktop/goruntu_isleme/assets/img1.jpg")

if pic is None:
    print("Görsel okunamadı.")
else:
    print("Görsel okundu.")

pic = cv2.resize(pic, (400, 400))
original_pic = pic.copy() 
gray_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)  

mod = "renkli"

while True:
    cv2.imshow("goruntu", pic)
    tus = cv2.waitKey(0)

    if tus == ord('w'):
        mod = "renkli"
        pic = original_pic.copy()
        cv2.imshow("goruntu", pic)

    elif tus == ord('e'):
        mod = "gri"
        gray_pic = cv2.cvtColor(
            original_pic if mod == "renkli" else pic, cv2.COLOR_BGR2GRAY
        )
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        cv2.imshow("goruntu", pic)

    elif tus == ord('r'):
        pic = cv2.rotate(pic, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("goruntu", pic)

    elif tus == ord('t'):
        pic = cv2.rotate(pic, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("goruntu", pic)

    elif tus == ord('y'):
        pic = cv2.flip(pic, 1)
        cv2.imshow("goruntu", pic)

    elif tus == ord('d'):
        pic = cv2.flip(pic, 0)
        cv2.imshow("goruntu", pic)

    elif tus == ord('n'):
        pic = cv2.bitwise_not(pic)
        cv2.imshow("goruntu", pic)

    elif tus == ord('+'):
        pic = cv2.convertScaleAbs(pic, alpha=1.2, beta=20) 
        cv2.imshow("goruntu", pic)

    elif tus == ord('-'):
        pic = cv2.convertScaleAbs(pic, alpha=0.8, beta=-20) 
        cv2.imshow("goruntu", pic)

    elif tus == ord('b'):
        pic = cv2.GaussianBlur(pic, (15, 15), 0)
        cv2.imshow("goruntu", pic)

    elif tus == ord('1'):
       pic = cv2.resize(pic, (0, 0), fx=0.8, fy=0.8) 
       cv2.imshow("goruntu", pic)

    elif tus == ord('2'):
       pic = cv2.resize(pic, (0, 0), fx=1.2, fy=1.2) 
       cv2.imshow("goruntu", pic)

    elif tus == ord('s'):
        cv2.imwrite("C:/Users/Sena/OneDrive/Desktop/goruntu_isleme/assets/kaydedilen.jpg", pic)
        print("Görsel başarıyla kaydedildi!")

    elif tus == ord('q'):
        cv2.destroyAllWindows()
        break