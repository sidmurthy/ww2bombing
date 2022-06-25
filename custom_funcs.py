def percent_missing(data):
    percents = data.isnull().sum() * 100 / len(data)
    missing_value_df = pd.DataFrame({'column_name': data.columns,'percent_missing': percents}).set_index('column_name')
    missing_value_df.sort_values('percent_missing', inplace=True)
    return missing_value_df

def filter_theater(country_data, theater):
    ret_df = country_data.loc[country_data['THEATER'] == theater].drop(['SIGHTING_METHOD_CODE', 'SPARES_RETURN_AC', 'AC_LOST',
       'TGT_PRIORITY_EXPLANATION', 'AC_DAMAGED', 'TGT_INDUSTRY',
       'TGT_INDUSTRY_CODE', 'TGT_ID', 'CALLSIGN', 'WX_FAIL_AC',
       'TGT_COUNTRY_CODE', 'MISC_FAIL_AC', 'MECH_FAIL_AC'], axis=1)
    return ret_df


def groupby_custom(theater_data, group_by: str):
    return theater_data.groupby(by=group_by).agg({'LATITUDE':'mean', 'LONGITUDE':'mean', 'AC_ATTACKING': ['mean','sum'],
'ALTITUDE':'mean', 'ALTITUDE_FEET':'mean', 'NUMBER_OF_HE':['mean','sum'], 'LBS_HE':['mean','sum'],'TONS_OF_HE':['mean','sum'],
'NUMBER_OF_IC':['sum', 'mean'], 'LBS_IC':['mean','sum'], 'TONS_OF_IC':['mean','sum'], 'NUMBER_OF_FRAG':['mean','sum'],
'LBS_FRAG':['mean','sum'], 'TONS_OF_FRAG':['mean','sum'], 'TOTAL_LBS':['mean','sum'], 'TOTAL_TONS':['mean','sum'],
'TAKEOFF_LATITUDE': 'mean', 'TAKEOFF_LONGITUDE': 'mean', 'AC_AIRBORNE':['mean','sum'], 'AC_DROPPING':['mean','sum'],
"ROUNDS_AMMO":['mean','sum']}
)


def stat_by_group(grouped_theater_data, category, stat):
    query_stat = [(category, stat)]
    stat_by_group = grouped_theater_data.loc[:, query_stat].sort_values(by=query_stat, ascending=False)
    stat_by_group.columns = stat_by_group.columns.to_flat_index()
    stat_by_group.reset_index(inplace=True)
    return stat_by_group

def top_n_category(dataframe, n, category):
    return dataframe[category].value_counts()[0:n]



