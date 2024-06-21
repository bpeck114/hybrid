# FILE script_master.py
# For running multiple hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

import script_lgs

output_file_lgs0 = "0S_mcao_study1A"
master_file_lgs0 = "A_mcao_hybrid.conf"
n_sodium = 0
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs0 = True

script_lgs.main(output_file=output_file_lgs0, master_file=master_file_lgs0, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs0)



output_file_lgs1 = "1S_mcao_study1A"
master_file_lgs1 = "A_mcao_hybrid.conf"
n_sodium = 1
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs1 = True

script_lgs.main(output_file=output_file_lgs1, master_file=master_file_lgs1, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs1)



output_file_lgs2 = "2S_mcao_study1A"
master_file_lgs2 = "A_mcao_hybrid.conf"
n_sodium = 2
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs2 = True

script_lgs.main(output_file=output_file_lgs2, master_file=master_file_lgs2, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs2)



output_file_lgs3 = "3S_mcao_study1A"
master_file_lgs3 = "A_mcao_hybrid.conf"
n_sodium = 3
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs3 = True

script_lgs.main(output_file=output_file_lgs3, master_file=master_file_lgs3, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs3)



output_file_lgs4 = "4S_mcao_study1A"
master_file_lgs4 = "A_mcao_hybrid.conf"
n_sodium = 4
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs4 = True

script_lgs.main(output_file=output_file_lgs4, master_file=master_file_lgs4, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs4)



output_file_lgs5 = "5S_mcao_study1A"
master_file_lgs5 = "A_mcao_hybrid.conf"
n_sodium = 5
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs5 = True

script_lgs.main(output_file=output_file_lgs5, master_file=master_file_lgs5, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs5)



output_file_lgs6 = "6S_mcao_study1A"
master_file_lgs6 = "A_mcao_hybrid.conf"
n_sodium = 6
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs6 = True

script_lgs.main(output_file=output_file_lgs6, master_file=master_file_lgs6, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs6)



output_file_lgs7 = "7S_mcao_study1A"
master_file_lgs7 = "A_mcao_hybrid.conf"
n_sodium = 7
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs7 = True

script_lgs.main(output_file=output_file_lgs7, master_file=master_file_lgs7, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs7)



output_file_lgs8 = "8S_mcao_study1A"
master_file_lgs8 = "A_mcao_hybrid.conf"
n_sodium = 8
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs8 = True

script_lgs.main(output_file=output_file_lgs8, master_file=master_file_lgs8, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs8)



output_file_lgs9 = "9S_mcao_study1A"
master_file_lgs9 = "A_mcao_hybrid.conf"
n_sodium = 9
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs9 = True

script_lgs.main(output_file=output_file_lgs9, master_file=master_file_lgs9, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs9)



output_file_lgs10 = "10S_mcao_study1A"
master_file_lgs10 = "A_mcao_hybrid.conf"
n_sodium = 10
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs10 = True

script_lgs.main(output_file=output_file_lgs10, master_file=master_file_lgs10, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs10)



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