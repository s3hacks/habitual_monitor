import cv2
import numpy as np
from skimage.measure import compare_ssim
from pygame import mixer
mixer.init()
mixer.music.load("mysong.mp3")
images_positive=[]
testimages=[]
def test(trainimages,image):
    maximum=0.0
    for i in trainimages:
        error=np.sum(i*image)**2
        if(error>maximum):
            maximum=error
    return maximum

def get_images():
    '''
    input : nothing
    functionality : uses webcamera to record video, converts to gray scale
                    appends to the list of images
    output : return the frames of the object as a numpy array
    '''

    capture = cv2.VideoCapture(0)
    global images_positive

    while (capture.isOpened()):
        result, image = capture.read()

        if result == True:
            cv2.imshow('Frame', image)
            image=cv2.resize(image,(100,100))
            #r,g,b=cv2.split(image)
            #image=cv2.merge((r,g,b,mask.astype("float32")/255.0))
            image=np.asarray(image, dtype="float32")
            image=image/np.sqrt(np.sum(image**2))
            images.append(image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break



    capture.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    return images
def get_imagestest():
    '''
    input : nothing
    functionality : uses webcamera to record video, converts to gray scale
                    appends to the list of images
    output : return the frames of the object as a numpy array
    '''
    global testimages
    global testimagesg
    capture = cv2.VideoCapture(0)

    while (capture.isOpened()):
        result, image = capture.read()

        if result == True:
            cv2.imshow('Frame', image)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #r,g,b=cv2.split(image)
            #image=cv2.merge((r,g,b,mask.astype("float32")/255.0))
            image=cv2.resize(image,(100,100))
            image=np.asarray(image, dtype="float32")

            image=image/np.sqrt(np.sum(image**2))
            testimages.append(image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            if (len(testimages)%10==0):
                val=test(images_positive[int(len(images_positive)/2):int(len(images_positive)/2)+20],testimages[-1])
                #print(test2(images_positiveg[int(len(images_positiveg)/2):int(len(images_positiveg)/2)+20],testimagesg[-1]))
                if(val>.95):
                    mixer.music.play()


    capture.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
array=[]
def choose_images():
    global images_positive
    global images_positiveg
    while(1):
        choice = input ("Enter 'h' to train habit : \n Enter 't' to train normal scenerio : \n 'q' to quit")
        if choice == "h":
            images_positive= get_images()
            a=int(len(images_positive)/2)
            print(test(images_positive[a:a+10],images_positive[a:a+10]))
            print("Recorded Frames of positive :")
        if choice == "t":
            print("Recorded Frames of negative :")
            get_imagestest()
        if choice == "q":
            print("Quitting")
            break


if __name__ == "__main__":
    choose_images()




