import os
import sys

print("脚本名" + sys.argv[0])
for i in range(1,len(sys.argv)):
    print("参数" + str(i) + " " + sys.argv[i])

# os.system("start explorer c:")