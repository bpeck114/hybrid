Hybrid Radius Study (0, 1, 2, 5, 7, 10)
Directory Name: 20km_study1A
MAOS Commit: ? (anshar)
Date: 6/3/24 

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          8         
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          8
     Rayleigh LGS Location:          0, 1, 2, 5, 7, 10 (arcseconds)

                        TT:          1
              TT Magnitude:          8

                Atmosphere:          "atm_mk13n50p_ground_detail.conf" # More error with hybrid version
                     Speed:          1/1500
                     Steps:          3000 (2 seconds with current speed)
                 Actuators:          34 x 34 (1156 actuators) # Memory error with increased density 
                    Stroke:          30 (mircrons)
              Inner-Stroke:          7 (mircrons)


Other Notes:
    Set powfs1_llt.ox = [6.5] powfs1_llt.oy = [6.5], should I try powfs1_llt.ox = [0] powfs1_llt.oy = [0]?