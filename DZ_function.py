# Задача №1
# str_1 = 14, 58, 0, -7, 63
# list_1 = [25, 59, 68, 63, 54]
# print(min(list_1))
# print(min(str_1))

# Задача №2

# def count(num, degree):
#     new_list = []
#     for i in range(len(num)):
#         if degree == 0:
#             nums = 1
#         elif degree < 0:
#             nums = 1 / (num[i] ** (-degree))
#         else:
#             nums = num[i] ** degree
#         new_list.append(nums)
#     return new_list
#
# result = count([2, 3, 4], -1)
# print(result)

# Задача №3
# def last_day(g, m, n):
#     if n != 1:
#         n -=1
#
#     else:
#         if m == 1:
#             n = 31
#             m = 12
#             g -= 1
#         elif m in [5, 7, 8, 10, 12]:
#             n = 30
#             m -= 1
#         elif m in [2, 4, 6, 9, 11]:
#             n = 31
#             m -= 1
#         elif m == 3:
#
#             if g % 4 == 0 and (g % 100 != 0 or year % 400 == 0):
#                 n = 28
#             else:
#                 n = 27
#     return g, m, n
# new_day1 = last_day(2022, 3, 1)
# print(new_day1)
#
# def next_day(g, m, n):
#     if n == 31:
#         if m in [1, 3, 5, 7, 8, 10]:
#             n = 1
#             m += 1
#         elif m == 12:
#             n = 1
#             m = 1
#             g += 1
#     elif n == 30:
#         if m in [4, 6, 9, 11]:
#             n = 1
#             m += 1
#     elif m == 2:
#         if g % 4 == 0 and (g % 100 != 0 or year % 400 == 0):
#             if n == 29:
#                 n = 1
#                 m += 1
#             else:
#                 n += 1
#         elif n == 28:
#             n = 1
#             m += 1
#     else:
#         n += 1
#     return g, m, n
#
# new_day2 = next_day(2024, 12, 31)
# print(new_day2)

# Задача №4
employess = [
    {'name': 'Alice', 'tasks_completed':25, 'quality':0.9},
    {'name': 'Bob', 'tasks_completed':30, 'quality':0.85},
    {'name': 'Charlie', 'tasks_completed':20, 'quality':0.95}
]

def evaluate_performance(employees: list):
    max_rating = 0
    best_employee = None
    min_rating = float('inf')  # Инициализируем минимальный рейтинг бесконечностью
    worst_employee = None

    for employee in employees:
        rating = employee['tasks_completed'] * employee['quality']
        print(f'Рейтинг сотрудников:\n {employee["name"]}: {rating}')
        if rating > max_rating:
            max_rating = rating
            best_employee = employee['name']
        if rating < min_rating:
            min_rating = rating
            worst_employee = employee['name']
    return max_rating, best_employee, min_rating, worst_employee

max_rating, best_employee, min_rating, worst_employee = evaluate_performance(employess)
print(f"\nМаксимальный рейтинг: {max_rating}")
print(f"Лучший сотрудник: {best_employee}")
print(f"\nМинимальный рейтинг: {min_rating}")
print(f"Худший сотрудник: {worst_employee}")