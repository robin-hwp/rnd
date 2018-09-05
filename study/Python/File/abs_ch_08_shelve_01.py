import shelve
import pprint

# shelve를 이용한 리스트 파일 핸들링
# shelve를 이용하면 filename.dat와 filename.dir 파일이 생성되고 
# 생성된 파일 2개 모두 있어야 오픈할때 이름으로 읽어들인다.
# 리스트 및 딕셔너리가 복합적으로 결합되어도 문제없이 동작한다.

# shelve를 이용한 리스트 저장

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# shelve를 이용한 리스트 로드
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()


# shelve플 이용한 리스트 및 딕셔너리

# shelve를 이용한 타입 저장
shelfFile2 = shelve.open('mydata2')
cats2 = [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
shelfFile2['cats'] = cats2
shelfFile2.close()

# shelve를 이용한 리스트 로드
shelfFile2 = shelve.open('mydata2')
print(type(shelfFile2))
pprint.pprint(shelfFile2['cats'])
shelfFile2.close()


