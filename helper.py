import numpy as np


def fetch_medal_taily(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == "Overall" and country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != "Overall" and country == "Overall":
        temp_df = medal_df[medal_df["Year"] == int(year)]
    if year != "Overall" and country != "Overall":
        temp_df = medal_df[(medal_df["Year"] == year) & (medal_df["region"] == country)]
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x["Gold"] + x["Silver"] + x["Bronze"]

    x["Gold"] = x["Gold"].astype("int")
    x["Silver"] = x["Silver"].astype("int")
    x["Bronze"] = x["Bronze"].astype("int")
    x["total"] = x["total"].astype("int")

    return x


def medal_taliy(df):
    medal_taily = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_taily = medal_taily.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
ascending=False).reset_index()

    medal_taily["total"] = medal_taily["Gold"] + medal_taily["Silver"] + medal_taily["Bronze"]

    medal_taily["Gold"]  = medal_taily["Gold"].astype("int")
    medal_taily["Silver"] = medal_taily["Silver"].astype("int")
    medal_taily["Bronze"] = medal_taily["Bronze"].astype("int")
    medal_taily["total"] = medal_taily["total"].astype("int")

    return medal_taily


def country_year_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df["region"].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years,country

def  data_Over_time(df,col):
    nations_Over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
    nations_Over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
    return nations_Over_time


def most_successful(df, sport):
    temp_df = df.dropna(subset=["Medal"])

    if sport != "Overall":
        temp_df = temp_df[temp_df["Sport"] == sport]

    x = temp_df['Name'].value_counts().reset_index().head(15).merge(df, left_on='index', right_on="Name", how="left")[
        ['index', "Name_x", 'Sport', 'region']].drop_duplicates('index')
    x.rename(columns={"index": "Name", "Name_x": "Medals"}, inplace=True)
    return x

def yearwise_medal_taily(df,country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df["region"] == country]
    final_df = new_df.groupby("Year").count()["Medal"].reset_index()
    return final_df


def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df["region"] == country]
    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)

    return pt


def most_successful_countrywise(df, country):
    temp_df = df.dropna(subset=["Medal"])

    temp_df = temp_df[temp_df["region"] == country]

    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='index', right_on="Name", how="left")[
        ['index', "Name_x", 'Sport']].drop_duplicates('index')
    x.rename(columns={"index": "Name", "Name_x": "Medals"}, inplace=True)
    return x

