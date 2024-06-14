Hybrid On-Axis Study (0.2, 0.4)
Directory Name: gain_study2A
MAOS Commit: ? (anshar)
Date: 6/4/24 

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          ?      
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          ? (it is unknown at the moment for increased actuator density)
     Rayleigh LGS Location:          On-Axis (but varying in height)

                        TT:          1
              TT Magnitude:          8

                Atmosphere:          "atm_mk13n50p_ground_detail.conf" # More error with hybrid version
                     Speed:          1/1500
                     Steps:          3000 (2 seconds with current speed)
                 Actuators:          34 x 34 (1156 actuators) # Memory error with increased density 
                    Stroke:          300 (mircrons)
              Inner-Stroke:          20 (mircrons)


Other Notes:
    Set recon.psd = 0 to turn off automatic gain in MAOS 
    Setting sim.ephi = 0 gain parameter