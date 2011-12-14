import sys
import math

def between_lipid(inputfile, outputfile):
    f=file(inputfile)
    f_new=open(outputfile, 'w')
    i=0
    z_sum=0
    
    while True:
        line=f.readline()
        if len(line)==0:
            f_new.close()
            break

        if (line[0:4]=='ATOM' or line[0:6]=='HETATM') and float(line[46:54])<=0 and float(line[46:54])>=-18.5:
            f_new.write(line)
            
between_lipid('md_4_CHARMM.pdb', 'md_4_up.pdb')    
    