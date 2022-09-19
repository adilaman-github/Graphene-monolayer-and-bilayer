#!/bin/bash      
#PBS -N Graphene_Bilayer_AA_w[1.50]
#PBS -q iiser
#PBS -l select=1:ncpus=1      
#PBS -o active.o       
#PBS -e active.err     
#PBS -l walltime=48:00:00  
cd $PBS_O_WORKDIR    


python3.7 Graphene_Bilayer_AA_w[1.50].py
    
