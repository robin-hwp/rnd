import re

# 숫자 포멧에 맞는 문자 검색
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo1.group())

# 괄호'()'로 둘러싸여 있는 2가지 그룹 형식이 같고 그룹 중간에 '-'도 일치하는 문자열 검색
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is 415-555-4242.')
print(mo2.group())
print(mo2.group(0))
print(mo2.group(1))
print(mo2.group(2))

# 문자열에서 괄호까지 호함된 그룹 검색 \(, \) 주의
phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex3.search('My phone number is (415) 555-4242.')
print(mo3.group(0))
print(mo3.group(1))
print(mo3.group(2))

# 여러개 중 먼저 일치하는 것을 검색할때 '|'를 사용한다.
heroRegex = re.compile (r'Batman|Tina Fey')
mo401 = heroRegex.search('Batman and Tina Fey.')
print(mo401.group())
mo402 = heroRegex.search('Tina Fey and Batman.')
print(mo402.group())

# 패턴 블럭을 |를 사용해서 선택한다.
batRegex5 = re.compile(r'Bat(man|mobile|copter|bat)')
mo5 = batRegex5.search('Batmobile lost a wheel')
print(mo5.group())
print(mo5.group(1))

#  ()? 블럭안의 내용이 0번 또는 1번인 경우 검색
# You can think of the ? as saying, 
# “Match zero or one of the group preceding this question mark.”

phoneRegex6 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6_1 = phoneRegex6.search('My number is 415-555-4242')
print(mo6_1.group())
mo6_2 = phoneRegex6.search('My number is 555-4242')
print(mo6_2.group())

# The * (called the star or asterisk) means “match zero or more”
batRegex7 = re.compile(r'Bat(wo)*man')
mo7_1 = batRegex7.search('The Adventures of Batman')
print(mo7_1.group())
mo7_2 = batRegex7.search('The Adventures of Batwoman')
print(mo7_2.group())
mo7_3 = batRegex7.search('The Adventures of Batwowowowoman')
print(mo7_3.group())

# The + (or plus) means “match one or more
batRegex8 = re.compile(r'Bat(wo)+man')
mo8_1 = batRegex8.search('The Adventures of Batwoman')
print(mo8_1.group())
mo8_2 = batRegex8.search('The Adventures of Batwowowowoman')
print(mo8_2.group())
mo8_3 = batRegex8.search('The Adventures of Batman')
print( 'The Match is None : {}'.format(mo8_3 == None) )

# 블럭을 반복하는 방법 (블럭){3} : (블럭)을 3번 반복하라는 의미
haRegex9 = re.compile(r'(Ha){3}')
mo9_1 = haRegex9.search('HaHaHa')
print(mo9_1.group())
mo9_2 = haRegex9.search('Ha')
print( 'The Match is None : {}'.format(mo9_2 == None) )

# different Greedy and Nongreedy

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo10 = greedyHaRegex.search('HaHaHaHaHa')
print( 'Greedy Match : ', + mo10.group())


nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo11 = nongreedyHaRegex.search('HaHaHaHaHa')
print( 'Nongreedy match : ' + mo11.group())


