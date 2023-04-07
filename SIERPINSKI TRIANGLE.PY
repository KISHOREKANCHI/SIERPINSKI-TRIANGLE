'''
1) Choose three points to form a triangle, which will be our main points.
2) Select one random point inside the triangle.
3) Plot a point that is equidistant from the random point and any of the main points.
4) Repeat step 3 using the new point as the random point and any of the main points.
5) Continue step 4 for a set number of iterations to create a Sierpinski triangle.

'''
import random as ra
import matplotlib.pyplot as plt

lower=int(input("Select least random value : "))
upper=int(input("Select highest random value : "))
def random():
    return ra.randint(lower,upper)
    # return ra.randint(0,500)


main_points=[]
for i in range (3):
    temp=[]
    temp.append(random())
    temp.append(random())
    main_points.append(temp)



def triangle(main_points):
    a=main_points[0]
    b=main_points[1]
    c=main_points[2]
    if (b[1]-a[1])/(b[0]-a[0])==(c[1]-b[1])/(c[0]-b[0]):
        return False
    else:
        return True

while triangle(main_points) is False:
    temp=[]
    temp.append(random())
    temp.append(random())
    main_points.pop()
    main_points.append(temp)

a,b,c=main_points[0],main_points[1],main_points[2]
plt.scatter(a[0],a[1],color='green')
plt.scatter(b[0],b[1],color='green')
plt.scatter(c[0],c[1],color='green')
main_area=(a[0]*(b[1]-c[1]))+(b[0]*(c[1]-a[1]))+(c[0]*(a[1]-b[1]))

def area(point):
    x1,y1=a[0],a[1]
    x2,y2=b[0],b[1]
    x3,y3=c[0],c[1]
    x,y=point[0],point[1]
    u = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    v = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    w = 1 - u - v
    if u>0 and v>0 and w>0:
        return True

def loop(point,n):
    if n<1:
        return
    temp=[]
    x=ra.choice(main_points)
    mid1=(x[0]+point[0])/2
    mid2=(x[1]+point[1])/2
    plt.scatter(mid1,mid2,color='black',s=5)
    temp.append(mid1)
    temp.append(mid2)
    loop(temp,n-1)

n=int(input("Enter no of iterations : "))

def ran():
    point=[]
    point.append(random())
    point.append(random())
    if area(point) is True:
        temp=[]
        mid1=(a[0]+point[0])/2
        mid2=(a[1]+point[1])/2
        plt.scatter(mid1,mid2,color='black',s=5)
        temp.append(mid1)
        temp.append(mid2)
        if n>0:
            loop(temp,n)
        else:
            print("No of iteration should be greater than 0")
            return
    else:
        ran()

ran()

plt.show()
