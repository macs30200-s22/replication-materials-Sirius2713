import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

def regression_analysis(data_path):
    data = pd.read_csv(data_path)
    data.columns = [x.replace(' ', '_') for x in data.columns]
    vc = {'date': '0 + C(date)'}
    md = smf.mixedlm('Price_Index ~ date + C1_School_closing_org + C2_Workplace_closing_org + C3_Cancel_public_events_org + C4_Restrictions_on_gatherings_org + C5_Close_public_transport_org + C6_Stay_at_home_requirements_org + C7_Restrictions_on_internal_movement_org + C8_International_travel_controls_org + log_cases_org + log_death_org + log_cases_dst + log_death_dst', vc_formula=vc,
                re_formula='1', data=data, groups='Country')
    mdf = md.fit(method=["lbfgs"])
    print(mdf.summary())
    
    return

