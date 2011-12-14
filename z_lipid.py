import sys
import math

def z_lipid(inputfile):
    f=file(inputfile)
    i=0
    z_sum=0
    mol=[0 for row in range(10000)]
    
    while True:
        line=f.readline()
        if len(line)==0:
            break

        if (line[0:4]=='ATOM' or line[0:6]=='HETATM') and line[13:14]=='P':
            i=i+1
            mol[i]=float(line[46:54])

    atom_number=i
    i=1
    while i<=atom_number:
        z_sum=z_sum+mol[i]
        i=i+1

    print str(z_sum/atom_number)        
             
z_lipid('popc_n512_centered_down.pdb')    
    