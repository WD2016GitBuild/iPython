#coding:utf8
import os;

def rename(path):
    # print(path)
    filelist = os.listdir(path)
    for file in filelist:
        # print(file)
        old_name = file
        old_dir = os.path.join(path, file)
        if os.path.isdir(old_dir):  # 如果是文件夹，则跳过
            continue;
        file_name = os.path.splitext(file) # 将文件拆分成文件名和后缀名(.jpg)
        # print(file_name)
        file_name_1 = file_name[0]
        file_name_2 = file_name[1].lower()
        # print(file_name_1)
        # print(file_name_2)
        if "jpg" in file_name_2 or "png" in file_name_2: # 只针对图片文件
            # print(file_name_1)
            if "-" in file_name_1:  # 判断文件名中是否存在-
                file_name_1 = file_name_1.replace("-", "_") # 将-替换成_
                new_dir = os.path.join(path, file_name_1 + file_name_2)
                # 如果文件存在，则将之删除
                if os.path.exists(new_dir): # 判断文件是否存在
                    os.remove(new_dir)  # 删除文件
                os.rename(old_dir, new_dir)
                print(old_name + "    替换成    " + file_name_1 + file_name_2)

rename(r"D:\中企动力\2018-05-11-四川蓉汇工程机械设备服务有限公司+全网门户+首购-吴东-陈秋霖\PSD\PSD3")
