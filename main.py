import cv2
import numpy as np


class HOG:


    def cropAndResizeImage(self):                           # Etape 1: coupure et redimensionnement

        img = cv2.imread('/home/djawed/Images/1.jpg')
        img_cropped=img[100:200, 100:200]
        ImgResized=cv2.resize(img_cropped,(64,128))
        cv2.imwrite('/home/djawed/PycharmProjects/Resized/1.jpg', ImgResized)
        print("Étape une éffectuée avec succés")



    def GradientCalculating(self):          # etape 2: calcule du gradient la magnitude de l'image
        # Read image
        im = cv2.imread('/home/djawed/PycharmProjects/Resized/1.jpg')
        im = np.float32(im) / 255.0

        # Calculate gradient
        gx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=1)
        gy = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=1)

        #magnitude & direction of gradient
        mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
        print("Étape 2 effectué avec succés")

if __name__ == '__main__':
    test= HOG()
    test.cropAndResizeImage()
    test.GradientCalculating()
