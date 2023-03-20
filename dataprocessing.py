import pandas as pd
import glob
# https://www.kaggle.com/datasets/unsdsn/world-happiness

wetern_europe = ['Finland', 'Denmark', 'Norway', 'Iceland', 'Netherlands', 'Switzerland', 'Sweden',
                 'Ireland', 'United Kingdom', 'Luxembourg', 'Germany', 'Belgium', 'France', 'Spain', 'Portugal', 'Italy']
central_europe = ['Austria', 'Czech Republic', 'Hungary',
                  'Liechtenstein', 'Poland', 'Slovakia', 'Slovenia', 'Greece', 'Bulgaria']
north_america = ['Canada', 'United States']
latin_america = ['Costa Rica', 'Mexico', 'Guatemala', 'Panama', 'Brazil', 'Uruguay',
                 'El Salvador', 'Argentina', 'Ecuador', 'Chile', 'Paraguay', 'Peru', 'Colombia', 'Jamaica', 'Bolivia', 'Venezuela']
central_america = ['El Salvador', 'Belize', 'Costa Rica',
                   'Guatemala', 'Honduras', 'Panama', 'Nicaragua']
middle_east_and_north_africa = ['Israel', 'United Arab Emirates', 'Saudi Arabia', 'Qatar', 'Bahrain', 'Kuwait', 'Libya',
                                'Morocco', 'Algeria', 'Lebanon', 'Iran', 'Tunisia', 'Iraq', 'Palestinian Territories', 'Syria', 'Yemen', 'Egypt']
asia_pacific = ['Australia', 'New Zealand', 'Taiwan', 'Singapore', 'Japan', 'South Korea', 'Hong Kong', 'Mongolia', 'North Macedonia', 'Vietnam', 'Cambodia', 'Philippines',
                'Pakistan', 'Russia', 'China', 'Bangladesh', 'Myanmar', 'Nepal', 'Sri Lanka', 'India', 'Indonesia', 'Thailand', 'Malaysia', 'Bhutan', 'Laos', 'Afghanistan']
sub_saharan_africa = ['Mauritius', 'Nigeria', 'Kenya', 'Mozambique', 'Tanzania', 'Cameroon', 'South Sudan', 'Central Africa Republic', 'Ghana', 'Ivory Coast', 'Senegal', 'Somalia', 'Namibia', 'Niger', 'Benin',
                      'Congo (Brazzaville)', 'Gabon', 'South Africa', 'Albania', 'Zimbabwe', 'Zambia', 'Togo', 'Liberia', 'Madagascar', 'Uganda', 'Burkina Faso', 'Mali', 'Sierra Leone', 'Burundi', 'Haiti', 'Botswana', 'Sudan', 'Angola', 'Oman', 'Suriname', 'Trinidad and Tobago', 'Djibouti']
eastern_europe_and_central_asia = ['Czech Republic', 'Malta', 'Poland', 'Slovakia', 'Hungary', 'Kosovo', 'Romania', 'Cyprus', 'Lithuania', 'Latvia', 'Estonia', 'Serbia', 'Moldova',
                                   'Montenegro', 'Croatia', 'Bosnia and Herzegovina', 'Belarus', 'Ukraine', 'Georgia', 'Armenia', 'Azerbaijan', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan', 'Turkey']


def assignRegions(country: str):
    if country in wetern_europe:
        return 'Western Europe'
    if country in central_europe:
        return 'Central Europe'
    elif country in north_america:
        return 'North America'
    elif country in latin_america:
        return 'Latin America'
    elif country in central_america:
        return 'Central America'
    elif country in middle_east_and_north_africa:
        return 'Middle East and North Africa'
    elif country in asia_pacific:
        return 'Asia Pacific'
    elif country in sub_saharan_africa:
        return 'Sub Saharan Africa'
    elif country in eastern_europe_and_central_asia:
        return 'Eastern Europe and Central Asia'
    else:
        return 'Uncategorized'


def processCSVs():
    # read all CSV files in the directory into a list of dataframes
    file_list = glob.glob('data/*.csv')
    df_list = []

    for f in file_list:
        # read the CSV file into a dataframe
        df = pd.read_csv(f)

        # extract the year from the filename
        year = f.split('data/')[-1].split('.')[0]
        # add the year column to the dataframe
        df['Year'] = year

        df['region_'] = df['country'].apply(assignRegions)

        # append the dataframe to the list
        df_list.append(df)

    # concatenate the dataframes along rows (i.e., append them)
    merged_df = pd.concat(df_list, axis=0, join='inner')

    # write the merged dataframe to a new CSV file
    merged_df.to_csv('merged.csv', index=False)


if __name__ == "__main__":
    processCSVs()
