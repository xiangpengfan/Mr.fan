import os

'''
这个功能可以查找指定目录下的所有文件，并且可以根据文件名进行过滤
'''

def find_files(path,keyword):
    num=0
    for root,dirs,files in os.walk(path):
        for file in files:
            if keyword in file:
                path1=os.path.join(root,file)   #这好像有点问题
                print(f'找到文件：{os.path.relpath(path1,path)}')
                #print(f'找到文件：{file}')
                num+=1
    print(f'总共找到{num}个文件')
if __name__=='__main__':
    path=input('请输入要查找的目录：')
    if not os.path.exists(path):
        print('目录不存在，请检测后重新输入')
        exit()
    if not os.path.isdir(path):
        print('输入的不是一个目录，请检查后重新输入')
        exit()
    keyword=input('请输入要查找的文件名关键字：')
    find_files(path,keyword)