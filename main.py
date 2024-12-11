import test_function as tf
import diagnosis_function as df
import already_function as af

A = 0
B = 0
C = 0
D = 0
result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
lever = 0

def program_start():
    print("버그가 있을 경우 jkw0527@gachon.ac.kr로 연락 부탁드립니다.")
    print("애착 성향 진단 테스트를 시작하려면 1, 이미 테스트했던 점수를 가지고 결과를 보고싶으시다면 2를 입력해주세요.")
    answer = int(input('답변: '))
    if answer == 1:
        test_start()
    elif answer == 2:
        af.already_test(A, B, C, D)
    else:
        print("잘못된 답변입니다.\n")
        program_start()

def test_start():
    print("설문을 제외한 대답은 Yes일 경우 1을 입력하시고 No일 경우 2를 입력해주시면 됩니다.")
    print("애착 성향 진단 테스트를 시작하시겠습니까?")
    answer = int(input('답변: '))
    if answer == 1:
        test_check()
    else:
        program_start()

def test_check():
    print("본 테스트는 오카다 다카시의 '나는 왜 혼자가 편할까'를 바탕으로 만들어졌습니다")
    print("실제 공식 테스트와 결과 차이가 있을 수 있으니 맹신하지 마십시오.")
    print("모두 확인하셨습니까?")
    answer = int(input('답변: '))
    if answer == 1:
        question_before()
    else:
        program_start()

def question_before():
    print("총 45문항의 설문입니다.")
    print("설문의 대답이 '네'일 경우엔 1, '아니요'일 경우엔 2, '어느 쪽이라고도 할 수 없다'일 경우엔 3을 입력해주시면 됩니다.")
    print("아래의 질문에 대해 과거 몇 년 동안 자신의 성향을 떠올리며 가장 적합한 것을 선택해주십시오. 다만 '어느 쪽이라고도 할 수 없다'가 너무 많으면 검사의 정밀도가 낮아지므로 주의하십시오.\n")
    tf.question_1()

def exit():
    print("\n")
    input("프로그램을 종료하려면 enter키를 눌러주세요.")


program_start() # 전체 설문조사 실행 or 이미 테스트 했던 점수 기반으로 결과 재확인
A, B, C, D = tf.question_45()

df.diagnosis_run(A, B, C, D, result) # 진단 함수들 실행
df.result_print(lever, result) # 진단한 애착유형을 알려줌

df.primary_attachment(A, B, C, D) # 오름차순으로 정렬한 num_sorted를 기반으로 주된 애착형과 부차적인 애착형을 알려줌
df.num_print() # 각각의 애착형 점수를 알려줌
exit()
