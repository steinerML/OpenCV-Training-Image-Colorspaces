# OpenCV-Training-Image-Colorspaces

Image colorspaces using OpenCV.
## Contents :
I have used the following functions/methods:

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.resize()     |We resize an image given a specific scale factor both on X and Y axis         |
|cv2.cvtColor()   |We convert color by specifying destination colorspace                         |

## Test Image used: 
I have used sample.jpg that can be found in the repository.

![Source Image Sequence](sample.jpg)
![Source Image Sequence](https://learnopencv.com/wp-content/uploads/2017/05/components-bgr.png)
## Summary:

```python
#We draw a line
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
```
```python
#Implement the circle() function
cv2.circle(imageCircle, circle_center, radius, color = (255,255,0) ,thickness=2,lineType=cv2.LINE_AA)
```
```python
# Draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8)
```
```python
#Ellipse Horizontal with Antialiasing
cv2.ellipse(imageEllipse, center, axis1, 0, 0, 360, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
```
```python
#Insert Text Horizontal with Antialiasing
cv2.putText(imageText, text, origin, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color = (255,255,0), thickness=0, lineType=cv2.LINE_AA)
```

