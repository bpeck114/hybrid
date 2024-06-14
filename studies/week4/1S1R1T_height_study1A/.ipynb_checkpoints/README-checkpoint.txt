Hybrid On-Axis Study (20, 22, 24, 26, 28, 30)
Directory Name: on_axis_study3B
MAOS Commit: ? (anshar)
Date: 6/10/24 

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          ?         
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          ?
     Rayleigh LGS Location:          On-Axis (but varying in height)

                        TT:          1
              TT Magnitude:          8

                Atmosphere:          "atm_mk13n50p_ground_detail.conf" # More error with hybrid version
                     Speed:          1/1500
                     Steps:          3000 (2 seconds with current speed)
                 Actuators:          34 x 34 (1156 actuators) # Memory error with increased density 
                    Stroke:          30 (mircrons)
              Inner-Stroke:          2 (mircrons)


Other Notes:
    Using old ground_detail atmosphere 

Questions:
    What does "step 211 DM 0: 162 actuators clipped" mean?
    ' ' Step  2047 updated high order loop gain: 0.354 ?
    ' ' Step  2049: TWFS[3] has output with gain 0.5 ?