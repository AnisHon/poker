import random
import matplotlib.pyplot as plt
import numpy as np



t = {}

t[1, 2] = 1
t[2, 3] = 2
print(t.keys())


exit(0)
random_random = random.Random()

def shuffle(array: list):
    end_index = len(array) - 1
    for _ in range(len(array)):
        rand_index = random_random.randint(0, end_index)
        array[end_index], array[rand_index] = array[rand_index], array[end_index]
        end_index -= 1

def simple_shuffle(array: list):
    for i in range(len(array) // 2):
        j = random_random.randint(0, len(array) - 1)
        array[i], array[j] = array[j], array[i]




alist = ['1', '2', '3', '4', '5']
shuffle(alist)

print(alist)

for i in range(5):
    counter = {}
    for _ in range(100000):
        alist = ['1', '2', '3', '4', '5']
        shuffle(alist)
        s = "".join(alist)
        counter[s] = counter.get(s, 0) + 1

    keys = np.array(list(counter.keys()))
    values = np.array(list(counter.values()))

    plt.figure(figsize=(10, 60))  # 调整宽度和高度
    plt.title("my implement")
    plt.barh(keys, values, height=0.5)
    plt.show()
    print("--advance-shuffle--")
    print("expectation:", values.mean())
    print("variance", values.var())

    counter = {}
    for _ in range(100000):
        alist = ['1', '2', '3', '4', '5']
        random.shuffle(alist)
        s = "".join(alist)
        counter[s] = counter.get(s, 0) + 1

    keys = np.array(list(counter.keys()))
    values = np.array(list(counter.values()))

    plt.figure(figsize=(10, 60))  # 调整宽度和高度
    plt.title("std lib")
    plt.barh(keys, values, height=0.5)
    plt.show()
    print("--std-shuffle--")
    print("expectation:", values.mean())
    print("variance", values.var())



    counter = {}
    for _ in range(100000):
        alist = ['1', '2', '3', '4', '5']
        simple_shuffle(alist)
        s = "".join(alist)
        counter[s] = counter.get(s, 0) + 1

    keys = np.array(list(counter.keys()))
    values = np.array(list(counter.values()))

    plt.figure(figsize=(10, 60))  # 调整宽度和高度
    plt.title("std lib")
    plt.barh(keys, values, height=0.5)
    plt.show()
    print("--simple-shuffle--")
    print("expectation:", values.mean())
    print("variance", values.var())
