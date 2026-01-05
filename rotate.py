
import math
import matplotlib.pyplot as plt
def matrix_multiplication(mat,point):
    result=[0,0,0]
    for i in range (3):
        result[i]=mat[0][i]*point[0]+mat[1][i]*point[1]+mat[2][i]*point[2]
    return result
points=[
    [1,1,1],
    [2,1,1],
    [2,2,1],
    [1,2,1]
] 
theta=math.radians(10)
transformation=[
    [math.cos(theta),-math.sin(theta) ,0],
    [math.sin(theta),math.cos(theta),0],
    [0,0,1]
]
t_points=[matrix_multiplication(transformation,p)for p in points]
plt.plot([points[0][0],points[0][1],points[0][2],points[0][3],points[0][0]],[[points[1][0],points[1][1],points[1][2],points[1][3],points[1][0]]],'red',label='original')
plt.plot([t_points[0][0],t_points[0][1],t_points[0][2],t_points[0][3],t_points[0][0]],[[t_points[1][0],t_points[1][1],t_points[1][2],t_points[1][3],t_points[1][0]]],'blue',label='rorated')
plt.show()