# FILE script_master.py
# For running multiple hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

import script_lgs

output_file_lgs00 = "30km60asR_15as0S_lgs_study1A"
master_file_lgs00 = "A_hybrid.conf"
n_sodium = 0
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs00 = True

script_lgs.main(output_file=output_file_lgs00, master_file=master_file_lgs00, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs00)



output_file_lgs11 = "30km60asR_15as1S_lgs_study1A"
master_file_lgs11 = "A_hybrid.conf"
n_sodium = 1
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs11 = True

script_lgs.main(output_file=output_file_lgs11, master_file=master_file_lgs11, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs11)



output_file_lgs22 = "30km60asR_15as2S_lgs_study1A"
master_file_lgs22 = "A_hybrid.conf"
n_sodium = 2
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs22 = True

script_lgs.main(output_file=output_file_lgs22, master_file=master_file_lgs22, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs22)



output_file_lgs33 = "30km60asR_15as3S_lgs_study1A"
master_file_lgs33 = "A_hybrid.conf"
n_sodium = 3
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs33 = True

script_lgs.main(output_file=output_file_lgs33, master_file=master_file_lgs33, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs33)



output_file_lgs44 = "30km60asR_15as4S_lgs_study1A"
master_file_lgs44 = "A_hybrid.conf"
n_sodium = 4
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs44 = True

script_lgs.main(output_file=output_file_lgs44, master_file=master_file_lgs44, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs44)



output_file_lgs55 = "30km60asR_15as5S_lgs_study1A"
master_file_lgs55 = "A_hybrid.conf"
n_sodium = 5
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs55 = True

script_lgs.main(output_file=output_file_lgs55, master_file=master_file_lgs55, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs55)



output_file_lgs66 = "30km60asR_15as6S_lgs_study1A"
master_file_lgs66 = "A_hybrid.conf"
n_sodium = 6
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs66 = True

script_lgs.main(output_file=output_file_lgs66, master_file=master_file_lgs66, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs66)



output_file_lgs77 = "30km60asR_15as7S_lgs_study1A"
master_file_lgs77 = "A_hybrid.conf"
n_sodium = 7
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs77 = True

script_lgs.main(output_file=output_file_lgs77, master_file=master_file_lgs77, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs77)



output_file_lgs88 = "30km60asR_15as8S_lgs_study1A"
master_file_lgs88 = "A_hybrid.conf"
n_sodium = 8
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs88 = True

script_lgs.main(output_file=output_file_lgs88, master_file=master_file_lgs88, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs88)



output_file_lgs99 = "30km60asR_15as9S_lgs_study1A"
master_file_lgs99 = "A_hybrid.conf"
n_sodium = 9
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs99 = True

script_lgs.main(output_file=output_file_lgs99, master_file=master_file_lgs99, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs99)



output_file_lgs100 = "30km60asR_15as10S_lgs_study1A"
master_file_lgs100 = "A_hybrid.conf"
n_sodium = 10
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs100 = True

script_lgs.main(output_file=output_file_lgs100, master_file=master_file_lgs100, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs100)



output_file_lgs111 = "30km60asR_15as11S_lgs_study1A"
master_file_lgs111 = "A_hybrid.conf"
n_sodium = 11
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs111 = True

script_lgs.main(output_file=output_file_lgs111, master_file=master_file_lgs111, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs111)



output_file_lgs122 = "30km60asR_15as12S_lgs_study1A"
master_file_lgs122 = "A_hybrid.conf"
n_sodium = 12
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs122 = True

script_lgs.main(output_file=output_file_lgs122, master_file=master_file_lgs122, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs122)



output_file_lgs133 = "30km60asR_15as13S_lgs_study1A"
master_file_lgs133 = "A_hybrid.conf"
n_sodium = 13
n_rayleigh = [1, 3, 5, 7, 9]
r_sodium = 15
r_rayleigh = 60
run_simulation_lgs133 = True

script_lgs.main(output_file=output_file_lgs133, master_file=master_file_lgs133, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, run_simulation=run_simulation_lgs133)

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