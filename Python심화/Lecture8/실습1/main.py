import directory.functions as functions
# 절대경로기준
# functions 안에 있는 모든 함수를 실행시킨다
print(functions.add(1, 3))

import directory.functions as func
print(func.add(1, 2))

from directory import functions

print(functions.add(1, 2))

from directory.functions import add
print(add(1, 2))

from directory.functions import * ## 권장 x
print(add(1, CONSTANT))
# 잘 모르는 함수들이 글로벌 네임 스페이스에 포함된다