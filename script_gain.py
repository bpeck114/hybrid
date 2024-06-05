# FILE script_gain.py
# For running gain hybrid simulations
# To just test script, comment out line 38 or "subprocess.run(command, shell=True, text=True))"

# Importing necessary packages
import numpy as np
import subprocess
import time
import os

# Set parameters for hybrid study
output_file = "gain_study"
master_file = "A_hybrid.conf"
angle_degrees = 30
gain = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
gain_index = np.array([0000, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

duration = [] # For recording how long each simulation takes

# Describe what is happening
print(f"Running {output_file} hybrid study:\n")

# Run MAOS simulations for on-axis hybrid study
for g, g_index in zip(gain, gain_index):
    command = f"maos -o {output_file}/{g_index}gain -c {master_file} plot.all=1 plot.setup=1 -O sim.ephi = {g}"
    
    print("---------------------------------------")
    print("SIM:", g)
    print("COMMAND:", command)
    print("MASTER:", master_file) 
    print("LOCATION:", output_file)
    print("---------------------------------------")

    # Run simulation (comment out the following line for testing on non-NERSC machine)
    start_time = time.time()
    subprocess.run(command, shell=True, text=True)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert time to hours, minutes, seconds and milliseconds
    hours = int(elapsed_time // 3600)
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

    duration.append({
        "sim": g,
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
    file.write("     TOTAL TIME: {}:{}:{}.{}\n".format(total_hours, total_minutes, total_seconds, total_milliseconds))
    file.write("---------------------------------------\n")

os.chdir("..")