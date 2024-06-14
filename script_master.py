# FILE script_master.py
# For running multiple hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

import script_lgs

output_file_lgs11 = "30km60asR_15as11S_lgs_study1A"
master_file_lgs11 = "A_hybrid.conf"
n_sodium = 11
n_rayleigh = [0, 14, 18, 22, 26]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs11 = True

script_lgs.main(output_file=output_file_lgs11, master_file=master_file_lgs11, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs11)



output_file_lgs12 = "30km60asR_15as12S_lgs_study1A"
master_file_lgs12 = "A_hybrid.conf"
n_sodium = 12
n_rayleigh = [0, 14, 18, 22, 26]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs12 = True

script_lgs.main(output_file=output_file_lgs12, master_file=master_file_lgs12, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs12)

output_file_lgs13 = "30km60asR_15as13S_lgs_study1A"
master_file_lgs13 = "A_hybrid.conf"
n_sodium = 13
n_rayleigh = [0, 14, 18, 22, 26]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs13 = True

script_lgs.main(output_file=output_file_lgs13, master_file=master_file_lgs13, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs13)




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