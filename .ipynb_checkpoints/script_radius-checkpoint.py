# FILE script_on_axis.py
# For running on-axis hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

# Set parameters for hybrid study
#output_file = "1S4R3T_radius_study1A"
#master_file = "A_hybrid.conf"
#radius = np.array([5, 15, 25, 35, 45, 60]) #km
#run_simulation = False

def main(output_file, master_file, radius, run_simulation=False):
    thetax = []
    thetay = []
    
    for r in radius: 
        thetax.append([r, 0, -r, 0])
        thetay.append([0, r, 0, -r])

    for r, x, y in zip(radius, thetax, thetay):
        x_coors = ' '.join(map(str, x))
        y_coors = ' '.join(map(str, y))

    duration = [] # For recording how long each simulation takes

    # Describe what is happening
    print(f"Running {output_file} hybrid study:\n")

    # Run MAOS simulations for on-axis hybrid study
    for r, x, y in zip(radius, thetax, thetay):
        x_coors = ' '.join(map(str, x))
        y_coors = ' '.join(map(str, y))
        command = f"maos -o {output_file}/{r}as -c {master_file} plot.all=1 plot.setup=1 -O powfs.nwfs=[4 4 3 1] wfs.thetax=[0 15 -7.5 -7.5 {x_coors} 5 -2.5 -2.5 0] wfs.thetay=[0 0 12.99 -12.99 {y_coors} 0 4.33 -4.33 0] powfs0_llt.ox = [1 0 -1 0]*6.5 powfs0_llt.oy=[0 1 0 -1]*6.5 powfs1_llt.ox = [1 0 -1 0]*6.5 powfs1_llt.oy=[0 1 0 -1]*6.5"
        
        print("---------------------------------------")
        print("SIM:", r)
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
            "sim": r,
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