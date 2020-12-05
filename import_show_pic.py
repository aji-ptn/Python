import cv2
pic=cv2.imread("Re")
img = cv2.imread("C:\\Users\\Aji Pamungkas\\PycharmProjects\\pythonProject1\\Resources/small_pic.jpg",0)
print(img.shape)
cv2.imshow("output", img)
cv2.waitKey()
cv2.destroyAllWindows()
