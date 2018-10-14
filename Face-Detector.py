# FACE AND EYE DETECTION PROGRAM:
# USES OPEN CV AND HAAR-CASCADE-FRONTAL FACE AND EYES Classifier

# import open-cv use subprocess.call("pip install opencv-python") to install opencv
import cv2

# loading required classifiers
# Trained classifier to detect faces:

face_classify = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Trained classifier to detect eyes:

eyes_classify = cv2.CascadeClassifier('haarcascade_eye.xml')

# Capture video from camera

vid = cv2.VideoCapture(0)

cv2.namedWindow('Face-Detector')

# infinite loop
while(True):

    # returns ret - bool(camera availability) frame -
    ret,frame = vid.read()

    #Convert to gray - needed for cascade classifier.
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detects multiple sized and shaped faces arg1 = image arg2 =scaleFactor(resizes faces to fit to alg(1.05-1.3))
    #arg3 - min neighbour(less detections higher quality (3-6))
    multi_face = face_classify.detectMultiScale(gray,1.3,4)

    # For each face detected get these parameters as multiface returns x,y,w,h
    for (x,y,w,h) in multi_face:


        #Draw rectangle
        cv2.rectangle(frame,(x,y),(x+w , y+h),(0,0,0),5)


        #ROI - region of interest for eyes is the face
        #use split function to split x:x+w and y:y+w for both gray and color region.
        roi_gray = gray[x:x+h, y:y+h]
        roi_frame = frame[x:x+h ,y:y+h]

        #detect various shapes and sizes of eyes. args same as face.
        multi_eyes = eyes_classify.detectMultiScale(roi_gray, 1.3, 4)

        for (ex,ey,ew,eh) in multi_eyes:
            # Draw rectangle
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    cv2.imshow('Face-Detector',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


vid.release()

cv2.destroyAllWindows()
