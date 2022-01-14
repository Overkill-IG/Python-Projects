import cv2

#face data to detect the faces
trainedface_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

feature = input("For Image Face Detection: Press 1\nFor Webcam Face Detection: Press 2\nFor in-Video Face Detection: Press 3 \n -->")
if feature == '1':
    a = input("Image name along with it's type: ")
    #Detecting faces in photos
    img = cv2.imread(a)
    #GrayScaling the Image
    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    #Detecting Faces
    Detect_Face = trainedface_data.detectMultiScale(grayscaled_img)
    
    mode = input("For Single Face: Press 1 || For All Faces: Press 2 \n --> ")
    
    if mode == '1':
        #Draw the Rectangle
        (x, y, w, h) = Detect_Face[1]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        #Show
        cv2.imshow("Image Face Detector", img)
        cv2.waitKey()
        
    elif mode == '2':
        for(x, y, w, h) in Detect_Face:
            cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 2 )
            #Show
            cv2.imshow("Image Face Detector", img)
            cv2.waitKey()
    
    else:
        print("Error!")
    
elif feature == '2':
    #Detecting Faces in Webcam
    webcam = cv2.VideoCapture(0)
    #Iterate forever for live capture
    while True:
        #Read the Current Frame
        successful_frame_read, frame = webcam.read()
        
        #GrayScaling the Image
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Detecting Faces
        Detect_Face = trainedface_data.detectMultiScale(grayscaled_img)
        
        #drawing Rectangle around the image
        for(x, y, w, h) in Detect_Face:
            cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 3 )
            
        cv2.imshow('Overkill Face Detector', frame)
        key = cv2.waitKey(1)
        
        #Exit
        if key == 27:
            break
    #Release the Video Object
    webcam.release()
    
elif feature == '3':
    #Detecting Faces in Video
    b = input("Enter the Video Name along with it's type: ")
    webcam = cv2.VideoCapture(b)
    #Iterate forever for live capture
    while True:
        #Read the Current Frame
        successful_frame_read, frame = webcam.read()
        
        #GrayScaling the Image
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Detecting Faces
        Detect_Face = trainedface_data.detectMultiScale(grayscaled_img)
        
        #drawing Rectangle around the image
        for(x, y, w, h) in Detect_Face:
            cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 3 )
            
        cv2.imshow('Overkill Face Detector', frame)
        key = cv2.waitKey(1)
        
        #Exit
        if key == 27:
            break
    #Release the Video Object
    webcam.release()
else:
    print("ERROR!")