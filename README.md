# Driver Drowsiness_
Drowsiness detection Using Open CV and Python.

libraries used:
SciPy for Euclidean distance
imutils
numpy
playsound for playing Alarm
dlib

The return value of the eye aspect ratio will be approximately constant when the eye is open. The value will then rapid decrease towards zero during a blink.

If the eye is closed, the eye aspect ratio will again remain approximately constant, but will be much smaller than the ratio when the eye is open.

To visualize this, consider the following figure from Soukupová and Čech’s 2016 paper
![Screenshot 1]\(eye.jpg)
