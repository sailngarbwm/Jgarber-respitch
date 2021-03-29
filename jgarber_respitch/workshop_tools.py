
import pandas as pd 
def convert_df_row_to_dictionary(df: pd.DataFrame,row_number:int):
    """
    converts the row of a dataframe to a dictionary
    of lists

    :param df: input dataframe
    :type df: pd.DataFrame
    :param row_number: row to convert into a dictionary
    
    :return: dictionary of the values, where keys are the column names, and the values are lists of the values
    :rtype: dictionary

    """

    out_dict = df.loc[row_number].to_dict()

    for key in out_tdict.keys():
        out_dict[key] = [out_dict[key]]
    return out_dict