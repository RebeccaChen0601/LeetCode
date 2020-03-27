import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    counter, i, j, x = 0, 0, 0, 0
    if (len(s) == 0 and len(t) != 0) or (len(t) == 0 and len(s) != 0) :
        counter = -1
    else:
        end = []
        while i < len(s):    
            if s[i] != t[j]:
                end.append(s[i])
                counter += 1
                i += 1
                continue
            i += 1
            j += 1

        while j < len(t):
            if end[x] != t[j]:
                counter = -1
            x += 1
            j += 1
    
    print(counter)


    