result = []

def divider(a, b):
    if a < b:
        raise ValueError("a is less than b")
    if b > 100:
        raise IndexError("b is greater than 100")
    return a / b

# Виправимо дані, замінимо [] на кортеж, який може бути ключем
data = {10: 2, 2: 5, "123": 4, 18: 0, (1,): 15, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])  # Перетворюємо ключ на int для функції
        result.append(res)
    except Exception as e:
        print(f"Error with key={key}, value={data[key]}: {e}")

print("Result:", result)