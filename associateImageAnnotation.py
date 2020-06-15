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
    data_date = sys.argv[1]
    sequence_id = sys.argv[2]
    vehicle_type = 'truck'
elif params_num <= 4:
    data_date = sys.argv[1]
    sequence_id = sys.argv[2]
    vehicle_type = sys.argv[3]

root_dir = '/media/hy/DATA3/TITAN/level_01/kitti/%s/'%vehicle_type

imgpath = '%s/%s/sequence_%s/testing/image_0'%(root_dir, data_date, sequence_id)
annopath = '%s/%s/sequence_%s/testing/image_0_annotation_voc'%(root_dir, data_date, sequence_id)

savepath = '%s/%s/sequence_%s/testing/image_0_annotation_filtered'%(root_dir, data_date, sequence_id)
savepath_image = '%s/image'%savepath
savepath_label = '%s/label'%savepath

# get the amount of the annotation files
annotation_files_num = len(os.listdir(annopath));

root = os.path.abspath(imgpath)
if os.path.exists(savepath):
    # if the save path already exist, remove it first
    shutil.rmtree(savepath, ignore_errors=True)
    os.mkdir(savepath)
else:
    os.mkdir(savepath)

if os.path.exists(savepath_image):
    # if the save path already exist, remove it first
    shutil.rmtree(savepath_image, ignore_errors=True)
    os.mkdir(savepath_image)
else:
    os.mkdir(savepath_image)

if os.path.exists(savepath_label):
    # if the save path already exist, remove it first
    shutil.rmtree(savepath_label, ignore_errors=True)
    os.mkdir(savepath_label)
else:
    os.mkdir(savepath_label)

imagelist = os.listdir(imgpath)
xmllist = os.listdir(annopath)

print 'total images: %d, total annotation files: %d'%(len(imagelist), len(xmllist))

for index in range(annotation_files_num):
    current_annotation_index_filename = xmllist[index]
    current_annotation_index = os.path.splitext(current_annotation_index_filename)

    imgfilesrc = imgpath + '/' + current_annotation_index[0] + '.png'
    imgfiledest = savepath_image + '/' + current_annotation_index[0] + '.png'
    xmlfilesrc = annopath + '/'  + current_annotation_index[0] + '.xml'
    xmlfiledest = savepath_label + '/'  + current_annotation_index[0] + '.xml'
    
    ## copy the files
    shutil.copyfile(imgfilesrc, imgfiledest)
    shutil.copyfile(xmlfilesrc, xmlfiledest)
    print('processing %s.png' % current_annotation_index[0])

print('FINISHED')
