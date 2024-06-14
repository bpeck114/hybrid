Hybrid On-Axis Study (0, 5, 10, 15, 20, 25, 30)
Directory Name: on_axis_study1A
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
    Working off of Keck's "base" configuration
    Only has NapDela20.fits for all sims, specifically powfs0_llt.fnprof = NapDelta20.fits

Diff against default/ and 20km
    MOST IMPORTANT (20km is left, default is right)
#powfs.bkgrnd=[1.5 1.5 8.273 25.25]                           | #powfs.bkgrnd=[1.5 8.273 25.25]
#powfs.dsa=[0.563 0.563 -1 0]                                 | #powfs.dsa=[0.563 -1 0]
#powfs.dtrat=[1 1 1 1000]                                     | #powfs.dtrat=[1 1 1000]
#powfs.dx=[1/64 1/64 1/16 1/32]                               | #powfs.dx=[1/64 1/16 1/32]
#powfs.fnllt=["keck_llt_CL.conf" "keck_llt_CL.conf" "" ""]    | #powfs.fnllt=["keck_llt_CL.conf" "" ""]
powfs.hs=[90e3,21.45e3,inf,inf]                               | #powfs.hs=[90e3 inf inf]
#powfs.nearecon=[43 43 1.93 1.28]                             | #powfs.nearecon=[43 1.93 1.28]
#powfs.nwfs=[1 1 1 1]                                         | #powfs.nwfs=[1 1 1]
#powfs.siglev=[1270 1270 64529.03 147933.02]                  | #powfs.siglev=[1270 64529.03 147933.02]
#powfs.wvl=[0.589e-6 0.532e-6 0.72e-6 0.72e-6]                | #powfs.wvl=[0.589e-6 0.72e-6 0.72e-6]
#wfs.thetax=[0 0 0 0]                                         | #wfs.thetax=[0 0 0]
#wfs.thetay=[0 0 0 0]                                         | #wfs.thetay=[0 0 0]
#tomo.precond=0                                               | #tomo.precond=1 

    LESS IMPORTANT (specific to just have multiple lgs files) 
#powfs.dither=[0 0 0 0]                                       | #powfs.dither=[0 0 0]
#powfs.dither_amp=[0.025 0.025 0 0]                           | #powfs.dither_amp=[0.025 0 0]
#powfs.dither_gog=[0.5 0.5 0 0]                               | #powfs.dither_gog=[0.5 0 0]
#powfs.dither_gpll=[1 1 0 0]                                  | #powfs.dither_gpll=[1 0 0]
#powfs.dither_npoint=[4 4 0 0]                                | #powfs.dither_npoint=[4 0 0]
#powfs.dither_ograt=[30 30 0 0]                               | #powfs.dither_ograt=[30 0 0]
#powfs.dither_ogskip=[6 6 0 0]                                | #powfs.dither_ogskip=[6 0 0]
#powfs.dither_pllrat=[160 160 0 0]                            | #powfs.dither_pllrat=[160 0 0]
#powfs.dither_pllskip=[0 0 0 0]                               | #powfs.dither_pllskip=[0 0 0]
#powfs.fieldstop=[0 0 0 0]                                    | #powfs.fieldstop=[0 0 0]
#powfs.gtype_recon=[0 0 0 0]                                  | #powfs.gtype_recon=[0 0 0]
#powfs.gtype_sim=[0 0 1 0]                                    | #powfs.gtype_sim=[0 1 0]
#powfs.hc=[0 0 0 0]                                           | #powfs.hc=[0 0 0]
#powfs.lo=[0 0 1 0]                                           | #powfs.lo=[0 1 0]
#powfs.misregx=[0.15 0.15 0 0.42]                             | #powfs.misregx=[0.15 0 0.42]
#powfs.misregy=[0.15 0.15 0 0.42]                             | #powfs.misregy=[0.15 0 0.42]
#powfs.mtchcr=[1 1 0 0]                                       | #powfs.mtchcr=[1 0 0]
#powfs.mtchstc=[0 0 1 1]                                      | #powfs.mtchstc=[0 1 1]
#powfs.nwvl=[1 1 1 1]                                         | #powfs.nwvl=[1 1 1]
#powfs.phystep=[0 0 -1 0]                                     | #powfs.phystep=[0 -1 0]
#powfs.phytype_recon=[1 1 1 1]                                | #powfs.phytype_recon=[1 1 1]
#powfs.pixblur=[0.27 0.27 0 0]                                | #powfs.pixblur=[0.27 0 0]
#powfs.pixpsa=[4 4 4 3]                                       | #powfs.pixpsa=[4 4 3]
#powfs.pixtheta=[3 3 1.5 1.5]                                 | #powfs.pixtheta=[3 1.5 1.5]
#powfs.pywfs=[]                                               | #powfs.pywfs=["" "" ""]
#powfs.rne=[3 3 0.1 7.96]                                     | #powfs.rne=[3 0.1 7.96]
#powfs.saat=[0.3 0.3 0.3 0.5]                                 | #powfs.saat=[0.3 0.3 0.5]
#powfs.sigmatch=[1 1 -1 1]                                    | #powfs.sigmatch=[1 -1 1]
#powfs.skip=[0 0 0 2]                                         | #powfs.skip=[0 0 2]
#powfs.step=[0 0 2 50]                                        | #powfs.step=[0 2 50]
#powfs.trs=[1 1 0 0]                                          | #powfs.trs=[1 0 0]
#powfs.type=[0 0 0 0]                                         | #powfs.type=[0 0 0]
#powfs.wvlwts=[1 1 1 1]                                       | #powfs.wvlwts=[1 1 1]
#powfs1_llt.coldtrat=0                                        <
#powfs1_llt.colprep=0                                         <
#powfs1_llt.colsim=0                                          <
#powfs1_llt.d=0.4                                             <
#powfs1_llt.dhs=10000                                         <
#powfs1_llt.fcfsm=0                                           <
#powfs1_llt.fnamp=""                                          <
#powfs1_llt.fnprep=                                           <
#powfs1_llt.fnprof="NapMean.bin"                              <
#powfs1_llt.fnrange=""                                        <
#powfs1_llt.fnsurf=""                                         <
#powfs1_llt.focus=0                                           <
#powfs1_llt.misreg=[0 0]                                      <
#powfs1_llt.na_fit_dh=500                                     <
#powfs1_llt.na_fit_maxit=0                                    <
#powfs1_llt.na_fit_svdthres=1e-3                              <
#powfs1_llt.na_interp=1                                       <
#powfs1_llt.na_smooth=1                                       <
#powfs1_llt.na_thres=100                                      <
#powfs1_llt.nhs=1                                             <
#powfs1_llt.ox=[0]*6.5                                        <
#powfs1_llt.oy=[0]*6.5                                        <
#powfs1_llt.ttfr=0                                            <
#powfs1_llt.ttpsd=""                                          <
#powfs1_llt.ttrat=5.155                                       <
#powfs1_llt.widthp=0.6                                        <                   