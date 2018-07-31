import time
xRange=range(-50,50)
yRange=range(-50,50)
zRange=range(-50,50)
def equation1(x,y,z):
    #Put the fucntion in this line
    func = 4*x+5*y-6*z
    return func
total1 = 2
def equation2(x,y,z):
    #Put the function in this line
    func = -3*x-2*y+7*z
    return func
total2 = -15
def equation3(x,y,z):
    #Put the function in this line
    func = -x+4*y+2*z
    return func
total3 = -13
start = time.time()
for x in xRange:
    for y in yRange:
        for z in zRange:
            if equation1(x,y,z) is total1:
                if equation2(x,y,z) is total2:
                    if equation3(x,y,z) is total3:
                        finalx=x
                        finaly=y
                        finalz=z
                        break
end = time.time()		
				
print('({0},{1},{2})'.format(finalx,finaly,finalz))
print((end-start)*1000,' ms elapsed')
