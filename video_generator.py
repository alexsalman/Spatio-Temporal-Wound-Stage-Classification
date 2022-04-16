# Cropped Images Folder
# Parse Images to Videos using openCV
import os
import cv2
import glob
import numpy as np


os.getcwd()
#### All Names of Files in One Directory ############################################
################################################################################
image_directory = {}
for filename in glob.glob('Cropped_images/*.png'):
    # could it be made better?
    mouse_age = filename[19:-4].split('_')[1].split('-')[0]
    mouse_number = filename[19:-4].split('_')[1].split('-')[1]
    mouse_orientation = filename[19:-4].split('_')[1].split('-')[2]
    day = int(filename[19:-4].split('_')[0])
    # mouse_age not in image_directory
    if mouse_age not in image_directory:
        image_directory[mouse_age] = {}
        image_directory[mouse_age][mouse_number] = {}
        image_directory[mouse_age][mouse_number][mouse_orientation] = []
        image_directory[mouse_age][mouse_number][mouse_orientation].append(day)
    else:
        # mouse_number not in mouse_age
        if mouse_number not in image_directory[mouse_age]:
            image_directory[mouse_age][mouse_number] = {}
            image_directory[mouse_age][mouse_number][mouse_orientation] = []
            image_directory[mouse_age][mouse_number][mouse_orientation].append(day)
        else:
            # mouse_orientation not in mouse_number
            if mouse_orientation not in image_directory[mouse_age][mouse_number]:
                image_directory[mouse_age][mouse_number][mouse_orientation] = []
                image_directory[mouse_age][mouse_number][mouse_orientation].append(day)
            else:
                # day not in mouse_orientation
                image_directory[mouse_age][mouse_number][mouse_orientation].append(day)

#### Structures of Video Length Consecutively ##################################
################################################################################
count = 0
for mouse_age in image_directory:
    for mouse_number in image_directory[mouse_age]:
        for mouse_orientation in image_directory[mouse_age][mouse_number]:
            VLC = 1
            while VLC <= 16:
                img_array = []
                for day in sorted(image_directory[mouse_age][mouse_number][mouse_orientation], reverse=False):
                    filename = 'Cropped_images/' + 'Day' + ' ' + str(day) + '_' + mouse_age + '-' + mouse_number + '-' + mouse_orientation + '.' + 'png'
                    img_array.append(cv2.imread(filename))
                    if len(img_array) == VLC:
                        filename = 'Day' + ' ' + str(day) + '_' + mouse_age + '-' + mouse_number + '-' + mouse_orientation + '-' + 'VLC' + str(VLC) + '.' + 'mp4'
                        framesize = (352, 352)
                        out = cv2.VideoWriter(filename ,cv2.VideoWriter_fourcc(*'mp4v'), 1, framesize)
                        for iDay in range(len(img_array)):
                            out.write(img_array[iDay])
                        out.release()
                        img_array.pop(0)
                        count += 1
                VLC += 1
print("Total videos generated: ", count, "!")
