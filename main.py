import random
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def dot_prod(A,B,C): #Ax,Ay,Bx,By,Cx,Cy):
    #Find the vector components
    BAx = B[0] - A[0]   #Bx-Ax
    BAy = B[1] - A[1]   #By-Ay
    BCx = C[0] - B[0]   #Cx-Bx
    BCy = C[1] - B[1]   #Cy-By

    #Find cross prod
    return BAx*BCy-BAy*BCx

def draw_ranch(coords,iteration,fail):
    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

    verts = [
        (coords[0][0], coords[0][1]), # left, bottom
        (coords[3][0], coords[3][1]), # left, top
        (coords[2][0], coords[2][1]), # right, top
        (coords[1][0], coords[1][1]), # right, bottom
        (0., 0.), # ignored
        ]

    path = Path(verts, codes)


    fig = plt.figure()
    plt.axhline(y=1, xmin=0, xmax=2, linewidth=1, color = 'k', linestyle='dashed')
    plt.axvline(x=1, ymin=0, ymax=2, linewidth=1, color = 'k', linestyle='dashed')
    ax = fig.add_subplot(111)
    if fail:
        patch = patches.PathPatch(path, ec='r', facecolor='none', lw=1)
    else:
        patch = patches.PathPatch(path, ec='g', facecolor='none', lw=1)
    ax.add_patch(patch)
    xs, ys = zip(*verts[0:4])
    
    ax.plot(xs, ys, 'x', lw=2, color='black', ms=10)
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)

    plt.savefig(str(iteration)+'.png')
    #plt.show()
    plt.clf()
    plt.close()
    return


def check_convexity(coordinates,iteration):
    got_neg = False
    got_paws = False
    num_families = len(coordinates)
    for i in range(0,num_families):
        sign = dot_prod(coordinates[i],coordinates[(i+1)%num_families],coordinates[(i+2)%num_families])
        if sign > 0:
            got_paws = True
        else:
            got_neg = True

        #Draw and show data if you want
        #if (got_paws & got_neg):
            #print(coord1," ",coord2," ",coord3)
            #print(sign," ",got_paws," ",got_neg)
        #draw_ranch(coordinates,iteration,(got_paws & got_neg))
    return got_paws & got_neg #Returns false if they were all the same sign

def run_tests(iterations):
    num_convex = 0
    total = 0
    for j in range(0,iterations):
        coords = [[random.random(),random.random()],[random.random()+1,random.random()],[random.random()+1,random.random()+1],[random.random(),random.random()+1]]
        num_convex = check_convexity(coords,j) + num_convex
        total = total + 1
    return float(num_convex/total)

print(run_tests(10000000))

