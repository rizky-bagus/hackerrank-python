def swap_case(s):
    updated_s = ""
    for char in s:
        if char.isupper():
            updated_s += char.lower()
            
        elif char.islower():
            updated_s += char.upper()
        
        else:
            updated_s += char
            
    return updated_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)