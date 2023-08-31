import cv2

img = cv2.imread("Sistema_Solar.png")
cv2.putText(img,
            "o coisa boa",
            (100, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255, 255, 255)
            )

cv2.imshow("resultado", img)
cv2.waitKey(0)
