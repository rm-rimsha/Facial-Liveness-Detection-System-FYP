"""
Created on 19.10.8 16:35
@File:generate_frames_and_bbox.py
@author: coderwangson
"""
"#codeing=utf-8"

'''
-------------------------------------------------------------------------------------------------------------------
-------------------------------------------- CODE FOR VIDEO PROCESSING --------------------------------------------
-------------------------------------------------------------------------------------------------------------------
'''

# TODO using pip install
from mtcnn.mtcnn import MTCNN
import cv2
import os
from glob import glob
import pandas as pd
from natsort import natsorted

detector = MTCNN()

def generate_frames_and_bbox(db_dir,save_dir,skip_num):

    

    file_list = open(save_dir+"/file_list.txt","a")
    #df = pd.read_csv('%s/liveness_train/train/label.csv' %db_dir)

    list_of_files = glob('%s/*.MOV'%db_dir)
    #print(list_of_files)
    #open("../../dataset/video_list(4).txt","a")
    #list_of_files = natsorted(list_of_files)

    for file in list_of_files:

        temp = os.path.normpath(file)
        print("Processing video %s"%temp)

        dir_name = os.path.join(save_dir, os.path.basename(file).split(".")[0])
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
      
        frame_num = 0
        count = 0
        vidcap = cv2.VideoCapture(file)
        success, frame = vidcap.read()

        while success:

            # save only frames with human faces
            detect_res = detector.detect_faces(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            if len(detect_res)>0 and count%skip_num==0:

                #file_name = os.path.join(dir_name,"frame_%d.jpg" % frame_num)
                file_name = os.path.normpath(os.path.join(dir_name,"frame_%d.jpg" % frame_num))
                # bbox = (x,y,w,h)
                ## bbox = (detect_res[0]['box'][0],detect_res[0]['box'][1],detect_res[0]['box'][2],detect_res[0]['box'][3])


                #print(file_name)
                #label_txt = file.split("/")[-1]
                label = 1
                #os.path.basename(file)
                #print(label)
 
                # file_name x y w h label
                ## file_list.writelines("%s %d %d %d %d %d\n"%(file_name,bbox[0],bbox[1],bbox[2],bbox[3],label))
                # text can be viewed when file is closed in file_list.close()
                write_line = "%s %d \n"%(file_name,label)
                file_list.writelines(write_line)  
                print(write_line)

                cv2.imwrite(file_name,frame)
                frame_num+=1
                
            count+=1
            success, frame = vidcap.read()  # get the next frame

        vidcap.release()

    file_list.close()
    

def read():

    file = open("C:/Users/dell/FYP/Dataset/remaining/file_list.txt")  # open a file
    for line in file:
        print(line.strip("\n").split(" "))


if __name__ == '__main__':

    

    db_dir = "C:/Users/dell/FYP/Dataset/remaining"
    save_dir = "C:/Users/dell/FYP/Dataset/remaining/frames"
    generate_frames_and_bbox(db_dir,save_dir,3)
    #read()



'''
-------------------------------------------------------------------------------------------------------------------
-------------------------------------------- CODE FOR IMAGE PROCESSING --------------------------------------------
-------------------------------------------------------------------------------------------------------------------
'''
'''
# TODO using pip install
from mtcnn.mtcnn import MTCNN
import cv2
import os
from glob import glob
import pandas as pd


detector = MTCNN()
true_img_start = ('1', '2', 'HR_1')
def generate_frames_and_bbox(db_dir,save_dir,skip_num):
    
    
    print("generate_frames_and_bbox | generate_frames_and_bbox.py")  
    
    file_list = open(save_dir+"/file_list.txt","a")

    #df = pd.read_csv('%s/liveness_train/train/label.csv' %db_dir)

    for file in glob('%s/dataset_processed/print/*/*.jpg'%db_dir): #pathname
        #/liveness_train/train/videos/*.mp4
        file = os.path.normpath(file)
        print("Processing image %s"%file)
        #dir_name = os.path.normpath(os.path.join(save_dir, *file.replace(".mp4", "").split("/")[-3:]))
        
        #print(dir_name)
        #if not os.path.exists(dir_name):
        #   os.makedirs(dir_name)   
        
        #frame_num = 0
        #count = 0
        #vidcap = cv2.VideoCapture(file)
        #success, frame = vidcap.read()
        frame = cv2.imread(file)
        

        #while success:
        
            # Save only frames with human faces
            #detect_res = detector.detect_faces(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            #if len(detect_res)>0 and count%skip_num==0:

                #file_name = os.path.join(dir_name,"frame_%d.png" % frame_num)
                # bbox = (x,y,w,h)
                ##bbox = (detect_res[0]['box'][0],detect_res[0]['box'][1],detect_res[0]['box'][2],detect_res[0]['box'][3])

                #label_txt = file.split("/")[-1]
                #label_txt=os.path.basename(file)
                #print(label_txt)
                #.replace(".mp4", "")

                #df.query('fname==@label_txt')["liveness_score"]
        label = 1

                # file_name x y w h label
                ##file_list.writelines("%s %d %d %d %d %d\n"%(file_name,bbox[0],bbox[1],bbox[2],bbox[3],label))
        file_list.writelines("%s %d \n"%(file,label))

                #cv2.imwrite(file,frame)
                #frame_num+=1

            #count+=1
            #success, frame = vidcap.read()  # get the next frame

        #vidcap.release()

    file_list.close()

def read():


    print("read | generate_frames_and_bbox.py")


    file = open("../../dataset/file_list.txt")  # open a file
    for line in file:
        print(line.strip("\n").split(" "))


if __name__ == '__main__':


    print("main | generate_frames_and_bbox.py")

    db_dir = "../../dataset" #pathname
    save_dir = "../../dataset/dataset_processed" #pathname
    generate_frames_and_bbox(db_dir,save_dir,3)

'''
