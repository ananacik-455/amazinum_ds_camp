# Завдання 2: Написати програму, котра приймає на вхід матрицю зі значеннями 1 або 0 (живий або
# мертвий стани) та ітеративно замінює значення в матриці за наступними правилами:
# ● якщо в живої клітини два чи три живих сусіди, то вона лишається жити;
# ● якщо в живої клітини один чи немає живих сусідів, то вона помирає від «самотності»;
# ● якщо в живої клітини чотири та більше живих сусідів, то вона помирає від «перенаселення»;
# ● якщо в мертвої клітини рівно три живих сусіди, то вона оживає.
# Кожна клітинка має вісім сусідів.

# Формат відповіді:
# ● Код програми, котра виводить 7-му ітерацію наступного початкового стану:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import argparse


class System:

    def __init__(self, default=True, h=7, w=7):
        self.default = default
        self.h = h
        self.w = w
        self.generate_cell()

    def generate_cell(self, seed=None):
        if seed:
            np.random.seed(seed)
        if self.default:
            self.cells = np.array([
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 0],
                [1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 0, 1]
            ])
        else:
            self.cells = np.random.randint(0, 2, (self.h, self.w))

        self.frames = np.array([self.cells])
        self.count_max = None
        self.start_counter = 0

    def iterate(self, _):
        # Create counters for System
        iteration = self.start_counter
        self.start_counter += 1

        if self.count_max:
            iteration %= self.count_max
            return self.plot_frame(self.frames[iteration], iteration)

        if iteration == 0:
            return self.plot_frame(self.cells, iteration)

        old_cell = np.copy(self.cells)
        for i in range(len(old_cell)):
            for j in range(len(old_cell[i])):
                n = self.find_neighbours(old_cell, i, j)
                if old_cell[i][j]:
                    if n <= 1 or n >= 4:
                        self.cells[i][j] = 0
                else:
                    if n == 3:
                        self.cells[i][j] = 1

        self.frames = np.append(self.frames, [self.cells], axis=0)

        self.plot_frame(self.cells, iteration)

    def plot_frame(self, cells, i):
        info_message = " Press [space] to stop/continue | Press [r] to recreate matrix \n [q] to quit"
        plt.axis('off')
        plt.title(f"Iteration №{i}\n {info_message}")
        if i == 0:
            plt.title(f'Start position №{i}\n {info_message}')
            return plt.imshow(cells)

        if np.sum(cells) == 0:
            if not self.count_max:
                self.count_max = i + 1
                if anim.running:
                    anim.event_source.stop()
            plt.title(f'System ends on №{i}\n Press [space] to review life cycle\n [q] to quit')

        return plt.imshow(cells)

    def find_neighbours(self, cell, i, j):
        s = 0
        m_h = len(cell)
        m_w = len(cell)

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == dj == 0:
                    continue
                s += cell[(i + di) % m_h, (j + dj) % m_w]
        return s


def on_press(event):
    # space for pause
    if event.key.isspace():
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running ^= True
    # 'r' for recreate system (Doesn't work on default System)
    if event.key == 'r':
        s.generate_cell(np.random.randint(5000))


def str2bool(v):
  #susendberg's function
  return v.lower() in ("yes", "true", "t", "1")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Task 2.\nTake matrix and change values according to the rules'
    )
    parser.add_argument(
        '--d', '-default',
        type=str2bool,
        help="[required] Is default matrix?",
        default=True, required=True
    )
    parser.add_argument(
        '--w', '-width',
        type=int,
        help='Width for random matrix as System',
        default=7
    )
    parser.add_argument(
        '--h', '-height',
        type=int,
        help='Height for random matrix as System',
        default=7
    )
    args = parser.parse_args()

    s = System(default=args.d, h=args.h, w=args.w)
    # s = System(default=True)
    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', on_press)
    anim = animation.FuncAnimation(fig, s.iterate, interval=1000, cache_frame_data=False)
    anim.running = True
    plt.show()
    # to show 7th iteration of default state
    if args.d:
        print(s.frames[7])

        # [[0, 0, 0, 0, 0, 1, 1]
        #  [0, 1, 1, 1, 1, 0, 1]
        #  [0, 1, 1, 1, 1, 0, 1]
        #  [0, 0, 0, 0, 1, 1, 0]
        #  [0, 0, 0, 0, 0, 0, 0]
        #  [0, 0, 1, 1, 0, 0, 0]
        #  [0, 1, 0, 1, 1, 0, 0]]
