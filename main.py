from calculator import sum_py,sub_py
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(sum_py('15', 15))
except AssertionError as e:
    print(f'invalid account: {e}')

try:
    print(sub_py(5, -5))
except AssertionError as e:
    print(f'invalid account: {e}')