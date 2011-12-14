import sys
import math
import random

def volume(inputfile, outputfile, events):
    f=file(inputfile)
    f_new=open(outputfile, 'w')
    inside=0
    i=0
    mol=[[0 for col in range(5)] for row in range(50000)]

    while True:
        line=f.readline()
        if len(line)==0:
            break
        
        if (line[0:4]=='ATOM' or line[0:6]=='HETATM'):
            i=i+1
            atomtype=((line[12:16]).strip())[0:1]
            if atomtype=='C':
                mol[i][0]='C'
                mol[i][1]=1.70

            elif atomtype=='H':
                mol[i][0]='H'
                mol[i][1]=1.0

            elif atomtype=='O':
                mol[i][0]='O'
                mol[i][1]=1.52

            elif atomtype=='N':
                mol[i][0]='N'
                mol[i][1]=1.55
                
            elif atomtype=='S':
                mol[i][0]='S'
                mol[i][1]=1.80
                
            mol[i][2]=float(line[30:38])
            mol[i][3]=float(line[38:46])
            mol[i][4]=float(line[46:54])
            
    atom_number=i
    i=1
    x_max=mol[1][2]
    x_min=mol[1][2]
    y_max=mol[1][3]
    y_min=mol[1][3]
    z_max=mol[1][4]
    z_min=mol[1][4]
    while i<=atom_number:
        if mol[i][2]>x_max:
            x_max=mol[i][2]
            
        if mol[i][2]<x_min:
            x_min=mol[i][2]
            
        if mol[i][3]>y_max:
            y_max=mol[i][3]
            
        if mol[i][3]<y_min:
            y_min=mol[i][3]
            
        if mol[i][4]>z_max:
            z_max=mol[i][4]
            
        if mol[i][4]<z_min:
            z_min=mol[i][4]
            
        i=i+1

    point_x_max=math.ceil(x_max)+1
    point_x_min=math.ceil(x_min)-1
    point_y_max=math.ceil(y_max)+1
    point_y_min=math.ceil(y_min)-1
    point_z_max=math.ceil(z_max)+1
    point_z_min=math.ceil(z_min)-1
    
    print 'atom_number='+str(atom_number)
    print 'x_max='+str(x_max)+' x_min='+str(x_min)+' y_max='+str(y_max)+' y_min='+str(y_min)+' z_max='+str(z_max)+' z_min='+str(z_min)
    print 'point_x_max='+str(point_x_max)+' point_x_min='+str(point_x_min)+' point_y_max='+str(point_y_max)+' point_y_min='+str(point_y_min)+' point_z_max='+str(point_z_max)+' point_z_min='+str(point_z_min)

    i=1
    while i<=float(events):
        print 'events '+str(i)
        point_x=random.uniform(point_x_min, point_x_max)
        point_y=random.uniform(point_y_min, point_y_max)
        point_z=random.uniform(point_z_min, point_z_max)

        j=1        
        while j<=atom_number:
            distance=((point_x-mol[j][2])**2+(point_y-mol[j][3])**2+(point_z-mol[j][4])**2)**0.5
            radius=mol[j][1]
            if distance<=radius:
                inside=inside+1
                f_new.write(str(point_x)+' '+str(point_y)+' '+str(point_z)+'\n')
                break
            j=j+1
                
        i=i+1
        
    f_new.close()
    print 'events= '+str(events)
    print 'inside= '+str(inside)
    print 'volume= '+str((point_x_max-point_x_min)*(point_y_max-point_y_min)*(point_z_max-point_z_min)*inside/float(events))
                
volume(sys.argv[1], sys.argv[2], sys.argv[3])    
    