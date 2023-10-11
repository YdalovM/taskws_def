# def distance(x1, x2, y1, y2):
#     res = (abs(x1 - x2)**2 + abs(y1 - y2)**2)*0.5
#     return (res)
# x1 = int(input()); x2 = int(input()); y1 = int(input()); y2 = int(input())
# print(distance(x1, x2, y1, y2))

# def power(a, n):
#     res = 1
#     if a > 0:
#         for i in range(n):
#             res += a
#     elif n < 0:
#         for i in range(-n):
#             res /= a
#     return res
# a = float(input())
# n =  int(input())
# print(power(a,n))


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(int(input())))

# def is_yer_lear(x):
#     if x % 4 == 0:
#         return True
#     else:
#         return False
# x = int(input())
# print(is_yer_lear(x))

# def square(x):
#     return 4 * x, x * x, int(x * 2 ** 0.5)
# x = int(input())
# print(square(x))

# def season(x):
#     if x < 3 or x == 12:
#         return ('зима')
#     if x > 2 and x < 6:
#         return ('весна')
#     if x > 5 and x < 9:
#         return ('лето')
#     else:
#         return ('осень')
#
# x = int(input())
# print(season(x))

# def bank(su, year):
#     for i in range(year):
#         su += su / 10
#     return (su)
# su = int(input()); year = int(input())
# print(bank(su, year))

# def is_prime(a):
#     if a % a == 0 and a != 0:
#         return True
#     else:
#         return False
#
# a = int(input())
# print(is_prime(a))

# def check_date(d, m, y):
#     if d < 0 or m < 0 or y < 0:
#         return False
#     mon=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if y % 400 == 0 or ((y % 4 == 0) and (y % 100 != 0)):
#         mon[1] = 29
#     if m >= 1 and m <= 12:
#        if d > 0 and d <= mon[m-1]:
#            return True
#     return False
# d, m, y = int(input()), int(input()), int(input())
# print(check_date(d, m, y))
