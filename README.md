# Driver Drowsiness_
In this project we are detecting driver Drowsiness Using Open CV and Python.

<h3>libraries used:</h3>
<li>SciPy for Euclidean distance</li>
<li>imutils</li>
<li>numpy</li>
<li>playsound for playing Alarm</li>
<li>dlib</li>
<br><br>
My drowsiness detector hinged on two important computer vision techniques:

Facial landmark detection
Eye aspect ratio
Facial landmark prediction is the process of localizing key facial structures on a face, including the eyes, eyebrows, nose, mouth, and jawline.

Specifically, in the context of drowsiness detection, we only needed the eye regions 

Once we have our eye regions, we can apply the eye aspect ratio to determine if the eyes are closed. If the eyes have been closed for a sufficiently long enough period of time, we can assume the user is at risk of falling asleep and sound an alarm to grab their attention

The return value of the eye aspect ratio will be approximately constant when the eye is open. The value will then rapid decrease towards zero during a blink.


If the eye is closed, the eye aspect ratio will again remain approximately constant, but will be much smaller than the ratio when the eye is open.

<img src="https://github.com/parasjain929/DriverDrowsiness_MiniProject6sem/blob/master/eye.jpg"/>

# ALGORITHM

we make a check to see if the eye aspect ratio is below the “blink/closed” eye threshold, EYE_AR_THRESH .

If it is, we increment COUNTER , the total number of consecutive frames where the person has had their eyes closed.

If COUNTER exceeds EYE_AR_CONSEC_FRAMES  , then we assume the person is starting to doze off.

Another check is made, this time on to see if the alarm is on — if it’s not, we turn it on.

 handle playing the alarm sound, provided an --alarm  path was supplied when the script was executed. We take special care to create a separate thread responsible for calling sound_alarm  to ensure that our main program isn’t blocked until the sound finishes playing.

 draw the text DROWSINESS ALERT!  on our frame  — again, this is often helpful for debugging, especially if you are not using the playsound  library.

Finally,  handle the case where the eye aspect ratio is larger than EYE_AR_THRESH , indicating the eyes are open. If the eyes are open, we reset COUNTER  and ensure the alarm is off.
