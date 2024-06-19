import cv2
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
cap = cv2.VideoCapture("cars.mp4")
while 1:
    # reads frames from a camera
    ret, img = cap.read()
    # convert to gray scale of each frames as it is better platform
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in cars:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()