import os, shutil

os.chdir('./study/python/09.files/test')
print(os.getcwd())

# 파일 복사
shutil.copy('../abs_ch_09_shutil.py', '.')
shutil.copy('../abs_ch_09_shutil.py', './abs_ch_09_shutil.copy_rename.py')
print('copy result :')
print(os.listdir())
print('')


# 이미 폴더가 있으면 폴더 삭제
if os.path.isdir('../test2'):
    shutil.rmtree('../test2')

# 디렉토리 복사
print('shutil.copytree() test :')
print(os.listdir('..'))
shutil.copytree('../test', '../test2')
print("shutil.copytree('../test', '../test2')")
print(os.listdir('..'))
print('')

shutil.copy('../abs_ch_09_shutil.py', '../abs_ch_09_shutil.temp0.py')
shutil.copy('../abs_ch_09_shutil.py', '../abs_ch_09_shutil.temp1.py')
shutil.move('../abs_ch_09_shutil.temp0.py', './abs_ch_09_shutil.move0.py')
shutil.move('../abs_ch_09_shutil.temp1.py', './abs_ch_09_shutil.move1.py')
print('move result :')
print(os.listdir())
print('')

shutil.copy('../abs_ch_09_shutil.py', './abs_ch_09_shutil.temp0.py')
print('copyto ./abs_ch_09_shutil.temp0.py')
print(os.listdir())
os.unlink('./abs_ch_09_shutil.temp0.py')
print('os.unlink(./abs_ch_09_shutil.temp0.py) result :')
print(os.listdir())

# 파일 생성 후 휴지통으로 보낸다.
# how to install send2trash.> python -m pip install send2trash
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('bacon.txt')


# 대상 디렉토리의 하위 디렉토리까지 모두 돌면서 확인.
for folderName, subfolders, filenames in os.walk('..'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')
