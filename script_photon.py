# FILE script_photon.py
# For running photometric hybrid simulations

# Importing necessary packages
import numpy as np
import math
import subprocess
import time
import os

# Import internal packages (needs additional installation)
from paarti.utils import maos_utils

# Set parameters for photometric hybrid study
output_file = "0S_8mag_mcao_study1A"               # Name of output file for a batch of simulations 
master_file = "A_mcao_hybrid.conf"                 # Name of selected master file for hybrid simulations
n_sodium = 3                                       # Number of Sodium laser guide stars 
n_rayleigh = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # Number of Rayleigh laser guide stars (creates sub-directories inside "output_file" directory)
r_sodium = 15                                      # Radius of Sodium laser guide star asterism
r_rayleigh = 60                                    # Radius of Rayleigh laser guide star asterism
m_sodium = 8                                       # Magnitude of Sodium laser guide star
m_rayleigh = 8                                     # Magnitude of Rayleigh laser guide star 
integration_time = 1/1500                          # Integration time for entire simulation (sim.dt and sim.dtref, set in master file, NOT set here)
run_simulation = False                             # Set to True to run simulations, otherwise just prints command




def calculate_circle_coordinates(n, radius):
    # Calculates (x, y) coordinate points evenly around the circumference of a circle
    # First point always begins on x-axis
    # Meant for calculating guide-star asterisms 
    
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x_coords = np.round(radius * np.cos(angles), 2)
    y_coords = np.round(radius * np.sin(angles), 2)
    return x_coords, y_coords




def main(output_file, master_file, n_sodium, n_rayleigh, r_sodium, r_rayleigh, m_sodium, m_rayleigh, integration_time, run_simulation=False):
    # For running photometric hybrid simulations
    # Function assumes one sodium beacon and splits the one beacon into multiple spots when prompted
    # Function assumes that each additional Rayleigh spot is a new beacon

    # Setting photometric values for sodium beacon 
    sodium_siglev_full_all, sodium_bkgrnd_all, sodium_snr_all, sodium_nearecon_all = maos_utils.keck_nea_photons_any_config(wfs='LGSWFS',
                                       side=0.154, # Needs to match dm.dx (actuator count), 0.154 is 4000 actuators for Keck primary
                                       throughput=0.36 * 0.88,
                                       ps = 3.0,
                                       theta_beta = 1.5 * ( math.pi/180.0 ) / ( 60.0*60.0 ),
                                       band = "R",
                                       sigma_e = 0.5,
                                       pix_per_ap = 4,
                                       time = integration_time,
                                       m = m_sodium)

    # Round the values that PAARTI gives for sodium beacons
    sodium_siglev_full = np.round(sodium_siglev_full_all, 2)
    sodium_nearecon = np.round(sodium_nearecon_all, 2)

    # Divide singualr sodium beacon into multiple spots on-sky
    if n_sodium == 0:
        sodium_siglev = sodium_siglev_full
    elif n_sodium > 0:
        sodium_siglev = sodium_siglev_full / n_sodium

    # Setting photometric values for tip-tilt stars and truth (low-bandwidth) wavefront sensor
    tt_siglev_all, tt_bkgrnd_all, tt_bkgrnd_all, tt_nearecon_all = maos_utils.keck_nea_photons(m=8, wfs='STRAP', wfs_int_time=integration_time)
    truth_siglev_all, truth_bkgrnd_all, truth_snr_all, truth_nearecon_all = maos_utils.keck_nea_photons(m=8, wfs='LBWFS', wfs_int_time=integration_time)

    # Round the values that PAARTI gives for tip-tilt and truth
    tt_siglev = np.round(tt_siglev_all, 2)
    tt_bkgrnd = np.round(tt_bkgrnd_all, 2)
    tt_nearecon = np.round(tt_nearecon_all, 2)
    
    truth_siglev = np.round(truth_siglev_all, 2)
    truth_bkgrnd = np.round(truth_bkgrnd_all, 2)
    truth_nearecon = np.round(truth_nearecon_all, 2)

    # Calculate positions of sodium wave-front sensors and laser launch telescopes
    wfs_sodium_xx, wfs_sodium_yy = calculate_circle_coordinates(n_sodium, r_sodium)
    llt_sodium_xx, llt_sodium_yy = calculate_circle_coordinates(n_sodium, radius=1) # Multiplied by 6.5 m later

    # Set the outputs in a format that MAOS accepts (no commas) 
    wfs_sodium_x = ' '.join(map(str, wfs_sodium_xx))
    wfs_sodium_y = ' '.join(map(str, wfs_sodium_yy))
    llt_sodium_x = ' '.join(map(str, llt_sodium_xx))
    llt_sodium_y = ' '.join(map(str, llt_sodium_yy))

    duration = [] # For recording how long each simulation takes

    # Describe what is happening
    print(f"Running {output_file} hybrid study:\n")

    # Run MAOS simulations for on-axis hybrid study
    for rayleigh in n_rayleigh:
        # Setting photometric values for Rayleigh beacon 
        rayleigh_siglev_all, rayleigh_bkgrnd_all, rayleigh_snr_all, rayleigh_nearecon_all = maos_utils.keck_nea_photons_any_config(wfs='RLGSWFS',
                                       side=0.154, # Needs to match dm.dx (actuator count), 0.154 is 4000 actuators for Keck primary
                                       throughput=0.36 * 0.88,
                                       ps = 3.0,
                                       theta_beta = 1.5 * ( math.pi/180.0 ) / ( 60.0*60.0 ),
                                       band = "R",
                                       sigma_e = 0.5,
                                       pix_per_ap = 4,
                                       time = integration_time,
                                       m = m_rayleigh)

        # Round the values that PAARTI gives for Rayleigh beacons
        rayleigh_siglev = np.round(rayleigh_siglev_all, 2)
        rayleigh_nearecon = np.round(rayleigh_bkgrnd_all, 2)

        # Calculate positions of Rayleigh wave-front sensors and laser launch telescopes
        wfs_rayleigh_xx, wfs_rayleigh_yy = calculate_circle_coordinates(rayleigh, r_rayleigh)
        llt_rayleigh_xx, llt_rayleigh_yy = calculate_circle_coordinates(rayleigh, radius=1)

        # Set the outputs in a format that MAOS accepts (no commas)
        wfs_rayleigh_x = ' '.join(map(str, wfs_rayleigh_xx))
        wfs_rayleigh_y = ' '.join(map(str, wfs_rayleigh_yy))
        llt_rayleigh_x = ' '.join(map(str, llt_rayleigh_xx))
        llt_rayleigh_y = ' '.join(map(str, llt_rayleigh_yy))

        # MAOS command
        command = f"maos -o {output_file}/{rayleigh}rayleigh -c {master_file} plot.all=1 plot.setup=1 -O powfs.nwfs=[{n_sodium} {rayleigh} 3 1] wfs.thetax=[{wfs_sodium_x} {wfs_rayleigh_x} 5 -2.5 -2.5 0] wfs.thetay=[{wfs_sodium_y} {wfs_rayleigh_y} 0 4.33 -4.33 0] powfs0_llt.ox = [{llt_sodium_x}]*6.5 powfs0_llt.oy=[{llt_sodium_y}]*6.5 powfs1_llt.ox = [{llt_rayleigh_x}]*6.5 powfs1_llt.oy=[{llt_rayleigh_y}]*6.5 powfs.siglev=[{sodium_siglev} {rayleigh_siglev} {tt_siglev} {truth_siglev}] powfs.bkgrnd=[0.1 0.1 {tt_bkgrnd} {truth_bkgrnd}] powfs.nearecon=[{sodium_nearecon} {rayleigh_nearecon} {tt_nearecon} {truth_nearecon}]"
        
        print("---------------------------------------")
        print("SIM:", rayleigh)
        print("COMMAND:", command)
        print("MASTER:", master_file) 
        print("LOCATION:", output_file)
        print("---------------------------------------")

        # Run simulation (comment out the following line for testing on non-NERSC machine)
        start_time = time.time()
        if run_simulation:
            subprocess.run(command, shell=True, text=True)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Convert time to hours, minutes, seconds and milliseconds
        hours = int(elapsed_time // 3600)
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

        duration.append({
            "sim": rayleigh,
            "elapsed_time": elapsed_time,
            "time_hours": hours,
            "time_minutes" : minutes,
            "time_seconds" : seconds,
            "time_milliseconds": milliseconds
        })

        print("\n")

    # Total duration
    total_elapsed_time = sum(dur["elapsed_time"] for dur in duration)
    total_hours = int(total_elapsed_time // 3600)
    total_minutes = int((total_elapsed_time % 3600) // 60)
    total_seconds = int(total_elapsed_time % 60)
    total_milliseconds = int((total_elapsed_time - int(total_elapsed_time)) * 1000)

    print("---------------------------------------")
    for dur in duration:
        print("SIM ({}) TIME:". format(dur["sim"]), "{}:{}:{}.{}".format(dur["time_hours"], dur["time_minutes"], dur["time_seconds"], dur["time_milliseconds"]))
    print("   TOTAL TIME: {}:{}:{}.{}".format(total_hours, total_minutes, total_seconds, total_milliseconds))
    print("---------------------------------------")

    os.chdir(output_file)

    with open("maos_sim_time.txt", "a") as file:
        file.write("---------------------------------------\n")
        for dur in duration:
            file.write("SIM ({}) TIME: {}:{}:{}.{}\n".format(
                dur["sim"], dur["time_hours"], dur["time_minutes"], dur["time_seconds"], dur["time_milliseconds"]))
        file.write("   TOTAL TIME: {}:{}:{}.{}\n".format(total_hours, total_minutes, total_seconds, total_milliseconds))
        file.write("---------------------------------------\n")

    os.chdir("..")

if __name__ == "__main__":
    main()