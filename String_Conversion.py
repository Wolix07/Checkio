def steps_to_convert(line1, line2):
    import string
    lin = ""
    c=0
    if line1 == line2:
        return 0
    if len(line1)==0:
        return len(line2)
    if len(line2)==0:
        return len(line1)
    if len(line1) >= len(line2):
        t = len(line1)
    else:
        t = len(line2)
    j=1
    if len(line2) > len(line1):
        for q in range(len(line2)-len(line1)):
            line1 = line1 + ";"
    for i in range(t):
        if i<len(line1) and i<len(line2):
            if i != len(line2)-1 :
                if line1[i] != line2[i] and line1[i] != line2[i+1]:
                    lin = line1[:i] + line2[i]  + line1[(i+1):]
                    line1=lin
                    c+=1
            else:
                if line1[i] != line2[i]:
                    lin = line1[:i] + line2[i]  + line1[:(i+1)]
                    line1=lin
                    c+=1
    return c
