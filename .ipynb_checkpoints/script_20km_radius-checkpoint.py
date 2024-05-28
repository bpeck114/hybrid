# FILE script_20km_radius.py
# For running hybrid simulations

# Importing necessary packages
import numpy as np
import subprocess
import time

# Set parameters for radius hybrid study
output_file = "20km_study"
angle_degrees = 30
radius = np.array([0, 1, 2, 5, 7, 10, 15, 20, 25, 30]) #arcseconds


'''
CODE TO DESCRIBE HOW KEEP RAYLEIGH AT 20KM BUT DIFFERENT DISTANCES
'''

duration = [] # For recording how long each simulation takes

# Describe what is happening
print("Running 20km radius hybrid study:\n")

# Run MAOS simulations for on-axis hybrid study
for a in angle:
    command = f"maos -o {output_file}/{r}as -c hybrid.conf plot.all=1 plot.setup=1 -O powfs.hs=[90e3"
    
    print("---------------------------------------")
    print("SIM:", a)
    print("COMMAND:", command)
    print("MASTER:", f"hybrid.conf") 
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
        "sim": h,
        "time_hours": hours,
        "time_minutes" : minutes,
        "time_seconds" : seconds,
        "time_milliseconds": milliseconds
    })

    print("\n")

print("---------------------------------------")
for dur in duration:
    print("SIM ({}) TIME:". format(dur["sim"]), "{}:{}:{}.{}".format(dur["time_hours"], dur["time_minutes"], dur["time_seconds"], dur["time_milliseconds"]))
print("---------------------------------------")
