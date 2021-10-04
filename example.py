#------objective function
##def test(x):
##    f=np.zeros((x.shape[0],2))
##    f[:,0]=x[:,0]
##    f[:,1]=(1+10*x[:,1])*(1-(x[:,0]/(1+10*x[:,1]))**2-(x[:,0]/(1+10*x[:,1]))*np.sin(2*3.14159*4*x[:,0]))    
##    return f

#----cost estimation --Schaffer function N. 1
def fn1(x):
    rows = x.shape[0]
    f=np.zeros((rows,2))
    for i in range(rows):
        f[i,0] = x[i,0]*x[i,0]
        f[i,1] = (x[i,0] - 2)*(x[i,0] - 2)
    return f
#----cost estimation --Schaffer function N. 2
def fn2(x):
    rows = x.shape[0]
    f=np.zeros((rows,2))
    for i in range(rows):
        if x[i,0] <= 1:
            f[i,0] = -x[i,0]
        elif  x[i,0] > 1 and x[i,0] <= 3:
            f[i,0] = x[i,0] - 2
        elif  x[i,0] > 3 and x[i,0] <= 4:
            f[i,0] = 4 - x[i,0]
        elif  x[i,0] > 4:
            f[i,0] = x[i,0] - 4
        f[i,1] = (x[i,0] - 5)*(x[i,0] - 5)
    return f

n = 1               # number of real-valued design variables
bo1 = [-5]    # lower boundary of all variables. [0,0] also works.
bo2 = [10]      # upper boundary of all variables. [1,1] also works.
g=100               # number of generations
p=40                # size of population         
ap=25               # size of archive population (archive consists of the elites in population)
mp=.1               # mutation probability (0<=mp<1)
