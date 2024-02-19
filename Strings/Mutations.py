def mutate_string(string, position, character):
    char = list(string)
    char[position] = character
    return ''.join(char)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)