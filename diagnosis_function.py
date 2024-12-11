def Secure(A, B, C, result):
    if A - C > 5:
        if A - B > 5:
            result[0] = 1
        else:
            pass
    else:
        pass

def Secure_Anxious(A, B, result):
    if A > B:
        if B >= 5:
            result[1] = 1
        else:
            pass
    else:
        pass

def Secure_Avoidant(A, C, result):
    if A > C:
        if C >= 5:
            result[2] = 1
        else:
            pass
    else:
        pass

def Anxious(A, B, C, result):
    if B > A:
        if B > C:
            result[3] = 1
        else:
            pass
    else:
        pass

def Anxious_Secure(A, B, result):
    if B >= A:
        if A >= 5:
            result[4] = 1
        else:
            pass
    else:
        pass

def Avoidant(A, B, C, result):
    if C - A >= 5:
        if C - B >= 5:
            result[5] = 1
        else:
            pass
    else:
        pass

def Avoidant_Secure(A, C, result):
    if C - A >= 5:
        if A >= 5:
            result[6] = 1
        else:
            pass
    else:
        pass

def Fearful_Avoidant(A, B, C, result):
    if B - A >= 5:
        if C - A >= 5:
            result[7] = 1
        else:
            pass
    else:
        pass

def Unresolved(D, result):
    if D >= 5:
        result[8] = 1
    else:
        pass


def diagnosis_run(A, B, C, D, result):
    Secure(A, B, C, result)  # A, B, C, D 수치를 기반으로 애착 유형 진단
    Secure_Anxious(A, B, result)
    Secure_Avoidant(A, C, result)
    Anxious(A, B, C, result)
    Anxious_Secure(A, B, result)
    Avoidant(A, B, C, result)
    Avoidant_Secure(A, C, result)
    Fearful_Avoidant(A, B, C, result)
    Unresolved(D, result)

def result_print(lever, result):
    print("\n\n\n<결과>")
    if result[7] == 0:
        if result[0] == 1:
            print("당신은 안정형입니다. 불안형, 회피형 성향이 모두 낮고 가장 안정된 유형입니다.")
        elif result[1] == 1:
            print("당신은 안정-불안형입니다. 불안형 성향이 보이지만 전체적으로는 안정형인 유형입니다.")
        elif result[2] == 1:
            print("당신은 안정-회피형입니다. 회피형 성향이 보이지만 전체적으로는 안정형인 유형입니다.")
        elif result[3] == 1:
            print("당신은 불안형입니다. 불안형이 강하며, 대인 관계에 민감한 유형입니다.")
        elif result[4] == 1:
            print("당신은 불안-안정형입니다. 불안형이 강하지만 어느 정도 적응력이 있는 유형입니다.")
        elif result[5] == 1:
            print("당신은 회피형입니다. 회피형이 강하고 친밀한 관계가 되기 어려운 유형입니다.")
        elif result[6] == 1:
            print("당신은 회피-안정형입니다. 회피형이 강하지만 어느 정도 적응력이 있는 유형입니다.")
    else:
        print("당신은 공포회피형입니다. 불안형, 회피형이 모두 강하고, 상처에 민감하며, 의심이 많은 유형입니다.")

    if result[8] == 1:
        i = 0
        for i in result:
            if lever == 0:
                if i < 8:
                    if result[i] == 1:
                        print("또한 미해결형도 가지고 있습니다. 부모(양육자)와의 애착 상처를 오랫동안 안고 있었으며, 불안정해지기 쉬운 유형으로 다른 유형과 공존합니다.")
                        lever = 1
                    else:
                        pass
                else:
                    print("당신은 미해결형입니다. 부모(양육자)와의 애착 상처를 오랫동안 안고 있었으며, 불안정해지기 쉬운 유형으로 다른 유형과 공존합니다.")
        else:
            pass
    else:
        pass

num = [0, 0, 0, 0] # 각 점수를 입력한 num 리스트 생성

def primary_attachment(A, B, C, D):
    num[0] = A
    num[1] = B
    num[2] = C
    num[3] = D

    num_sorted = sorted(num)

    # 제일 강한 요소 진단
    if num_sorted[3] == A:
        print("기본적인 애착형은 안정형입니다.")
    elif num_sorted[3] == B:
        if B > 9:
            if B > 14:
                print("기본적인 애착형은 불안형이며 점수가 15점 이상으로 그 경향이 상당히 강합니다.")
            else:
                print("기본적인 애착형은 불안형이며 점수가 10점 이상으로 그 경향이 강합니다.")
        else:
            print("기본적인 애착형은 불안형입니다.")
    elif num_sorted[3] == C:
        if C > 9:
            if C > 14:
                print("기본적인 애착형은 회피형이며 점수가 15점 이상으로 그 경향이 상당히 강합니다.")
            else:
                print("기본적인 애착형은 회피형이며 점수가 10점 이상으로 그 경향이 강합니다.")
        else:
            print("기본적인 애착형은 회피형입니다.")
    elif num_sorted[3] == D:
        if D > 9:
            if D > 14:
                print("기본적인 애착형은 미해결형이며 점수가 15점 이상으로 그 경향이 상당히 강합니다.")
            else:
                print("기본적인 애착형은 미해결형이며 점수가 10점 이상으로 그 경향이 강합니다.")
        else:
            print("기본적인 애착형은 미해결형입니다.")
    else:
        pass

    # 두번째로 강한 요소 진단
    if num_sorted[2] == A:
        pass
    elif num_sorted[2] == B:
        if B > 4:
            print("부차적인 애착형은 불안형이며 점수가 5점 이상으로 이 경향도 무시할 수 없는 수준입니다.")
        else:
            print("부차적인 애착형은 불안형입니다.")
    elif num_sorted[2] == C:
        if C > 4:
            print("부차적인 애착형은 회피형이며 점수가 5점 이상으로 이 경향도 무시할 수 없는 수준입니다.")
        else:
            print("부차적인 애착형은 회피형입니다.")
    elif num_sorted[2] == D:
        if D > 4:
            print("부차적인 애착형은 미해결형이며 점수가 5점 이상으로 이 경향도 무시할 수 없는 수준입니다.")
        else:
            print("부차적인 애착형은 미해결형입니다.")
    else:
        pass

def num_print():
    print("애착형 점수는 ", num[0],"점, 불안형 점수는 ", num[1],"점, 회피형 점수는 ", num[2],"점, 미해결형 점수는 ", num[3],"점입니다.")