# calculate WQI for a DataFrame
def calculate_wqi_for_df(df):
    from utils.vnwqi import vnwqi
    # apply for each row
    df["vnwqi_result"] = df.apply(lambda row: vnwqi(row.to_dict()), axis=1)
    
    # extract WQI and Note from the result
    df["WQI"] = df["vnwqi_result"].apply(lambda x: x.get("WQI"))
    df["Note"] = df["vnwqi_result"].apply(lambda x: x.get("Note"))
    df.drop(columns=["vnwqi_result"], inplace=True)
    
    return df
