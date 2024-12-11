# 이미 테스트했던 점수를 가지고 결과를 보는 함수
def receive_A():
    A = int(input("애착형 점수를 입력해주세요: "))
    if A > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if A > 20:
            print("잘못된 답변입니다.\n")
            receive_A()
    else:
        print("잘못된 답변입니다.\n")
        receive_A()
    return A

def receive_B():
    B = int(input("불안형 점수를 입력해주세요: "))
    if B > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if B > 20:
            print("잘못된 답변입니다.\n")
            receive_B()
    else:
        print("잘못된 답변입니다.\n")
        receive_B()
    return B

def receive_C():
    C = int(input("회피형 점수를 입력해주세요: "))
    if C > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if C > 20:
            print("잘못된 답변입니다.\n")
            receive_C()
    else:
        print("잘못된 답변입니다.\n")
        receive_C()
    return C

def receive_D():
    D = int(input("미해결형 점수를 입력해주세요: "))
    if D > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if D > 20:
            print("잘못된 답변입니다.\n")
            receive_D()
    else:
        print("잘못된 답변입니다.\n")
        receive_D()
    return D

def already_test():
    print('\n')
    A = receive_A()
    B = receive_B()
    C = receive_C()
    D = receive_D()

    af_lever = 1
    return af_lever, A, B, C, D
