#!/bin/bash

#mpirun -np 4 parun dambreak_Colagrossi_so.py -l1 -v -C "gen_mesh=False usePUMI=False adapt=0" -D "R00_closure0_parallel"
#mpirun -np 4 parun dambreak_Colagrossi_so.py -l1 -v -C "gen_mesh=False usePUMI=False adapt=0" -D "R01_closure2_parallel"
mpirun -np 4 parun dambreak_Colagrossi_so.py -l1 -v -C "gen_mesh=False usePUMI=False adapt=0" -D "R02_closure2_parallel_fix"

