#1vs1 끝말잇기
pla1=input("플레이어1의 이름을 선택해주세요:")
pla2=input("플레이어2의 이름을 선택해주세요:")
li=[]
check="b"
b=0
win=0

print()
print("플레이어 1부터 시작합니다")
for i in range(1000000):
    1==1
print("게임이 끝나면 진 사람의 차례때 'end'라고 해주세요")
for j in range(1000000):
    1==1
print("그럼 시작합니다!")
for k in range(1000000):
    1==1

a=input("{}는(은) 단어를 말해주세요:".format(pla1))
li.append(a)
while a!="end" or b!="end":
    if check=="a":
        a=input("{}는(은) 단어를 말해주세요:".format(pla1))
        if a=="end":
            win=pla2
            break
        elif a[0]!=b[len(b)-1]:
            print("다시 입력해주세요(사용 불가 단어):")
        
        else:
            check="b"
            li.append(a)
    
    if check=="b":
        b=input("{}는(은) 단어를 말해주세요:".format(pla2))
        if b=="end":
            win=pla1
            break
        elif b[0]!=a[len(a)-1]:
            print("다시 입력해주세요(사용 불가 단어):")
        
        else:
            check="a"
            li.append(b)
        
print("승자는 {}입니다!".format(win)) 