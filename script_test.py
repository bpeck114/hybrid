# FILE script_on_axis.py
# For running on-axis hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

# Set parameters for hybrid study
output_file = "time"
angle_degrees = 30
height = np.array([20, 22, 24, 26, 28, 30]) #km

angle_radians = np.deg2rad(angle_degrees)
corrected_height = (height + 4.765) * np.cos(angle_radians)
rounded_height = np.round(corrected_height, 2)

duration = [] # For recording how long each simulation takes

# Describe what is happening
print("Running on-axis hybrid study:\n")

# Run MAOS simulations for on-axis hybrid study
for h, rounded_h in zip(height, rounded_height):
    command = f"maos -o {output_file}/{h}km -c A_hybrid.conf plot.all=1 plot.setup=1 -O powfs.hs=[90e3,{rounded_h}e3,inf,inf] powfs1_llt.fnprof = NapDelta{h}.fits powfs.nwfs=[1]"
    
    print("---------------------------------------")
    print("SIM:", h)
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
        "sim": h,
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
