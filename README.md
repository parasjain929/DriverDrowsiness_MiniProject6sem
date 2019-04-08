# Driver Drowsiness_
Drowsiness detection Using Open CV and Python.

libraries used:
SciPy for Euclidean distance
imutils
numpy
playsound for playing Alarm
dlib

Our drowsiness detector hinged on two important computer vision techniques:

Facial landmark detection
Eye aspect ratio
Facial landmark prediction is the process of localizing key facial structures on a face, including the eyes, eyebrows, nose, mouth, and jawline.

Specifically, in the context of drowsiness detection, we only needed the eye regions 

Once we have our eye regions, we can apply the eye aspect ratio to determine if the eyes are closed. If the eyes have been closed for a sufficiently long enough period of time, we can assume the user is at risk of falling asleep and sound an alarm to grab their attention

The return value of the eye aspect ratio will be approximately constant when the eye is open. The value will then rapid decrease towards zero during a blink.


If the eye is closed, the eye aspect ratio will again remain approximately constant, but will be much smaller than the ratio when the eye is open.

<img src="https://github.com/parasjain929/DriverDrowsiness_MiniProject6sem/blob/master/eye.jpg"/>
