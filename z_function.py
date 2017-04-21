"abad*****'aba'bad - плохой пример, когда нужен выход за окно"

def z_function(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        x = min(z[i-left], right - i +1) if i <= right else 0
        while i + x < n and s[x] == s[i + x]:
            x += 1
        z[i] = x
        if i + x - 1 > right:
            left, right = i, i + x - 1
    return z
print(' '.join(map(str, z_function(input()))))