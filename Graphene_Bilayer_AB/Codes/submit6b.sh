#!/bin/bash      
#PBS -N Graphene_Bilayer_AB_w[1.25].py      
#PBS -q ShortQ
#PBS -l select=1:ncpus=1      
#PBS -o active.o       
#PBS -e active.err     
#PBS -l walltime=24:00:00  
cd $PBS_O_WORKDIR    


python3.7 Graphene_Bilayer_AB_w[1.25].py
    
