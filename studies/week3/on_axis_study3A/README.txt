ERROR FROM INCREASED ACTUATOR COUNT AND ATM PROFILE

Hybrid On-Axis Study (20, 22, 24, 26, 28, 30)
Directory Name: on_axis_study3A
MAOS Commit: 
Date:

Parameters:
                Sodium LGS:          1
      Sodium LGS Magnitude:          8         
       Sodium LGS Location:          On-Axis

              Rayleigh LGS:          1
    Rayleigh LGS Magnitude:          8
     Rayleigh LGS Location:          On-Axis (but varying in height)

                        TT:          1
              TT Magnitude:          8

Other Notes:
    Same setup as act_study2 with powfs1
    34x34 actuators and at 1/1500 speed (segmentation fault at denser levels)
    More actuator and inner-actuator stroke, no latency (sim.alhi = 0) 
    More steps (3000)
    Less atmospheric levels (to preserve memory)

Runtimes
---------------------------------------
SIM (20) TIME: 0:2:42.503
SIM (22) TIME: 0:2:40.120
SIM (24) TIME: 0:2:46.236
SIM (26) TIME: 0:2:44.880
SIM (28) TIME: 0:2:42.860
SIM (30) TIME: 0:2:43.92
---------------------------------------

Diff against on_axis_study2 (first is study2, second is study3)

< #atm.ht=[0 120 280 440 807 4349 8000 12000 19501]
> #atm.ht=[0 15 30 45 120 200 280 360 440 807 4349 8000 12000 19501]
---
< #atm.ws=[5.6 7.0 7.0 7.0 6.5 12.8 22 9.5 5.6]
> #atm.ws=[5.6 5.77 6.25 7.57 7.0 7.0 7.0 7.0 7.0 6.5 12.8 22 9.5 5.6]
---
< #atm.wt=[.499 0.021 0.018 0.006 0.107 0.144 0.093 0.075 0.036]
> #atm.wt=[0.302 0.154 0.041 0.002 0.021 0.010 0.008 0.005 0.001 0.107 0.144 0.093 0.075 0.036]
---
< #dm.dx=[0.287]
> #dm.dx=[0.563]
---
< #powfs.bkgrnd=[0.012 0.012 2.603 0.001]
> #powfs.bkgrnd=[1.5 1.5 8.273 25.25]
---
< #powfs.nearecon=[161.140 161.140 1.369 202.516]
> #powfs.nearecon=[43 43 1.93 1.28]
---
< #powfs.siglev=[114.042 114.042 128116.746 41.558]
> #powfs.siglev=[1270 1270 64529.03 147933.02]
---
< Mean: 337.56 107.51 319.98  nm.
> Mean: 753.10 60.87 750.63  nm.