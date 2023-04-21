import cv2
#Go to the VS Code Settings -> Extensions -> Git. From there you can disable "Decorations".

#We read 2 images from the same cube, one brighter than the other (darker).
bright = cv2.imread('cube1.jpg')
dark = cv2.imread('cube8.jpg')

#We check the size of each just for fun
print(bright.shape[:2])
print(dark.shape[:3])

#We calculate the scale factor roughly and we scale it down
scale_factor = 0.82057 #343/418 px
scaled_bright = cv2.resize(bright, None, fx= scale_factor, fy= scale_factor, interpolation= cv2.INTER_LINEAR)

#We convert from BGR to LAB and create both variables.
brightLAB = cv2.cvtColor(scaled_bright,cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark,cv2.COLOR_BGR2LAB)
# for (name,chan) in zip(("B","G","R"),cv2.split(darkLAB)):
#     cv2.imshow(name,chan)

#WE convert from BGR to YCrCb
brightYCB = cv2.cvtColor(scaled_bright,cv2.COLOR_BGR2YCR_CB)
darkYCB = cv2.cvtColor(dark,cv2.COLOR_BGR2YCR_CB)

#WE convert to HSV color space
brightHSV = cv2.cvtColor(scaled_bright,cv2.COLOR_BGR2HSV)
darkHSV = cv2.cvtColor(dark,cv2.COLOR_BGR2HSV)

#We print the images respectively
cv2.imshow('Bright BGR (Default)', scaled_bright)
cv2.imshow('Dark BGR (Default)', dark)
cv2.imshow('Bright LAB', brightLAB)
cv2.imshow('Dark LAB', darkLAB)
cv2.imshow('Bright YCB', brightYCB)
cv2.imshow('Dark YCB', darkYCB)
cv2.imshow('Bright HSV', brightHSV)
cv2.imshow('Dark HSV', darkHSV)

#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()