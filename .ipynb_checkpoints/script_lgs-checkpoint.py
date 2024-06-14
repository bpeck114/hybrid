# FILE script_on_axis.py
# For running on-axis hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

# Set parameters for hybrid study
output_file = "30km60asR_15asS_lgs_study1A"
master_file = "A_hybrid.conf"
n_sodium = 3
n_rayleigh = [2, 4, 6, 8, 10]
r_sodium = 15
r_rayleigh = 60
run_simulation = False

def calculate_circle_coordinates(n, radius):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x_coords = np.round(radius * np.cos(angles), 2)
    y_coords = np.round(radius * np.sin(angles), 2)
    return x_coords, y_coords

def main(output_file, master_file, n_sodium, n_rayleigh, r_sodium, r_rayleigh, run_simulation=False):
    wfs_sodium_xx, wfs_sodium_yy = calculate_circle_coordinates(n_sodium, r_sodium)
    llt_sodium_xx, llt_sodium_yy = calculate_circle_coordinates(n_sodium, radius=1)

    wfs_sodium_x = ' '.join(map(str, wfs_sodium_xx))
    wfs_sodium_y = ' '.join(map(str, wfs_sodium_yy))
    llt_sodium_x = ' '.join(map(str, llt_sodium_xx))
    llt_sodium_y = ' '.join(map(str, llt_sodium_yy))

    duration = [] # For recording how long each simulation takes

    # Describe what is happening
    print(f"Running {output_file} hybrid study:\n")

    # Run MAOS simulations for on-axis hybrid study
    for rayleigh in n_rayleigh:
        wfs_rayleigh_xx, wfs_rayleigh_yy = calculate_circle_coordinates(rayleigh, r_rayleigh)
        llt_rayleigh_xx, llt_rayleigh_yy = calculate_circle_coordinates(rayleigh, radius=1)
        
        wfs_rayleigh_x = ' '.join(map(str, wfs_rayleigh_xx))
        wfs_rayleigh_y = ' '.join(map(str, wfs_rayleigh_yy))
        llt_rayleigh_x = ' '.join(map(str, llt_rayleigh_xx))
        llt_rayleigh_y = ' '.join(map(str, llt_rayleigh_yy))
        
        command = f"maos -o {output_file}/{rayleigh}rayleigh -c {master_file} plot.all=1 plot.setup=1 -O powfs.nwfs=[{n_sodium} {rayleigh} 3 1] wfs.thetax=[{wfs_sodium_x} {wfs_rayleigh_x} 5 -2.5 -2.5 0] wfs.thetay=[{wfs_sodium_y} {wfs_rayleigh_y} 0 4.33 -4.33 0] powfs0_llt.ox = [{llt_sodium_x}]*6.5 powfs0_llt.oy=[{llt_sodium_y}]*6.5 powfs1_llt.ox = [{llt_rayleigh_x}]*6.5 powfs1_llt.oy=[{llt_rayleigh_y}]*6.5"
        
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