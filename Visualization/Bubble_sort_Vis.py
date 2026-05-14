import matplotlib.pyplot as plt

arr = [5, 3, 8, 4, 2]
n = len(arr)

fig = plt.figure()
plt.ion()

def show(compare=None, sorted_from=None):
    if not plt.fignum_exists(fig.number):
        return

    colors = ["skyblue"] * n

    if sorted_from is not None:
        colors[sorted_from:] = ["green"] * (n - sorted_from)

    if compare:
        for i in compare:
            colors[i] = "red"

    plt.clf()
    plt.bar(range(n), arr, color=colors)
    plt.title("Bubble Sort Visualization")
    plt.pause(0.5)


for i in range(n):
    for j in range(n - i - 1):
        show(compare=[j, j+1], sorted_from=n-i)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

show(sorted_from=0)
plt.ioff()
plt.show()
