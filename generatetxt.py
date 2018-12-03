import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='VOCdevkit/VOC2018/JPEGImages/'
    dest='VOCdevkit/VOC2018/ImageSets/Main/train.txt'
    dest2='VOCdevkit/VOC2018/ImageSets/Main/test.txt'
    file_list=os.listdir(source_folder)
    train_file=open(dest,'a')
    test_file=open(dest2,'a')
    for file_obj in file_list:
        file_path=os.path.join(source_folder,file_obj)
        file_name,file_extend=os.path.splitext(file_obj)
        file_num=int(file_name)
        if(file_num<800):
            train_file.write(file_name+'\n')
        else:
            test_file.write(file_name+'\n')
    train_file.close()
test_file.close()
