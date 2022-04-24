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

regression_analysis('../data/processed/export_policy.csv') # for export data.
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

Export data regression results:
```
                        Mixed Linear Model Regression Results
======================================================================================
Model:                       MixedLM          Dependent Variable:          Price_Index
No. Observations:            112              Method:                      REML       
No. Groups:                  4                Scale:                       4.4394     
Min. group size:             28               Log-Likelihood:              -263.1834  
Max. group size:             28               Converged:                   Yes        
Mean group size:             28.0                                                     
--------------------------------------------------------------------------------------
                                          Coef.  Std.Err.   z    P>|z|  [0.025  0.975]
--------------------------------------------------------------------------------------
Intercept                                100.789    1.851 54.448 0.000  97.161 104.417
date                                       1.453    0.081 17.901 0.000   1.293   1.612
C1_School_closing_org                      2.930    3.899  0.752 0.452  -4.711  10.571
C2_Workplace_closing_org                   1.199    2.411  0.497 0.619  -3.528   5.925
C3_Cancel_public_events_org               -1.598    4.966 -0.322 0.748 -11.330   8.135
C4_Restrictions_on_gatherings_org         -4.034    0.906 -4.452 0.000  -5.810  -2.258
C5_Close_public_transport_org              1.924    1.350  1.425 0.154  -0.722   4.570
C6_Stay_at_home_requirements_org          -1.917    2.578 -0.744 0.457  -6.969   3.135
C7_Restrictions_on_internal_movement_org  -1.350    3.997 -0.338 0.736  -9.184   6.483
C8_International_travel_controls_org      -1.029    3.376 -0.305 0.760  -7.645   5.587
log_cases_org                              0.464    0.788  0.589 0.556  -1.081   2.008
log_death_org                              0.042    0.751  0.057 0.955  -1.429   1.513
log_cases_dst                             -0.328    0.955 -0.344 0.731  -2.199   1.543
log_death_dst                             -0.733    1.040 -0.705 0.481  -2.771   1.304
Country Var                                6.946                                      
date Var                                   3.422                                      
======================================================================================
```

Import air freight price indexes are more impacted by Covid-related policies compred to export air freight price indexes. For import data, policies in origin countries (Canada, Mexico, China, Japan), including cancel public events, restrictions on gatherings, stay at home requirements, international travel controls, are significantly negative associated with air freight price indexes. This is not what I originally expected, but I think it's probably because demands for trading between two countries decline with these policies. I'll look into effects among different countries and categories in later analysis.
