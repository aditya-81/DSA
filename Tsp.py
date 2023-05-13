class Tsp:
    def reduce(self, mat: list):
        counter = 0
        for i in range(len(mat[0])):
            mi = min(mat[i])
            if not mi == float('inf'):
                counter += mi
            for j in range(len(mat[i])):
                mat[i][j] -= mi

        for i in range(len(mat[0])):
            mi = float('inf')
            set_flag = False
            for j in mat:
                if j[i] == 0:
                    set_flag = True
                    break
                else:
                    if mi > j[i]:
                        mi = j[i]
            if not set_flag:
                if not mi == float('inf'):
                    counter += mi
                for j in mat:
                    j[i] -= mi
        print("\nreduction cost", counter)
        print()
        return mat

    def new_node(self, a_mat, i, j):
        a_mat[i] = [float('inf')] * len(a_mat[i])
        for k in range(len(a_mat[0])):
            a_mat[k][j] = float('inf')

        a_mat[j][i] = float('inf')
        return self.reduce(a_mat)


if __name__ == "__main__":
    mat = [[float('inf'), 20, 30, 10, 11],
           [15, float('inf'), 16, 4, 2],
           [3, 5, float('inf'), 2, 4],
           [19, 6, 18, float('inf'), 3],
           [16, 4, 7, 16, float('inf')]
           ]
    obj = Tsp()
    a = obj.reduce(mat)
    print("Reduced Mat:\n")
    print('=' * 80)
    for i in a:
        print(i)
    print('=' * 80)
    print()
    m = obj.new_node(a, 0, 1)
    print('=' * 80)
    print()
    print("for 1->2:")
    for i in m:
        print(i)
    print('=' * 80)
