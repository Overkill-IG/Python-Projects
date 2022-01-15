import cv2

def detect_smile():
    import cv2

    #Face Classifier
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

    #Webcam
    webcam = cv2.VideoCapture(0)
    while True: 
        successful_frame_read, frame = webcam.read()
        if not successful_frame_read:
            break
        #Change to Grayscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Detecting Faces and Coordinates
        faces = face_detector.detectMultiScale(grayscale)
        
        #Drawing Rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            #Getting the SubFrame using numpy list slicing
            the_face = frame[y : y + h, x : x + w ]
            
            grayscale_the_face = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
            
            smiles = smile_detector.detectMultiScale(grayscale_the_face, scaleFactor = 1.7, minNeighbors = 20)
            
                #To draw the rectangle around the smile
                # for (x_, y_, w_, h_) in smiles:
                #     cv2.rectangle(the_face, (x_, y), (x_ + w_, y_ + h_), (50, 50, 200), 2)
                
            if len(smiles) > 0:
                cv2.putText(frame, 'Smiling', ( x, y + h + 40), fontScale = 1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, color = (255, 255, 255) )
        
        #Displaying the Webcam
        cv2.imshow('Smile Detector', frame)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

    #Cleanup code
    webcam.release()
    cv2.destroyAllWindows()

    print("code completed")

#face data to detect the faces
trainedface_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

feature = input("For Image Face Detection: Press 1\nFor Webcam Face Detection: Press 2\nFor in-Video Face Detection: Press 3 \nFor Smile Detection: Press 4\n -->")
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
elif feature == '4':
    detect_smile()
else:
    print("ERROR!")