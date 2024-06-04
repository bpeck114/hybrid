# FILE script_20km_radius.py
# For running radius hybrid simulations
# To just test script, comment out line 27 or "subprocess.run(command, shell=True, text=True))"

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

# Set parameters for radius hybrid study
output_file = "20km_study1A"
angle_degrees = 30
radius = np.array([1, 2, 5, 7, 10]) #arcseconds

duration = [] # For recording how long each simulation takes

# Describe what is happening
print(f"Running {output_file} radius hybrid study:\n")

# Run MAOS simulations for on-axis hybrid study
for rad in radius:
    command = f"maos -o {output_file}/{rad}as -c A_hybrid.conf plot.all=1 plot.setup=1 -O wfs.thetax=[0 {rad} 0 0] powfs1_llt.ox = [6.5] powfs1_llt.oy = [6.5]"
    
    print("---------------------------------------")
    print("SIM:", rad)
    print("COMMAND:", command)
    print("MASTER:",f"A_hybrid.conf") 
    print("LOCATION:", output_file)
    print("---------------------------------------")

    # Run simulation (comment out the following line for testing on non-NERSC machine)
    start_time = time.time()
    #subprocess.run(command, shell=True, text=True)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert time to hours, minutes, seconds and milliseconds
    hours = int(elapsed_time // 3600)
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

    duration.append({
        "sim": rad,
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