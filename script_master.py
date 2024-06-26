# FILE script_master.py
# For running multiple hybrid simulations

# Importing necessary packages
import numpy as np
import math
import subprocess
import time
import os

import script_photon

output_file_lgs0 = "0S_8mag_mcao_study1A"
master_file_lgs0 = "A_mcao_hybrid.conf"
n_sodium = 1
n_rayleigh = [1]
r_sodium = 15
r_rayleigh = 60
m_sodium = 8
m_rayleigh = 8 
integration_time = 1/1500
run_simulation_lgs0 = False

script_photon.main(output_file=output_file_lgs0, master_file=master_file_lgs0, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, m_sodium=m_sodium, m_rayleigh=m_rayleigh, integration_time=integration_time, run_simulation=run_simulation_lgs0)

output_file_lgs0 = "0S_8mag_mcao_study1A"
master_file_lgs0 = "A_mcao_hybrid.conf"
n_sodium = 8
n_rayleigh = [1, 2]
r_sodium = 15
r_rayleigh = 60
m_sodium = 8
m_rayleigh = 8 
integration_time = 1/1500
run_simulation_lgs0 = False

script_photon.main(output_file=output_file_lgs0, master_file=master_file_lgs0, n_sodium=n_sodium, n_rayleigh=n_rayleigh, r_sodium=r_sodium, r_rayleigh=r_rayleigh, m_sodium=m_sodium, m_rayleigh=m_rayleigh, integration_time=integration_time, run_simulation=run_simulation_lgs0)



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