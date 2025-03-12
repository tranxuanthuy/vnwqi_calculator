def calculate_wqi_for_row(row, weighted = False):
    '''Calculate WQI for a row
    input:
        row: a row of the dataframe
    output:
        WQI
    '''
    group_data = []
    from units.group import group_1, group_2, group_3, group_4, group_5
    for group in [group_1, group_2, group_3, group_4, group_5]:
        group_dict = {}
        for col in group:
            if col in row.index: 
                group_dict[col + '_value'] = row[col]
        group_data.append(group_dict)
    from units.fomula import wqi
    if 'temperature' in row.index:
        temperature = row['temperature']
    else:
        import numpy as np
        temperature = np.nan
    vnwqi = wqi(*group_data, temperature=temperature, weighted=weighted)
    return vnwqi

