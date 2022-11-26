#8.1
# fruits_dic = {'사과':0, '배':0, '수박':0, '귤':0, '포도':0}

# price = list(map(int,input("사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력 :").split()))


# fruits_dic['사과'] = price[0]
# fruits_dic['배'] = price[1]
# fruits_dic['수박'] = price[2]
# fruits_dic['귤'] = price[3]
# fruits_dic['포도'] = price[4]


# print("---------오늘의 과일 가격----------")
# for key,num in fruits_dic.items() :
#     print(key, ':', num)

#8.3.1
# student = {'211101' : ['조성훈', '010-1234-4500'], '211102' : ['김은지', '010-2230-6540'],
#            '211103' : ['윤소정', '010-3232-7788'] }
 
# print('학생들의 정보 목록')
 
# for key in student.keys() :
#     print('{', end ='')
#     print("'{}' : {}".format(key, student[key]), end = '')
#     print('}', end = '\n')

#8.3.2
# student_tup = {'211101' : ['조성훈', '010-1234-4500'], '211102' : ['김은지', '010-2230-6540'],
#            '211103' : ['윤소정', '010-3232-7788'] }

# num = input('학번을 입력하시오: ')
# print('이름 :', student_tup[num][0])
# print('연락처 :', student_tup[num][1])

#8.3.3
# student_tup = {'211101' : ['조성훈', '010-1234-4500',4.3], '211102' : ['김은지', '010-2230-6540',3.9],
#            '211103' : ['윤소정', '010-3232-7788',4.25] }

# print('학생들의 정보 목록')
 
# for key in student_tup.keys() :
#     print('{', end ='')
#     print("'{}' : {}".format(key, student_tup[key]), end = '')
#     print('}', end = '\n')
      
#8.3.4
# student_tup = {'211101' : ['조성훈', '010-1234-4500',4.3], '211102' : ['김은지', '010-2230-6540',3.9],
#            '211103' : ['윤소정', '010-3232-7788',4.25] }

# sum = 0

# for key in student_tup.keys() :
#     sum = sum+student_tup[key][2]

# print("전체 학생의 학점 평균 : ",round(sum/len(student_tup.keys()),2))

#8.5
print("사전 프로그램 시작... 종료는 q를 입력")
dic = {}

while True:
    st = input('$ ')
    command = st[0]
    if command == '<':
        st = st[1:]
        inputStr = st.split(':')
        if len(inputStr) < 2:
            print("입력 오류가 발생했습니다.")
        else:
            dic[inputStr[0].strip()] = inputStr[1].strip()
    elif command == '>':
        st = st[1:]
        inputStr = st.strip()
        if inputStr in dic:
            print(dic[inputStr])
        else:
            print("{}가 사전에 없습니다.".format(inputStr))
    elif command == 'v':
        print("영어 사전에 있는 단어와 뜻을 출력합니다.")
        for key in dic.keys():
            print("{} :  {}".format(key, dic[key]), end = '')
            print(end = '\n')
    elif command == 'q':
        break
    else :
        print("입력 오류가 발생했습니다.")
    
print("사전 프로그램을 종료합니다.")

