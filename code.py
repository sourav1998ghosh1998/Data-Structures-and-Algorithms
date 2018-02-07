for i in range(int(input())):
    s = str(input())
    count = 0
    for j in range(len(s)):

        if s[j]=='c' or s[j]=='h' or s[j]=='e' or s[j]=='f':
            if set(s[j:j + 4]) != {'c', 'h', 'e', 'f'}:
              continue
            else:
                count = count + 1

    if count==0:
            print("normal")
    else:
          print("lovely", count)