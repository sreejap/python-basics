def safe_modify_string(s: str, index: int, new_char: str) -> str:
    res = [] # is this the way to initialize an empty string 
    for i in range (len(s)):
        
        # res[i] = s[i] , this is wrong
        if i == index:
            res.append(new_char)
            # s [i] = new_char # this is not allowed
        else:
            res.append(s[i])
    return ''.join(res)
    # str(res) # to convert the object into string

if __name__ == "__main__":
    s = input()
    index = int(input())
    new_char = input()
    res = safe_modify_string(s, index, new_char)
    print(res)
