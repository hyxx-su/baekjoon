# 자료구조 수행평가 테스트
import sys   # 빠른 입력을 위해 sys 모듈 사용

n = int(sys.stdin.readline())   # 명령의 개수 입력받기

stack = []   # 스택 자료구조를 빈 리스트로 초기화

# 명령의 개수(n)만큼 반복
for i in range(n):
    command = sys.stdin.readline().split()   # 명령어 한 줄 입력받기 (push X 형태 등)

    # push X : 정수 X를 스택에 삽입
    if command[0] == 'push':
        stack.append(command[1])   # 입력된 정수를 스택에 추가

    # pop : 스택의 가장 위(top)에 있는 정수를 제거하고 출력
    elif command[0] == 'pop':
        if len(stack) == 0:        # 스택이 비어 있다면
            print(-1)              # -1 출력
        else:
            print(stack.pop())     # 스택의 맨 위 원소를 제거하며 출력

    # size : 현재 스택에 들어있는 정수의 개수를 출력
    elif command[0] == 'size':
        print(len(stack))

    # empty : 스택이 비어 있으면 1, 아니면 0 출력
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # top : 스택의 맨 위(top)에 있는 정수를 출력
    elif command[0] == 'top':
        if len(stack) == 0:        # 스택이 비어 있는 경우
            print(-1)              # -1 출력
        else:
            print(stack[-1])       # 스택의 가장 위 원소를 출력 (제거하지 않음)
