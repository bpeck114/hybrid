# FILE script_master.py
# For running multiple hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

import script_lgs

output_file_lgs0 = "15as0S_30km60asR_lgs_mcao_study1A"
master_file_lgs0 = "A_mcao_hybrid.conf"
n_sodium = 0
n_rayleigh = [0, 2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs0 = True

script_lgs.main(output_file=output_file_lgs0, master_file=master_file_lgs0, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs0)

output_file_lgs1 = "15as1S_30km60asR_lgs_mcao_study1A"
master_file_lgs1 = "A_mcao_hybrid.conf"
n_sodium = 1
n_rayleigh = [0, 2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs1 = True

script_lgs.main(output_file=output_file_lgs1, master_file=master_file_lgs1, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs1)

output_file_lgs2 = "15as2S_30km60asR_lgs_mcao_study1A"
master_file_lgs2 = "A_mcao_hybrid.conf"
n_sodium = 2
n_rayleigh = [0, 2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs2 = True

script_lgs.main(output_file=output_file_lgs2, master_file=master_file_lgs2, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs2)

output_file_lgs3 = "15as3S_30km60asR_lgs_mcao_study1A"
master_file_lgs3 = "A_mcao_hybrid.conf"
n_sodium = 3
n_rayleigh = [0, 2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs3 = True

script_lgs.main(output_file=output_file_lgs3, master_file=master_file_lgs3, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs3)

output_file_lgs4 = "15as4S_30km60asR_lgs_mcao_study1A"
master_file_lgs4 = "A_mcao_hybrid.conf"
n_sodium = 4
n_rayleigh = [0, 2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs4 = True

script_lgs.main(output_file=output_file_lgs4, master_file=master_file_lgs4, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs4)




#import script_height

#output_file_height = "4S1R1T_height_study1A"
#master_file_height = "A_hybrid.conf"
#angle_degrees = 30
#height = np.array([20, 22, 24, 26, 28, 30]) #km
#run_simulation_height = True

#script_height.main(output_file=output_file_height, master_file=master_file_height, angle_degrees=angle_degrees, height=height, run_simulation=run_simulation_height)

#import script_radius

#output_file_radius = "4S4R3T_radius_study1A"
#master_file_radius = "A_hybrid.conf"
#radius = np.array([5, 10, 15, 25, 35, 45, 55, 60]) #km
#run_simulation_radius = True

#script_radius.main(output_file=output_file_radius, master_file=master_file_radius, radius=radius, run_simulation=run_simulation_radius)