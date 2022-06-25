import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer 
import warnings
warnings.filterwarnings('ignore')

categorical_columns = ['intertiol_plan', 'voice_mail_plan', 'Churn', 'location_code']

df = pd.read_csv('Train_Dataset.csv')
df_test = pd.read_csv('Test_Dataset.csv')

def drop_duplicates(df):
    print('No of duplicates: ' + str(df.duplicated().sum()))
    df.customer_id.drop_duplicates()
    df.drop_duplicates()

def d_types_report(df):
    columns=[]
    d_types=[]
    uniques=[]
    n_uniques=[]
    null_values=[]
    null_values_percentage=[]
    
    for i in df.columns:
        columns.append(i)
        d_types.append(df[i].dtypes)
        uniques.append(df[i].unique()[:5])
        n_uniques.append(df[i].nunique())
        null_values.append(df[i].isna().sum())
        null_values_percentage.append(null_values[-1] * 100 / rows)

    return pd.DataFrame({"Columns": columns, "Data_Types": d_types, "Unique_values": uniques, "N_Uniques": n_uniques,  "Null_Values": null_values, "Null_Values_percentage": null_values_percentage})
report = d_types_report(df)
report_test = d_types_report(df_test)

def imputing_missing(df):
    del df['Unnamed: 20']
    df_without_id = df.iloc[:, 1:]
    df = df_without_id
