import sys
import math

def box_lipid(inputfile):
    f=file(inputfile)
    i=0
    P_x=[]
    P_y=[]
    P_z=[]
    P_x_min_sum=0
    P_x_max_sum=0
    P_y_min_sum=0
    P_y_max_sum=0
    P_z_min_sum=0
    P_z_max_sum=0
    volume=0
    P_number=0

    while True:
        line=f.readline()
        if len(line)==0:
            break

        if (line[0:4]=='ATOM' or line[0:6]=='HETATM') and line[17:20]=='POP' and line[13:14]=='P':
            i=i+1
            P_x.append(float(line[30:38]))
            P_y.append(float(line[38:46]))
            P_z.append(float(line[46:54]))

    P_number=i

    P_x.sort()
    P_y.sort()
    P_z.sort()

    i=0
    while i<5:
        P_x_min_sum=P_x_min_sum+P_x[i]
        P_y_min_sum=P_y_min_sum+P_y[i]
        P_z_min_sum=P_z_min_sum+P_z[i]
        i=i+1

    P_x.reverse()
    P_y.reverse()
    P_z.reverse()

    i=0
    while i<5:
        P_x_max_sum=P_x_max_sum+P_x[i]
        P_y_max_sum=P_y_max_sum+P_y[i]
        P_z_max_sum=P_z_max_sum+P_z[i]
        i=i+1

    volume=(P_x_max_sum/5-P_x_min_sum/5)*(P_y_max_sum/5-P_y_min_sum/5)*(P_z_max_sum/5-P_z_min_sum/5)
    print "\n lipid_box x max: "+str(P_x_max_sum/5)+"; x min: "+str(P_x_min_sum/5)
    print "\n lipid_box y max: "+str(P_y_max_sum/5)+"; y min: "+str(P_y_min_sum/5)
    print "\n lipid_box z min: "+str(P_z_max_sum/5)+"; z min: "+str(P_z_min_sum/5)
    print "\n lipid_box volume: "+str(volume)+"; lipid_number: "+str(P_number)
    print "\n volume/lipid: "+str(volume/P_number)

box_lipid(sys.argv[1])    
                    