def creation(a):
    b = dict()
    for i in a:
        if i != 0 and i != '0' and i != 'O':
            b[a.index(i)] = i
    return b


def sparse_array_sum(a, b):
    vector_sum = dict()
    for i in a:
        if i in b:
            vector_sum[i] = None
            x = int(a[i]) + int(b[i])
            vector_sum[i] = x
    return vector_sum


def main():
    sparse_ar_1 = input("Enter a sparse array: ")
    sparse_ar_2 = input("Enter a spaese array: ")

    n_1_dict = creation(sparse_ar_1)
    n_2_dict = creation(sparse_ar_2)

    vector_sum = sparse_array_sum(n_1_dict, n_2_dict)
    print(vector_sum)
    for i in vector_sum:
        print(f"{'0'*i}{vector_sum[i]}", end='')


if __name__ == '__main__':
    main()
