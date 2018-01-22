import math

def wsp_prostej( p0, p1):
    print ("p0= ",p0)
    print ("p1= ",p1)
    a = (p1[1] - p0[1]) / (p1[0] - p0[0])
    print ("a= ",a)
    return a

def b_prostej( p0, p1):
    b = ((-p0[0]) * (p1[1] - p0[1]) - (p1[0] - p0[0]) * (-p0[1])) / (p1[0] - p0[0])
    print ("b= ",b)
    return b
    
def checkio(data):
    listX = sorted(data)
    listY = sorted(listX)
    for i in range(len(listX)):
        listY[i]=list(reversed(listY[i]))
    listY=sorted(listY)
    listXR = list(reversed(sorted(listX)))
    listYR = list(reversed(sorted(listY)))
    l = []
    x1 = min(data)[0]
    y1 = min(data)[1]
    e=-10
    f=-100

    for i in listX: #////// >
        
        for j in data:
            if len(l)>0:
                if [j[0],j[1]] != data[l[len(l)-1]] and j[0] !=  data[l[len(l)-1]][0]:
                    if e < wsp_prostej( [j[0],j[1]],data[l[len(l)-1]]) and j[0]>i[1]:
                        
                        e=wsp_prostej( [j[0],j[1]],data[l[len(l)-1]])
                        f=b_prostej( [j[0],j[1]],data[l[len(l)-1]])

        if i[1] >= y1 and i[1]>=e*i[0]+f:
            l.append(data.index(i))
            x1=i[0]
            y1=i[1]
            e=-10
            f=-100
        
    e=-10
    f=-100
    for i in listYR: #\\\\\\\\ >      sprawdzic czy nie ma punktów powyzej prostej 
        for j in data:
            if [j[0],j[1]] != data[l[len(l)-1]] and j[0] !=  data[l[len(l)-1]][0]:
                if e < wsp_prostej( [j[0],j[1]],data[l[len(l)-1]]) and j[0]>i[1]:
                    e=wsp_prostej( [j[0],j[1]],data[l[len(l)-1]])
                    f=b_prostej( [j[0],j[1]],data[l[len(l)-1]])
        if i[0] <= y1 and i[1]>x1 and i[0]>=e*i[1]+f:
                
                if data.index(list(reversed(i))) in l:
                    return l

                l.append(data.index(list(reversed(i))))
                x1=i[1]
                y1=i[0]
        e=-10
    e=-10
    f=-100
    for i in listXR: #/////////// <
        
        for j in data:
            if len(l)>0:
                if [j[0],j[1]] != data[l[len(l)-1]] and j[0] !=  data[l[len(l)-1]][0]:
                    if e < wsp_prostej( [j[0],j[1]],data[l[len(l)-1]]) and j[0]<=i[1]: #ZMIANNAANNANANANA > na <=
                        
                        e=wsp_prostej( [j[0],j[1]],data[l[len(l)-1]])
                        f=b_prostej( [j[0],j[1]],data[l[len(l)-1]])
        
        if i[1] < y1 and i[0]<=x1 and i[1]<=e*i[0]+f:
            if data.index(i) in l:
                    return l
                
            l.append(data.index(i))
            x1=i[0]
            y1=i[1]
            e=-10
            f=-100
    for i in listY: 
        if i[0] >= y1 and i[1]<x1 and i[0]<min(data)[1] and i[0] <= i[1]*wsp_prostej( data[l[len(l)-1]],[min(data)[0],min(data)[1]])+b_prostej( data[l[len(l)-1]],[min(data)[0],min(data)[1]]) :
            if min(data)[0]==i[1] and min(data)[1]==i[0]:
                break
            if len(l)==len(data):
                break
            l.append(data.index(list(reversed(i))))
            x1=i[1]
            y1=i[0]
    

    return l
