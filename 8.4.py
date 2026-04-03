import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Дані з умови
INPUT_A = [3, 1, 4, 1, 5, 0, 3, 2, 4, 2]
N = len(INPUT_A)
K = 5 

def draw_array(ax, y_pos, name, data, indices=None, title=None):
    size = len(data)
    cell_w, cell_h = 1.0, 1.0
    ax.text(-0.5, y_pos + 0.5, name, va='center', ha='right', fontsize=12, fontweight='bold')
    if title:
         ax.text((size * cell_w) / 2, y_pos + 2.2, title, va='center', ha='center', fontsize=13, fontweight='bold')

    for i in range(size):
        val = data[i]
        facecolor = 'white' if val is not None else '#E0E0E0'
        rect = patches.Rectangle((i * cell_w, y_pos), cell_w, cell_h, linewidth=1, edgecolor='black', facecolor=facecolor)
        ax.add_patch(rect)
        if val is not None:
            ax.text(i * cell_w + 0.5, y_pos + 0.5, str(val), va='center', ha='center', fontsize=11)
        idx_text = str(indices[i] if indices else i)
        ax.text(i * cell_w + 0.5, y_pos + 1.3, idx_text, va='center', ha='center', fontsize=9)

def get_state_after_iterations(steps):
    # 1. Рахуємо кількості
    C = [0] * (K + 1)
    for x in INPUT_A: C[x] += 1
    # 2. Робимо префіксні суми (позиції)
    for i in range(1, len(C)): C[i] += C[i-1]
    
    # 3. Розстановка (імітація кроків)
    B = [None] * N
    # Копіюємо стан С для декрементів
    current_C = list(C)
    for i in range(steps):
        val = INPUT_A[N - 1 - i] # Беремо з кінця
        pos = current_C[val]
        B[pos - 1] = val
        current_C[val] -= 1
    return B, current_C

def main():
    fig, axs = plt.subplots(2, 3, figsize=(16, 9))
    plt.subplots_adjust(wspace=0.3, hspace=0.6)
    
    idx_10 = list(range(1, 11))
    idx_5 = list(range(6))

    # а) Початковий стан
    C_init = [0] * 6
    for x in INPUT_A: C_init[x] += 1
    ax = axs[0, 0]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 2.5, "A", INPUT_A, idx_10, "а) Вхідний масив A")
    draw_array(ax, 0, "C", C_init, idx_5)

    # б) Крок 2: Позиції
    C_pos = list(C_init)
    for i in range(1, 6): C_pos[i] += C_pos[i-1]
    ax = axs[0, 1]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 1, "C", C_pos, idx_5, "б) Крок 2: Позиції")

    # в) Ітерація 1 (Число 2)
    B1, C1 = get_state_after_iterations(1)
    ax = axs[0, 2]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 2.5, "B", B1, idx_10, "в) Розстановка (іт. 1)")
    draw_array(ax, 0, "C", C1, idx_5)

    # г) Після 2 ітерацій (Числа 2, 4)
    B2, C2 = get_state_after_iterations(2)
    ax = axs[1, 0]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 2.5, "B", B2, idx_10, "г) Проміжний стан (іт. 2)")
    draw_array(ax, 0, "C", C2, idx_5)

    # д) Прогрес (Після 5 ітерацій: 2, 4, 2, 3, 0)
    B5, C5 = get_state_after_iterations(5)
    ax = axs[1, 1]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 2.5, "B", B5, idx_10, "д) Прогрес (іт. 5)")
    draw_array(ax, 0, "C", C5, idx_5)

    # е) Фінал
    B_final = sorted(INPUT_A)
    ax = axs[1, 2]; ax.axis('off'); ax.set_xlim(-1, 11); ax.set_ylim(-1, 4)
    draw_array(ax, 1.5, "B", B_final, idx_10, "е) Відсортований масив")

    plt.show()

if __name__ == "__main__":
    main()