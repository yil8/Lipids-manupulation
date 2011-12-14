import sys
import math

def scale_lipid(argv=sys.argv):
    usage="""\
Usage: scale_lipid -i inputfile -o outputfile -f factor -l layer -c x y z

inputfile:  Lipid file before scaling
outputfile: Lipid file after scaling
factor:     Scaling factor, usually 4.0 for expand and 0.98 for compress
layer:      Chose which layer to scale. The value can only be 'up', 'down', or 'whole'
x:          The x coordinate of the lipid's center
y:          The y coordinate of the lipid's center
z:          The z coordinate of the lipid's center

Note:
Currently, the scale_lipid.py only support POPC pdb file for CHARMM force field, which can be download from
http://www.charmm-gui.org/?doc=archive&lib=lipid_pure

Any questions, please contact liyi@mail.shcnc.ac.cn"""
    if len(argv)!=13:
        print usage
    else:
        i=1
        while i<len(argv)-1:
            if argv[i]=="-i":
                i=i+1
                inputfile=argv[i]
            elif argv[i]=="-o":
                i=i+1
                outputfile=argv[i]
            elif argv[i]=="-f":
                i=i+1
                factor=argv[i]
            elif argv[i]=="-l":
                i=i+1
                layer=argv[i]
            elif argv[i]=="-c":
                i=i+1
                center_x=argv[i]
                i=i+1
                center_y=argv[i]
                i=i+1
                center_z=argv[i]
            else:
                i=i+1
        
        print "inputfile is "+inputfile
        print "outputfile is "+outputfile
        print "factor is "+factor
        print "layer is "+layer
        print "x y z of center is "+center_x+" "+center_y+" "+center_z

        f=file(inputfile)
        mol={}
        i=1
        f_new=open(outputfile, 'w')

        while True:
            line=f.readline()
            if len(line)==0:
                f_new.close()
                break

            if (line[0:4]=='ATOM' or line[0:6]=='HETATM') and line[17:20]=='POP':
                if i<134:
                    mol[i]=line
                    i=i+1
                else:
                    mol[i]=line
                    i=1
                    j=1
                    while j<=134:
                        line_head=mol[j][0:30]
                        line_tail=mol[j][46:]
                        x_new=("%.3f"%(float(mol[j][30:38])+(float(factor)-1)*(float(mol[20][30:38])-float(center_x)))).rjust(8)
                        y_new=("%.3f"%(float(mol[j][38:46])+(float(factor)-1)*(float(mol[20][38:46])-float(center_y)))).rjust(8)
                        line_new=line_head+x_new+y_new+line_tail
                        if layer=='up':
                            if float(mol[20][46:54])>float(mol[134][46:54]):
                                f_new.write(line_new)
                            else:
                                f_new.write(mol[j])
                        elif layer=='down':
                            if float(mol[20][46:54])<float(mol[134][46:54]):
                                f_new.write(line_new)
                            else:
                                f_new.write(mol[j])
                        elif layer=='whole':
                            f_new.write(line_new)
                        else:
                            f_new.write(line_new)
                        j=j+1
                continue
                
            f_new.write(line)
                
scale_lipid(sys.argv)    
    