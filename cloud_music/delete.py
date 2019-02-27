import re
import os
import os.path

# lists = ['伤感','思念','兴奋','性感','治愈']
lists = ['怀旧']
for list in lists:
    rootdir ="E:\\yunyinyue\\train\\"+list
    # print(rootdir1)
# rootdir='E:\\yunyinyue\\train\\清新'
    for filenames in os.walk(rootdir):
        allfile = filenames[2]
        print(len(allfile))
        # print(allfile)
        for file in allfile:
            # print(file)
            all_chinese_num = 0
            filepath = rootdir + "\\" + file
            file1 = open(filepath, 'r', encoding='utf-8')
            try:
                for line in file1:
                    chinese = re.compile('[\u4e00-\u9fa5]')
                    all = re.findall(chinese, line)
                    if len(all) > 10:
                        # print(len(all))
                        all_chinese_num = len(all)
                file1.close()
                if all_chinese_num < 10:
                    os.remove(filepath)
            except:
                print(file+"读取出错")
    # print("num  = ",'+str(num))
    print(list+"删除完成")