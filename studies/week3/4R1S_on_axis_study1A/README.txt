Hybrid On-Axis Study (20, 22, 24, 26, 28, 30)
Directory Name: 4R1S_on_axis_study1A
MAOS Commit: ? (anshar)
Date: 6/4/24 

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          ?       
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          ? (it is unknown at the moment for increased actuator density)
     Rayleigh LGS Location:          60 arc-second radius (side-launch)

                        TT:          1
              TT Magnitude:          8

                Atmosphere:          "atm_mk13n50p_ground_detail.conf" # More error with hybrid version
                     Speed:          1/1500
                     Steps:          3000 (2 seconds with current speed)
                 Actuators:          34 x 34 (1156 actuators) # Memory error with increased density 
                    Stroke:          300 (mircrons)
              Inner-Stroke:          20 (mircrons)


Other Notes:
    wfs.thetax = [0 60 0 -60 0 0 0] 
    wfs.thetay = [0 0 60 0 -60 0 0]
    powfs1_llt.ox = [1 0 -1 0] *6.5
    powfs1_llt.oy = [0 1 0 -1] *6.5