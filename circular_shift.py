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

def find_sub(s, sub):
    working_string = sub + '#' + s
    z_working_string = z_function(working_string)
    sub_pos = []
    for item in range(len(z_working_string)):
        if z_working_string[item] == len(sub):
            sub_pos.append(item - len(sub) - 1)
    if len(sub_pos) != 0:
        return sub_pos
    else:
        return [-1]

def circular_shift_left(s, sub):
    working_string = s + s
    return find_sub(working_string, sub)[0]

s = input()
sub = input()
print(circular_shift_left(s, sub))