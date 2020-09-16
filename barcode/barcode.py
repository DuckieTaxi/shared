import cv2
import numpy as np
import apriltag


def GetImage():
    camera = cv2.VideoCapture(0)
    ret, image = camera.read()
    return image


def ViewImage(image, name_of_window):
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def BarcodeDetector(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = apriltag.Detector(apriltag.DetectorOptions('tag36h11'))

    result = detector.detect(image)

    if result == []:
        return None
    else:
        return result[0][5]


def Cropping(image, y, high, x, width):
    image = image[y:high, x:width]
    return image
"""
image = cv2.imread('/mnt/c/Users/gia/PycharmProjects/CleverTaxi/project/duckietown_barcode.png')
image = Cropping(image, 0, 460, 0, 460)
cv2.imwrite('image.jpg', image)
#ViewImage(image, 'image')

img = cv2.imread('/mnt/c/Users/gia/PycharmProjects/CleverTaxi/car.jpg')
#ViewImage(img, 'image')
cv2.imwrite('img.jpg', img)
res = BarcodeDetector('img.jpg')
print(res)
result = BarcodeDetector('image.jpg')
print(result)
"""