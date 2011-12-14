import sys
import math

def scaling_lipid(inputfile, outputfile, atomtypesfile):
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

             atomtypes_list=file(atomtypesfile)             
             while j<=134:
                 line_head='ATOM  '+mol[j][6:12]
                 line_tail=mol[j][16:17]+'POPC'+mol[j][21:]
                 atomtypes=(atomtypes_list.readline()).strip('\n')
                 if len(atomtypes)==1:
                     line_atom=' '+atomtypes+'  '
                 elif len(atomtypes)==2:
                     line_atom=' '+atomtypes+' '
                 else:
                     line_atom=atomtypes.rjust(4)
                 line_new=line_head+line_atom+line_tail
                 f_new.write(line_new)
                 j=j+1
         continue 
          
     f_new.write(line)
     
scaling_lipid(sys.argv[1], sys.argv[2], sys.argv[3])
