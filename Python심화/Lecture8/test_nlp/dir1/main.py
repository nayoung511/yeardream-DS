# import dir1.functions1 as functions
# # 절대경로기준
# # functions 안에 있는 모든 함수를 실행시킨다
# print(functions.add(1, 3))

# import dir1.functions1 as func
# print(func.add(1, 2))

# from dir1 import functions1

# print(functions1.add(1, 2))

# from dir1.functions1 import add
# print(add(1, 2))

# from dir1.functions1 import * ## 권장 x
# print(add(1, CONSTANT))
# # 잘 모르는 함수들이 글로벌 네임 스페이스에 포함된다


"""
위는 글로벌로 취급
"""
##########################
import test_nlp.dir1.functions1

import test_nlp.dir1.functions1 as functions
# 절대경로기준
# functions 안에 있는 모든 함수를 실행시킨다
print(functions.add(1, 3))

import test_nlp.dir1.functions1 as func
print(func.add(1, 2))

from test_nlp.dir1 import functions1

print(functions1.add(1, 2))

from test_nlp.dir1.functions1 import add
print(add(1, 2))

from test_nlp.dir1.functions1 import * ## 권장 x
print(add(1, CONSTANT))
# 잘 모르는 함수들이 글로벌 네임 스페이스에 포함된다

###########################
from * import functions1
from ..dir2.functions2 import add
