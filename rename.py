import os

n = 1
path = 'D://ocrpic/'
file_name_list = os.listdir(path)
for i in file_name_list:
    file_name = path + file_name_list[n-1]
    count = "%03d" % n
    new_filename = path + count + ".tif"
    os.rename(file_name, new_filename)
    n += 1
