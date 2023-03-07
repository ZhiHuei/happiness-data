import pandas as pd
import glob

# read all CSV files in the directory into a list of dataframes
file_list = glob.glob('data/*.csv')
df_list = []


for f in file_list:
    # read the CSV file into a dataframe
    df = pd.read_csv(f)

    # extract the year from the filename
    year = f.split('data/')[-1].split('.')[0]
    print(year)

    # add the year column to the dataframe
    df['Year'] = year

    # append the dataframe to the list
    df_list.append(df)

# concatenate the dataframes along rows (i.e., append them)
merged_df = pd.concat(df_list, axis=0, join='inner')

# write the merged dataframe to a new CSV file
merged_df.to_csv('merged.csv', index=False)
