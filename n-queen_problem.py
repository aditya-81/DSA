# import time
# new_time = time.time()
n = int(input("Enter value of n: "))
x = [-1] * (n+1)


def place(k, j) -> bool:
    for i in range(1, k):
        if ((x[i] == j) or (abs(i - k) == abs(x[i] - j))):
            return False
    return True

def nqueen(k, n):
    global x
    for j in range(1, n + 1):
        if place(k, j):
            x[k] = j
            if (k == n):
                print(x[1:])
                print("=" * 50)


            else:
                nqueen(k + 1, n)


def func_caller(n):
    nqueen(1, n)


if __name__ == '__main__':
    func_caller(n)
    # print(f"time taken : {time.time() - new_time} seconds")