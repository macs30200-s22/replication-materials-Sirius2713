[![DOI](https://zenodo.org/badge/483373544.svg)](https://zenodo.org/badge/latestdoi/483373544)

# Perspectives on Computational Research

The code is written in Python 3.8.8 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

```
pip install -r requirements.txt
```

To replicate the results of the initial analysis, import the `initial_analysis` module under `codes` folder and use processed data from `data/processed`. The you can do regression analysis to fit mixed-effects regression models.

```
import initial_analysis # Make sure you are under codes folder before importing this package. Otherwise, you need to specify the path.
```

Then, fit mixed-effects regression models on import air freight price indexes and export air freight price indexes.
```
regression_analysis('../data/processed/import_policy.csv') # for import data.
```

Import data regression results:
```
                        Mixed Linear Model Regression Results
======================================================================================
Model:                       MixedLM          Dependent Variable:          Price_Index
No. Observations:            112              Method:                      REML       
No. Groups:                  4                Scale:                       89.5603    
Min. group size:             28               Log-Likelihood:              -386.0116  
Max. group size:             28               Converged:                   Yes        
Mean group size:             28.0                                                     
--------------------------------------------------------------------------------------
                                          Coef.  Std.Err.   z    P>|z|  [0.025  0.975]
--------------------------------------------------------------------------------------
Intercept                                115.604   14.409  8.023 0.000  87.363 143.845
date                                       0.758    0.277  2.737 0.006   0.215   1.301
C1_School_closing_org                     -1.027   13.220 -0.078 0.938 -26.938  24.884
C2_Workplace_closing_org                   0.805    8.178  0.098 0.922 -15.224  16.833
C3_Cancel_public_events_org              -35.935   16.905 -2.126 0.034 -69.067  -2.802
C4_Restrictions_on_gatherings_org         -6.954    3.084 -2.255 0.024 -12.999  -0.910
C5_Close_public_transport_org              6.277    4.756  1.320 0.187  -3.046  15.599
C6_Stay_at_home_requirements_org         -21.311    8.770 -2.430 0.015 -38.499  -4.123
C7_Restrictions_on_internal_movement_org  26.158   13.708  1.908 0.056  -0.709  53.026
C8_International_travel_controls_org     -23.644   11.508 -2.054 0.040 -46.199  -1.088
log_cases_org                             13.562    2.788  4.865 0.000   8.098  19.026
log_death_org                            -11.962    2.664 -4.489 0.000 -17.184  -6.739
log_cases_dst                             -6.199    3.267 -1.897 0.058 -12.602   0.204
log_death_dst                              6.617    3.570  1.854 0.064  -0.380  13.614
Country Var                              752.789                                      
date Var                                   0.754                                      
======================================================================================
```

Country-level random effects of international travel controls:

![re_c](/images/re_viz.png)


Category-level random effects of international travel controls in Canada:

![re_ca](/images/re_viz_ca.png)

****
### Cite this repo as
Wenqian Zhang. “Macs30200-s22/replication-materials-sirius2713: Draft”. Zenodo, May 22, 2022. https://doi.org/10.5281/zenodo.6570841.
