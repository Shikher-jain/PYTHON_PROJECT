# https://github.com/Shikher-jain/Shikher-jain/blob/main/.ipynb_checkpoints/classMatplotlib-checkpoint.ipynb#L48

from matplotlib import markers
import matplotlib.pyplot as plt

S_x=[2.0, 2.2, 3.6, 5.0, 5.2, 3.6, 2.0, 2.2, 3.6, 5.00, 5.2]
S_y=[2,   0.75, 0,  0.75, 2,   3,   4,  5.25, 6,  5.25,  4]

O_x=[0,0,2,4,4,2,0]
O_y=[1,5,6,5,1,0,1]

R_x=[0,0,2,2.75,2.75,2,0,3 ]#,3.6,5.2,5.2,0,0]
R_y1=[0, 5, 5,  4,   3,      2,   2 ,0  ]#5,4,3,2.5,3.75]
R_y2=[0, 5, 5, 3.75, 3.5, 2.5, 2.5  ,0]#5,4,3,2.5,3.75]

Y_x=[1,5,2.5,0]
Y_y=[1,5,2.5,5]

T_x=[2.5,2.5,0,5]
T_y=[0,5,5,5]

A_x=[0,2.5,4,1,4,5]
A_y=[0,5,  2,2,2,0]

U_x=[0,0,2,4,4]
U_y=[5,1,0,1,5]


fig, ax=plt.subplots(2,5)
ax[0,0].plot(R_x,R_y2,linewidth=5)  #R
ax[0,1].plot(Y_x,Y_y,linewidth=5)   #Y
ax[0,2].plot(O_x,O_y,linewidth=5)   #O
ax[0,3].plot(U_x,U_y,linewidth=5)   #U
ax[0,4].plot(R_x,R_y1,linewidth=5)  #R
ax[1,0].plot(S_x,S_y,linewidth=5)   #S
ax[1,1].plot(T_x,T_y,linewidth=5)   #T
ax[1,2].plot(A_x,A_y,linewidth=5)   #A
ax[1,3].plot(R_x,R_y2,linewidth=5)  #R

ax[1,4].plot([0,0,5,5,0],[0,5,5,0,0],linewidth=2.5,c="y")

ax[1,4].scatter([1.25,3.75],[3.5,3.5],s=[300,300],c="k")
ax[1,4].scatter([2.5],[2.5],s=200,c="tan",marker="^")
ax[1,4].scatter([1.25,2.5,3.75],[3.5,2.5,3.5],s=[100,0,100],c=["w","tan","w"])
ax[1,4].plot([0,2.5,5],[1,2,1],linewidth=5,c="r")


ax[1,4].plot([0,  0, 2.5, 5,  5],
             [1, 1.5, 2, 1.5, 1],linewidth=5,c="r")
ax[1,4].grid(True,color="pink")
plt.show()

