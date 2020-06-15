## usage of the python script

### checkAnnotationRandom.py
    随机检查数据集标注的情况，将标注框渲染到图像上.
`python checkAnnotationRandom.py 20190508 10 0.002`  
`python checkAnnotationRandom.py 20190508 17 0.002`  
`python checkAnnotationRandom.py 20190627 01 0.002`  

### associateImageAnnotation.py
    在原始图像中筛选标注过的图像.
`python associateImageAnnotation.py 20190627 01`  
`python associateImageAnnotation.py 20190508 10`  
`python associateImageAnnotation.py 20190508 17`  

### validateAnnotation.py
    查看标注文件和图像是否一一匹配.
`python validateAnnotation.py 20190627 01`  
`python validateAnnotation.py 20190508 10`  
`python validateAnnotation.py 20190508 17`  

### statisticalAnnotation.py
    统计标注文件夹下标注框的总数, 以及每一类框的个数.
`python statisticalAnnotation.py 20190627 01`  
`python statisticalAnnotation.py 20190508 10`  
`python statisticalAnnotation.py 20190508 17`  
