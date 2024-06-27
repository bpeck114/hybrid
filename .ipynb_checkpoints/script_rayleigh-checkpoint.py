# FILE script_rayleigh.py
# For running photometric Rayleigh simulations

# Importing necessary packages
import numpy as np
import math
import subprocess
import time
import os

# Import internal packages (needs additional installation)
from paarti.utils import maos_utils

# Set parameters for photometric hybrid study
output_file = "0S_rayleigh_mag_study1C"            # Name of output file for a batch of simulations 
master_file = "A_mcao_hybrid.conf"                 # Name of selected master file for hybrid simulations
s_rayleigh = [8.80, 17.61, 35.22, 70.43, 140.86, 281.73, 563.45]
                                                   # powfs.siglev of Rayleigh laser guide star 
w_rayleigh = [6.25, 12.5, 25, 50, 100, 200, 400]
integration_time = 1/1500                          # Integration time for entire simulation (sim.dt and sim.dtref, set in master file, NOT set here)
run_simulation = False                             # Set to True to run simulations, otherwise just prints command




def main(output_file, master_file, s_rayleigh, w_rayleigh, integration_time, run_simulation=False):
    # For running photometric Rayleigh simulations

    # Setting photometric values for tip-tilt stars and truth (low-bandwidth) wavefront sensor
    tt_snr_all, tt_nearecon_all, tt_siglev_all, tt_bkgrnd_all = maos_utils.keck_nea_photons(m=8, wfs='STRAP', wfs_int_time=integration_time)
    truth_snr_all, truth_nearecon_all, truth_siglev_all, truth_bkgrnd_all = maos_utils.keck_nea_photons(m=8, wfs='LBWFS', wfs_int_time=integration_time)

    # Round the values that PAARTI gives for tip-tilt and truth
    tt_siglev = np.round(tt_siglev_all, 3)
    tt_bkgrnd = np.round(tt_bkgrnd_all, 3)
    tt_nearecon = np.round(tt_nearecon_all, 3)
    
    truth_siglev = np.round(truth_siglev_all, 3)
    truth_bkgrnd = np.round(truth_bkgrnd_all, 3)
    truth_nearecon = np.round(truth_nearecon_all, 3)

    duration = [] # For recording how long each simulation takes

    # Describe what is happening
    print(f"Running {output_file} Rayleigh study:\n")

    # Run MAOS simulations for on-axis Rayleigh study
    for i, rayleigh in enumerate(w_rayleigh):

        rayleigh_siglev = s_rayleigh[i]
        print(rayleigh_siglev)

        # MAOS command
        command = f"maos -o {output_file}/{rayleigh}W -c {master_file} plot.all=1 plot.setup=1 -O 'powfs.siglev=[0 {rayleigh_siglev} 64.52903 147933.02]'"
        
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