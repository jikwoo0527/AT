# 이미 테스트했던 점수를 가지고 결과를 보는 함수
def receive_A(A):
    A = int(input("애착형 점수를 입력해주세요: "))

def receive_B(B):
    B = int(input("불안형 점수를 입력해주세요: "))

def receive_C(C):
    C = int(input("회피형 점수를 입력해주세요: "))

def receive_D(D):
    D = int(input("미해결형 점수를 입력해주세요: "))

def already_test(A, B, C, D):
    print("\n")

    receive_A(A) # 첫번째 실행
    if A > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if A < 20:
            pass
        else:
            print("잘못된 답변입니다.\n")
            receive_A(A)
    else:
        print("잘못된 답변입니다.\n")
        receive_A(A)

    receive_B(B) # 첫번째 실행
    if B > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if B < 20:
            pass
        else:
            print("잘못된 답변입니다.\n")
            receive_B(B)
    else:
        print("잘못된 답변입니다.\n")
        receive_B(B)

    receive_C(C) # 첫번째 실행
    if C > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if C < 20:
            pass
        else:
            print("잘못된 답변입니다.\n")
            receive_C(C)
    else:
        print("잘못된 답변입니다.\n")
        receive_C(C)

    receive_D(D) # 첫번째 실행
    if D > 0: # 입력 받은 값이 잘못 됐을 경우 다시 실행
        if D < 20:
            pass
        else:
            print("잘못된 답변입니다.\n")
            receive_D(D)
    else:
        print("잘못된 답변입니다.\n")
        receive_D(D)
