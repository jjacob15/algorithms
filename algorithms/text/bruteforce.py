def find_brute(T, P):
    n, m = len(T), len(P)
    if n < m:
        return -1
    if n == m:
        return 0 if T == P else -1
    for i in range(n-m+1):
        if (T[i:i+m] == P):
            return i
    return -1


if __name__ == "__main__":
    print(find_brute('jack', 'jack'),0)
    print(find_brute('jackson', 'jack'),0)
    print(find_brute('jaison jack', 'jack'),7)
    print(find_brute('jaison.jack@gmail.com', 'jack'),7)
    print(find_brute('ja', 'jack'), -1)
    print(find_brute('abacaabaccabacabaabb', 'abacab'))
