def find_palindrome_substrings(s):
    if len(s)==0:
        return 0
    b=1
    a=0
    c=[]
    for i in range(len(s)):
        if i-b >=1 and s[i-b-1:i+1]==s[i-b-1:i+1][::-1]:
            c.append(s[i-b-1:i+1])
            a=i-b-1
            b+=2
            continue

        if i-b >=0 and s[i-b:i+1]==s[i-b:i+1][::-1]:
            c.append(s[i-b-1:i+1])
            a=i-b
            b+=1
    return c
print(find_palindrome_substrings("maadaam"))