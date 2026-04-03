import time
import random
import matplotlib.pyplot as plt

def counting_sort(A):
    if not A: return A
    k = max(A)
    n = len(A)
    B = [0] * n
    C = [0] * (k + 1)
    for j in range(n):
        C[A[j]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    return B

def measure_time(data):
    start = time.perf_counter()
    counting_sort(data)
    return time.perf_counter() - start

# Збільшені розміри масивів для більш тривалого сортування
sizes = [5000000, 10000000, 15000000, 20000000, 25000000, 30000000, 35000000]
results = {'best': [], 'average': [], 'worst': []}

print("Починаю вимірювання (це може зайняти трохи часу через великі об'єми)...")
print(f"\n{'Розмір (n)':>12} | {'Найкращий':>10} | {'Середній':>10} | {'Найгірший':>10}")
print("-" * 55)

for n in sizes:
    # Діапазон значень k (також великий)
    k = n // 5 
    
    # Середній випадок
    avg_data = [random.randint(0, k) for _ in range(n)]
    # Найкращий випадок (вже відсортований)
    best_data = sorted(avg_data)
    # Найгірший випадок (зворотний порядок)
    worst_data = best_data[::-1]
    
    t_best = measure_time(best_data)
    t_avg = measure_time(avg_data)
    t_worst = measure_time(worst_data)
    
    results['best'].append(t_best)
    results['average'].append(t_avg)
    results['worst'].append(t_worst)
    
    print(f"{n:12,d} | {t_best:10.4f} | {t_avg:10.4f} | {t_worst:10.4f}")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, results['best'], 'o-', label='Найкращий випадок')
plt.plot(sizes, results['average'], 's-', label='Середній випадок')
plt.plot(sizes, results['worst'], '^-', label='Найгірший випадок')

plt.title('Практична оцінка складності Counting Sort (великі об\'єми)')
plt.xlabel('Кількість елементів (n)')
plt.ylabel('Час виконання (секунди)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()