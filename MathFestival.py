#수학 계산을 위한 sympy 모듈 포함
from sympy import *
# from sympy.functions import *
# from sympy import symbols
# from sympy import simplify
# from sympy import Limit
# from sympy import S
# from sympy import Function
# from sympy import pprint
# from sympy import Symbol
# from sympy import Series

#콘솔 제어를 위한 ctypes 모듈 포함
import ctypes

#명령 상수화
STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12

#콘솔 API 사용을 위한 변수
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

#콘솔 컬러 사용을 위한 함수
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

#입력 방법을 알려주는 함수
def notice_bef_insert():
    set_color(10)
    print('※입력 기호 안내\n')
    print('1. 루트식은 sqrt()로 묶어줘야함, 무한대는 oo (알파벳 소문자 o두개)\n   ex)sqrt(x**2+2x)')
    print('2. 곱하기는 *로 사용,\n   ex)x**2+2*x+4+a+4*a')
    print('3. 제곱은 **로 사용,\n   ex)x**7+x**5')
    print('4. 나누기는 /을 사용,\n   ex)4/5 (=5분의 4)')
    print('5. 절대값, 가우스 기호 사용 불가능')
    print('6. +,-로 구분된 식들을 ()로 정확히 구분,\n   ex)((x**2+2*x)/(x**3+4*x))+(x)\n')
    set_color(7)


#변수,상수 및 함수로 사용될 문자들 정의
n,x,y,z = symbols("n,x,y,z")
a,b,c,d,k,p,q,r = symbols("a,b,c,d,k,p,q,r")
f,g,h = symbols("f,g,h", cls = Function)

#종료 플래그
end_flag = 1

set_color(31)
print('                                                    ')
print('                                                    ')
print('          Paekun High school Math Festival          ')
print('                   <극한과 미분>                    ')
print('                made by 20324 junwha                ')
print('                                                    ')
print('                                                    \n')
set_color(7)

while end_flag:
    print("문제의 분류를 선택하세요. \n1.극한값 구하기(함수/수열) 2.미분 0.종료")
    #메뉴 선택용 변수
    sel_num = int(input())

    #1. 극한값 구하기(함수/수열)
    if sel_num == 1:
        print('극한값 구하기 문제의 유형을 선택하세요\n')
        print('유형1. 극한값 구하기(1)')
        print('유형2. 극한의 대소(2)')
        print('->',end='')
        #메뉴 선택용 변수
        sel_num = int(input())
        #유형1. 극한값 구하기
        if sel_num == 1:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a... , Limit 아래 사용되는 문자)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('수식을 입력하세요.')
            print('lim('+v+'->',end = " ") 
            to = (input())
            print(')', end = '')
            equation = (input()) #수식 입력
            f = simplify(equation)  #문자열을 sympy형식에 맞게 변환
            print('lim('+v+'->'+to+')'+equation+'=')
            pprint(Limit(f, var, to).doit()) #Limit 함수로 극한 계산 후 출력
        #유형2. 수열의 극한의 대소
        elif sel_num == 2:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('lim('+v+'->',end = " ") 
            to = (input())
            print('lim('+ v+'->'+to+')좌변 <= lim('+v+'->'+to+')An <= lim('+v+'->'+to+')우변 형태의 식을 입력하세요.\n')
            print('좌변: lim('+v+'->'+to+')')
            equation = (input()) #수식 입력
            f = simplify(equation)
            print('우변: lim('+v+'->'+to+')')
            equation = (input()) #수식 입력
            g = simplify(equation) #sympy에 맞게 변환
            print()
            if Limit(f, var, to).doit()==Limit(g, var, to).doit():
                if Limit(f, var, to).doit() == oo: #한쪽의 극한값이 무한대일 경우
                    print('lim('+v+'->'+to+')') 
                    print(f)
                    print('<=lim('+v+'->'+to+')An<='+'lim('+v+'->'+to+')')
                    print(g)
                else: #양쪽 모두 같은 값으로 수렴하는 수열일 경우
                    print('lim('+v+'->'+to+')An = ')
                    pprint(Limit(f, v, to).doit())
            elif  Limit(f, var, to).doit()!=Limit(g, var, to).doit(): #양쪽이 다르게 수렴하는 수열일 경우
                print('lim('+v+'->'+to+')')
                print(f)
                print('<= lim('+v+'->'+to+')An <='+'lim('+v+'->'+to+')')
                print(g)
    
    #2.미분
    elif sel_num == 2:
        print('도함수 문제의 유형을 선택하세요\n')
        print('유형1. 평균변화율 구하기(1)')
        print('유형2. 도함수 구하기(2)')
        print('유형3. 미분계수 구하기(3)')
        print('유형4. 함수 위의 점(a,f(a))에 그은 접선(4)')
        print('유형5. 함수 밖의 점 (a,b)에서 그은 접선(5)')
        print('유형6. 기울기가 주어졌을 때 접선이 그어진 함수 위의 점 (a,f(a))의 좌표(6)')
        print('->',end='')
        #메뉴 선택용 변수
        sel_num = int(input())
        
        #유형1. 평균변화율 구하기
        if sel_num == 1:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            print('f('+v+')=',end = " ") 
            f = simplify(input())
            print('a에서 b까지의 평균변화율을 구하려고 할 때, a,b를 입력하세요.')
            print('a=',end="")
            a = int(input())
            print('b=',end="")
            b = int(input())
            print('(a에서 b까지 평균변화율)=')
            pprint((f.subs(var,b)-f.subs(var,a))/(b-a))

        #유형2.도함수 구하기
        elif sel_num == 2:  
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            print('f('+v+')=',end = " ") 
            f = simplify(input())
            print('f\'('+v+')=')
            pprint(Derivative(f,var).doit()) #미분
        
        #유형3.미분계수 구하기
        elif sel_num == 3:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            f = simplify(input())
            print('f('+v+')=',end = " ")
            print(v+'=a에서의 미분계수를 구합니다.')
            print('a=')
            a=int(input())
            g = Derivative(f,var).doit() #미분
            pprint(g.subs(var,a))
        
        #유형4.함수 위의 점 (a,b)에 그은 접선
        elif sel_num == 4:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a..)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            print('f('+v+')=',end = " ")
            f = simplify(input())
            print('a=')
            a=int(input())
            g = Derivative(f,var).doit() #미분
            y=(g.subs(var,a))*(var-a)+f.subs(var,a)
            print('y=')
            pprint(y)

        #유형5. 함수 밖의 점 (a,b)에서 그은 접선
        elif sel_num == 5:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            print('f('+v+')=',end = " ")
            f = simplify(input())
            print('함수 밖의 점 (a,b)를 입력하세요.')
            print('a=')
            a=int(input())
            print('b=')
            b=int(input())
            g = Derivative(f,var).doit() #미분
            t = symbols('t')
            arr = (solve( ((f.subs(var,t)-b)/(t-a))-g.subs(var,t) )) #근의 개수
            if arr.__len__() == 0:
                print('접선을 그을 수 없습니다.')
            for i in arr:
                y = g.subs(var,i)*(x-i)+f.subs(var,i)
                print('y=')
                pprint(y)

        #유형6. 기울기가 주어졌을 때 접선이 그어진 함수 위의 점 (a,f(a))의 좌표(6)
        elif sel_num == 6:
            notice_bef_insert()
            print('사용할 변수를 입력해주세요(n,x,a...)')
            v = input() #변수 입력
            var = symbols(v) #변수 선언
            print('함수를 입력하세요.')
            print('f('+v+')=',end = " ")
            f = simplify(input())
            print('접선의 기울기 m을 입력하세요.')
            print('m=')
            m=int(input()) #기울기 입력
            g = Derivative(f,var).doit() #미분
            arr = solve(g-m) #f'(x)=m 인 x를 찾는다.
            if arr.__len__() == 0:
                print('접선을 그을 수 없습니다.')
            for i in arr:
                y = m*(x-i)+f.subs(var,i)
                print('y=')
                pprint(y)
    else: 
        print()
        print('프로그램을 종료합니다.')
        break

            
