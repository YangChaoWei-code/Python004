# -*- coding:utf-8 -*-
"""
@author:YCW
@file:diningPhilosophers.py
@time:2020/10/17 20:55
"""

# # 示例代码
# import threading
# class DiningPhilosophers:
#    def __init__(self):
#    pass
# # philosopher 哲学家的编号。
# # pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
# # eat 表示吃面。
# # putLeftFork 和 putRightFork 表示放下左边或右边的叉子。
#    def wantsToEat(self,
#       philosopher,
#       pickLeftFork(),
#       pickRightFork(),
#       eat(),
#       putLeftFork(),
#       putRightFork())

# 使用信号量
from threading import Semaphore
import queue
import threading
import random
import time

class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher, q, eat_times, status):
        super().__init__()
        self.sizelock = Semaphore(4)
        self.locks = [Semaphore(1) for _ in range(5)]
        self.q = q
        self.eat_times = eat_times
        self.philosopher_num = philosopher
        self.status = status
        self.left = self.philosopher_num % len(self.locks)
        self.right = (self.philosopher_num + 1)% len(self.locks)

    def wantsToEat(self, *actions):
        with self.sizelock:
            with self.locks[self.left], self.locks[self.right]:
                [action() for action in actions]

    def run(self):
        current_time = 1
        self.think()
        while current_time <= self.eat_times:
            if not self.status[self.left] and not self.status[self.right]:
                self.wantsToEat(
                    self.pickLeftFork,
                    self.pickRightFork,
                    self.eat,
                    self.putLeftFork,
                    self.putRightFork
                )
                current_time += 1
            self.think()

    def think(self):
        think_time = random.randint(1, 5) / 100
        time.sleep(think_time)

    def pickLeftFork(self):
        self.status[self.left] = True
        self.q.put([self.philosopher_num, 1, 1])
        print(f'philosopher {self.philosopher_num} pickLeftFork')

    def pickRightFork(self):
        self.status[self.right] = True
        self.q.put([self.philosopher_num, 2, 1])
        print(f'philosopher {self.philosopher_num} pickRightFork')

    def eat(self):
        eat_time = random.randint(1, 3) / 100
        time.sleep(eat_time)
        self.q.put([self.philosopher_num, 0, 3])
        print(f'philosopher {self.philosopher_num} eat noodle')

    def putLeftFork(self):
        self.status[self.left] = False
        self.q.put([self.philosopher_num, 1, 2])
        print(f'philosopher {self.philosopher_num} putLeftFork')

    def putRightFork(self):
        self.status[self.right] = False
        self.q.put([self.philosopher_num, 2, 2])
        print(f'philosopher {self.philosopher_num} putRightFork')


def main():
    threads = []
    result = []
    q = queue.Queue()
    eat_times = 5
    status = [False] * 5
    for i in range(5):
        t = DiningPhilosophers(i, q=q, eat_times=eat_times, status=status)
        threads.append(t)


    for t in threads:
        t.start()

    for t in threads:
        t.join()

    while not q.empty():
        result.append(q.get())
    print(len(result))
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(str(result) + '\n')


if __name__ == '__main__':
    main()
