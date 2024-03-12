import cmath

def solve_incomplete_quadratic_equation(c):
    x1 = cmath.sqrt(-c)
    x2 = -cmath.sqrt(-c)
    return x1, x2

# Ввод свободного члена уравнения
c = float(input("Введите свободный член c: "))

# Решение уравнения
roots = solve_incomplete_quadratic_equation(c)

# Вывод корней уравнения
print("Корни уравнения:")
for i, root in enumerate(roots):
    print(f"x{i+1} =", root)
