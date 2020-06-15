# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import cv2
import sys
import shutil
import random

params_num = len(sys.argv)

if params_num <= 1:
    print 'you should input date such as 20190627'
    exit(0)
elif params_num <= 2:
    print 'you should input the sequence id such as 01'
    exit(0)
elif params_num <= 3:
    print 'you should input the random ratio such as 0.01 (0~1)'
    exit(0)
elif params_num <= 4:
    data_date = sys.argv[1]
    sequence_id = sys.argv[2]
    random_ratio = float(sys.argv[3])
    vehicle_type = 'truck'
elif params_num <= 5:
    data_date = sys.argv[1]
    sequence_id = sys.argv[2]
    random_ratio = float(sys.argv[3])
    vehicle_type = sys.argv[4]

if random_ratio < 0:
    print 'random_ratio smaller then 0, will be set to 0'
    random_ratio = 0;
elif random_ratio > 1:
    print 'random_ratio larger then 1, will be set to 1'
    random_ratio = 1;

root_dir = '/media/hy/DATA3/TITAN/level_01/kitti/%s/'%vehicle_type

imgpath = '%s/%s/sequence_%s/testing/image_0'%(root_dir, data_date, sequence_id)
annopath = '%s/%s/sequence_%s/testing/image_0_annotation_voc'%(root_dir, data_date, sequence_id)
savepath = '%s/%s/sequence_%s/testing/image_0_annotation_render'%(root_dir, data_date, sequence_id)

# get the amount of the annotation files
annotation_files_num = len(os.listdir(annopath));
random_num = int(random_ratio * annotation_files_num);

# generate the random index
random_annotation_indexes = random.sample(range(0, annotation_files_num), random_num)

root = os.path.abspath(imgpath)
if os.path.exists(savepath):
    # if the save path already exist, remove it first
    shutil.rmtree(savepath, ignore_errors=True)
    os.mkdir(savepath)
else:
    os.mkdir(savepath)

imagelist = os.listdir(imgpath)
xmllist = os.listdir(annopath)

print 'total images: %d, total annotation files: %d, choosing render files: %d'%(len(imagelist), len(xmllist), len(random_annotation_indexes))

for random_index in range(len(random_annotation_indexes)):
    current_random_index = random_annotation_indexes[random_index]
    current_annotation_index_filename = xmllist[current_random_index]
    current_annotation_index = os.path.splitext(current_annotation_index_filename)

    imgfile = imgpath + '/' + current_annotation_index[0] + '.png'
    #print(imgfile)
    xmlfile = annopath + '/'  + current_annotation_index[0] + '.xml'
    #print(xmlfile)
    im = cv2.imread(imgfile)
    tree=ET.parse(xmlfile)
    root=tree.getroot()
    for object in root.findall('object'):
        object_name=object.find('name').text
        #print(object_name)
        Xmin=int(object.find('bndbox').find('xmin').text)
        Ymin=int(object.find('bndbox').find('ymin').text)
        Xmax=int(object.find('bndbox').find('xmax').text)
        Ymax=int(object.find('bndbox').find('ymax').text)
        color = (4, 250, 7)
        cv2.rectangle(im,(Xmin,Ymin),(Xmax,Ymax),color,2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, object_name, (Xmin,Ymin - 7), font, 0.5, (6, 230, 230), 2)

    path = savepath + '/' + current_annotation_index[0] + '.png'
    cv2.imwrite(path, im)
    print('%s.png is saved' % current_annotation_index[0])

print('FINISHED')
