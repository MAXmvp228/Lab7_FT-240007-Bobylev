# Проверка ввода данных для n
while True:
    try:
        n = int(input("Введите количество критериев: "))
        if n<2:
            print("Количество критериев должно быть больше 1")
            continue
        break
    except ValueError:
        print("Введите числовое значение")


    # Матрица для хранения попарных сравнений
A=[]
for i in range(n):
    A.append([1.0]*n)

print("\nПопарное сравнение критериев (шкала от 1 до 9):")
print("1 - равная важность")
print("3 - умеренное превосходство")
print("5 - сильное превосходство")
print("7 - очень сильное превосходство")
print("9 - абсолютное превосходство")
print("2,4,6,8 - промежуточные значения\n")

# Проверка ввода данных для заполнения матрицы
for i in range(n):
    for j in range(i + 1, n):
         while True:
            try:
                value = float(input(f"Сравнение критерия {i + 1} с критерием {j + 1}: "))
                if value < 1 / 9 or value > 9:
                    print("Значение должно быть от 1/9 до 9")
                    continue
                A[i][j] = value
                A[j][i] = 1.0 / value
                break
            except ValueError:
                print("Введите числовое значение, с точкой разделителем")

# Расчёт общей суммы попарных сравнений
sum=0.0
for i in range(n):
    for j in range(n):
        sum+=A[i][j]

# Расчёт суммы сравнений для одного критерия
for i in range(n):
    linesum=0.0
    for j in range(n):
        linesum += A[i][j]
    print(f'Весовой коэффициент критерия №{i+1} равен {(linesum/sum).__round__(2)}')
