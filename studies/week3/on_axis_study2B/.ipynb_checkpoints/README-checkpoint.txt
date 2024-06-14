Hybrid On-Axis Study (20, 22, 24, 26, 28, 30)
Directory Name: on_axis_study2B
MAOS Commit: ? (anshar)
Date: 6/3/24 

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          8         
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          8
     Rayleigh LGS Location:          On-Axis (but varying in height)

                        TT:          1
              TT Magnitude:          8

                Atmosphere:          "atm_mk13n50p_hybrid.conf" # More error with hybrid version
                     Speed:          1/1500
                     Steps:          3000 (2 seconds with current speed)
                 Actuators:          34 x 34 (1156 actuators) # Memory error with increased density 
                    Stroke:          30 (mircrons)
              Inner-Stroke:          7 (mircrons)


Other Notes:
    Changed to "atm_mk13n50p_hybrid.conf" atmospheric profile
    Increased stroke and inner-actuator stroke from 1B

Questions:
    What does "step 211 DM 0: 162 actuators clipped" mean?