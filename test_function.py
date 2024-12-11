A = 0
B = 0
C = 0
D = 0

answer_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def question_1():
    global A
    print("페이지 I")
    print("1. 적극적으로 새로운 일을 시작하거나 새로운 장소, 새로운 사람을 만나는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[0] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_1()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_1()

    question_2()

def question_2():
    global A, C
    print("\n2. 누구와도 금방 대화할 수 있고 친해지는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            C+=2
        elif answer == 3:
            answer_3[1] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_2()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_2()

    question_3()

def question_3():
    global A
    print("\n3. 만약 곤란한 일이 생겨도 어떻게 되겠지 하고 낙관적으로 생각하는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[2] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_3()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_3()
    question_4()

def question_4():
    global A
    print("\n4. 친한 친구나 지인을 진심으로 신뢰하는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[3] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_4()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_4()
    question_5()

def question_5():
    global A
    print("\n5. 누군가를 질책하는 등 공격적인 성향을 가지고 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[4] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_5()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_5()
    question_6()

def question_6():
    global A
    print("\n6. 지금까지 해본 적 없는 경험을 할 때, 불안을 잘 느끼는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[5] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_6()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_6()
    question_7()

def question_7():
    global A, D
    print("\n7. 당신의 부모(양육자)는 당신에게 냉담한 면이 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            D+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[6] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_7()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_7()
    question_8()

def question_8():
    global A
    print("\n8. 인간은 무슨 일이 생겼을 떄 배신하거나 믿을 수 없는 존재라고 생각하십니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[7] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_8()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_8()
    question_9()

def question_9():
    global A, D
    print("\n9. 당신의 부모(양육자)는 당신을 평가해주기보다 비판적인 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            D+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[8] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_9()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_9()
    question_10()

def question_10():
    global A, B, D
    print("\n10. 어린 시절의 추억은 즐거웠던 일이 슬펐던 일보다 더 많습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            B+=1
            D+=1
        elif answer == 3:
            answer_3[9] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_10()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_10()
    question_11()

def question_11():
    global A, B, D
    print("\n11. 당신의 부모(양육자)에게 정말 감사하고 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            B+=1
            D+=1
        elif answer == 3:
            answer_3[10] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_11()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_11()
    question_12()

def question_12():
    global A, B, D
    print("\n12. 힘든 일이 있을 때 부모나 가족을 생각하면 마음이 진정됩니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            B+=1
            D+=1
        elif answer == 3:
            answer_3[11] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_12()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_12()
    question_13()

def question_13():
    global A, B
    print("\n13. 옆에 없게 되었어도 그 사람을 오랫동안 계속해서 생각하는 편입니까? 아니면 다음 사람을 곧바로 찾는 편입니까?")
    print("'그사람을 계속 생각하는 편이다'일 경우 1, '다음 사람을 찾는 편이다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            B+=1
        elif answer == 3:
            answer_3[12] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_13()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_13()
    question_14()

def question_14():
    global B
    print("\n페이지 II")
    print("14. 좋고 싫은 구분이 명확한 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[13] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_14()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_14()
    question_15()

def question_15():
    global B
    print("\n15. 정말 좋은 사람이라고 생각했는데, 환멸을 느끼거나 싫어진 적이 있습니까?")
    print("'자주 있다'일 경우 1, '거의 없다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[14] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_15()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_15()
    question_16()

def question_16():
    global B
    print("\n16. 자주 화가 나거나 침울해지는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[15] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_16()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_16()
    question_17()

def question_17():
    global B
    print("\n17. 자신에게는 장점이 거의 없다고 생각한 적이 있습니까?")
    print("'자주 있다'일 경우 1, '거의 없다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[16] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_17()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_17()
    question_18()

def question_18():
    global B
    print("\n18. 거절당할까 봐 불안한 적이 있습니까?")
    print("'자주 있다'일 경우 1, '거의 없다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[17] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_18()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_18()
    question_19()

def question_19():
    global B
    print("\n19. 좋은 점보다 나쁜 점을 더 신경 쓰는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[18] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_19()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_19()
    question_20()

def question_20():
    global B
    print("\n20. 스스로에게 자신감을 갖고 있는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            B+=1
        elif answer == 3:
            answer_3[19] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_20()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_20()
    question_21()

def question_21():
    global B
    print("\n21. 다른 사람에게 기대지 않고 결단하거나 행동할 수 있는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            B+=1
        elif answer == 3:
            answer_3[20] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_21()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_21()
    question_22()

def question_22():
    global A, B
    print("\n22. 자신은 다른 사람에게 그다지 사랑받지 못하는 존재라고 생각하십니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[21] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_22()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_22()
    question_23()

def question_23():
    global A, B
    print("\n23. 무슨 안 좋은 일이 생기면 하던 일을 자꾸 미루는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[22] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_23()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_23()
    question_24()

def question_24():
    global A, B, D
    print("\n24. 당신의 부모(양육자)로부터 상처받은 적이 자주 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
            D+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[23] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_24()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_24()
    question_25()

def question_25():
    global A, B, D
    print("\n25. 당신의 부모(양육자)에 대해 분노나 원망을 느낀 적이 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
            D+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[24] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_25()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_25()
    question_26()

def question_26():
    global C
    print("\n페이지 III")
    print("26. 힘들 때 친한 사람과 자주 만나려고 노력하는 편입니까, 아니면 힘들수록 만나지 않으려고 하는 편입니까?")
    print("'만나려고 한다'일 경우 1, '만나려고 하지 않는다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[25] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_26()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_26()
    question_27()

def question_27():
    global C
    print("\n27. 친밀한 대인 관계는 당신에게 중요합니까?")
    print("'정말 중요하다'일 경우 1, '그다지 중요하지 않다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[26] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_27()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_27()
    question_28()

def question_28():
    global C
    print("\n28. 늘 냉정하고 쿨한 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[27] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_28()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_28()
    question_29()

def question_29():
    global C
    print("\n29. 끈적끈적한 만남은 질색입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[28] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_29()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_29()
    question_30()

def question_30():
    global C
    print("\n30. 알던 사람과 헤어져도 금방 잊는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[29] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_30()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_30()
    question_31()

def question_31():
    global C
    print("\n31. 다른 사람과의 만남보다 자신의 세계가 더 중요합니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[30] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_31()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_31()
    question_32()

def question_32():
    global C
    print("\n32. 자신의 능력만을 믿습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[31] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_32()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_32()
    question_33()

def question_33():
    global C
    print("\n33. 지나간 일은 별로 그리워하지 않은 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[32] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_33()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_33()
    question_34()

def question_34():
    global C
    print("\n34. 표정에 감정을 잘 드러내지 않는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[33] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_34()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_34()
    question_35()

def question_35():
    global C
    print("\n35. 연인이나 배우자에게도 사생활은 간섭 받고 싶지 않습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[34] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_35()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_35()
    question_36()

def question_36():
    global C
    print("\n36. 친한 사람과 살갗이 닿거나 포옹 같은 스킨십을 좋아하십니까? 아니면 그다지 좋아하지 않습니까?")
    print("'좋아하는 편이다'일 경우 1, '그다지 좋아하지 않는다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[35] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_36()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_36()
    question_37()

def question_37():
    global C
    print("\n37. 어린 시절의 일을 잘 기억하는 편입니까, 아니면 별 기억이 없는 편입니까?")
    print("'잘 기억하고 있다'일 경우 1, '별 기억이 없다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[36] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_37()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_37()
    question_38()

def question_38():
    global A, B
    print("\n38. 친한 사람과 있을 때도 신경 써서 예의를 갖추는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            A+=1
        elif answer == 3:
            answer_3[37] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_38()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_38()
    question_39()

def question_39():
    global A, C
    print("\n39. 곤란에 처했을 때 타인은 친절하게 도와주는 존재라고 생각하십니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[38] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_39()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_39()
    question_40()

def question_40():
    global A, C
    print("\n40. 타인의 선의를 부담 없이 받아들이는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            A+=1
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[39] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_40()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_40()
    question_41()

def question_41():
    global C
    print("\n41. 실패가 두려워 도전을 피해버린 적이 있습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            pass
        elif answer == 3:
            answer_3[40] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_41()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_41()
    question_42()

def question_42():
    global B, C
    print("\n42. 누군가와 헤어질 때 정말 슬프거나 동요하는 편입니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            B+=1
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[41] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_42()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_42()
    question_43()

def question_43():
    global B, C
    print("\n43. 타인의 간섭 없이 혼자 자유롭게 살아가는 게 좋습니까?")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            B+=1
        elif answer == 3:
            answer_3[42] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_43()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_43()
    question_44()

def question_44():
    global B, C
    print("\n44. 당신에게는 일과 학업, 연애와 대인 관계 어느 쪽이 더 중요합니까?")
    print("'일과 학업'일 경우 1, '연애와 대인 관계'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            C+=1
        elif answer == 2:
            B+=1
        elif answer == 3:
            answer_3[43] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_44()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_44()
    question_45()

def question_45():
    global A, B, C, D
    print("\n45. 당신이 상처받았거나 침울해 있을 때 다른 사람이 위로해주거나 이야기를 들어주는 것이 얼마나 중요합니까?")
    print("'정말 중요하다'일 경우 1, '별로 중요하지 않다'일 경우 2, '어느 쪽이라고도 할 수 없다'일 경우 3을 입력해주세요.")
    try:
        answer = int(input('답변: '))
        if answer == 1:
            pass
        elif answer == 2:
            C+=1
        elif answer == 3:
            answer_3[44] = 1
        else:
            print("잘못된 답변입니다.\n")
            question_45()
    except ValueError:
        print("잘못된 답변입니다.\n")
        question_45()
    return A, B, C, D
