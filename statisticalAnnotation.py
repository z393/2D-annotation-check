# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import cv2
import sys
import shutil
import random

def parse_obj(xml_filename):
    tree=ET.parse(xml_filename)
    objects=[]
    for obj in tree.findall('object'):
        obj_struct={}
        obj_struct['name']=obj.find('name').text
        objects.append(obj_struct)
    return objects

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

# get the amount of the annotation files
annotation_files_num = len(os.listdir(annopath));

imagelist = os.listdir(imgpath)
xmllist = os.listdir(annopath)

print 'total images: %d, total annotation files: %d'%(len(imagelist), len(xmllist))

classnames=[]
num_objs={}

for index in range(annotation_files_num):
    current_annotation_index_filename = xmllist[index]
    current_annotation_index = os.path.splitext(current_annotation_index_filename)

    name = current_annotation_index[0]

    xmlfilesrc = annopath + '/'  + name + '.xml'

    objects = parse_obj(xmlfilesrc)

    for object in objects:
        if object['name'] not in num_objs.keys():
            num_objs[object['name']]=1
        else:
            num_objs[object['name']]+=1
        if object['name'] not in classnames:
            classnames.append(object['name'])

for name in classnames:
    print('{}:{}'.format(name,num_objs[name]))
print('FINISHED')
