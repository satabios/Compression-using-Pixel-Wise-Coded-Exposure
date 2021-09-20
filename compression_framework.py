import cv2
import numpy as np
from genBump import genBump
import time
import glob
#from __future__ import divison



def read_buffer_compression(compression_ratio,bump_time,segregated,folder,extension,save_dir):
    N,H =0,0
    data_file = 0
    compressed_data = []
   
    if(segregated):
        buffer = []
        cnt = 0
        for img in range(sorted(glob.iglob(folder+"*"+extension))):
            if(cnt == compression_ratio-1):

                sensing_matrix = genBump(bump_time,N,H,compression_ratio)
                image_list = np.asarray(bump_time)
                compressed_image = np.multiply(sensing_matrix, image_list)
                compressed_image = np.sum(compressed_image, 0)/compression_ratio.
                np.savez(compressed_data)
                compressed_data.append(save_dir+str(data_file)+".npz",compressed_data=compressed_image)
                data_file+=1
                buffer = []
                cnt = 0      

            else:
                image  = cv2.imread(img,0)
                N, H  = image.shape
                buffer.append(image) # remove zero if RGB 
                cnt+=1
        
    


def real_time_compression_tx2():

    sens = genBump(3, 608, 608, 20)
    cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)608, height=(int)608,format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    if cap.isOpened():
        windowName = "Temporal Compression"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName,1280,720)
        cv2.moveWindow(windowName,0,0)
        cv2.setWindowTitle(windowName,"Temporal Compression")

        counter = 0
        images = []
        ret_val,frame=cap.read()
        displayBuf = frame
        while True:
            start = time.time()
            ret_val, frame = cap.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("./"+str(counter)+".png",gray_frame)
            images.append(gray_frame)
            counter = counter + 1
            if(counter==20):
                image_list = np.asarray(images)
                compressed_image = np.multiply(sens, image_list)
                compressed_image = np.sum(compressed_image, 0)/3.
    
                counter = 0
                displayBuf = compressed_image
                images=[]
                cv2.imshow(windowName,displayBuf)
                end = time.time()
                print(str(end-start))
        
                key=cv2.waitKey(10)
            if key == 27: # Check for ESC key
                cv2.destroyAllWindows()
                break ;
    else:
    
        print ("camera opening failed!")



if __name__ == '__main__':
    #read_cam()
    read_buffer_compression(compression_ratio,bump_time,segregated,folder,extension,save_dir)