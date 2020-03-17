#!/bin/bash 

#parun -l 5 --TwoPhaseFlow oscillating_cylinder.py -C "" -v -D "R00_initial"
#parun -l 5 --TwoPhaseFlow oscillating_cylinder.py -C "genMesh=True usePUMI=True" -v -D "R01_Adapt"
mpirun -np 4 parun -l 5 --TwoPhaseFlow oscillating_cylinder.py -C "genMesh=True usePUMI=False" -v -D "R00_test_debug"
