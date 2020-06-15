# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import cv2
import sys
import shutil
import random
import xml.etree.ElementTree as ET

def getAnnotationFilename(annopath, xmlfilename):
    tree=ET.parse(annopath + '/' + xmlfilename)
    root = tree.getroot()
    filenameObj = root.find('filename')
    return filenameObj.text

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
annopath = '%s/%s/sequence_%s/testing/image_0_annotation_voc'%(root_dir, data_date, sequence_id)

# get the amount of the annotation files
annotation_files_num = len(os.listdir(annopath));

xmllist = os.listdir(annopath)

print 'total annotation files: %d'%(len(xmllist))

for index in range(annotation_files_num):
    current_annotation_index_filename = xmllist[index]
    current_annotation_index = os.path.splitext(current_annotation_index_filename)

    xmlfile = current_annotation_index[0] + '.xml'
    xmlfilename = getAnnotationFilename(annopath, xmlfile);

    current_annotation_filename_index = os.path.splitext(xmlfilename)
    
    if current_annotation_filename_index[0] != current_annotation_index[0]:
        print '%s.xml filename mismatch with the %s.png'%(current_annotation_index[0], current_annotation_filename_index[0])

print('FINISHED')
