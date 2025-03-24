import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', na_values=['?']) # There are '?' symbols for unknown values in the dataset, so I converte those to NaN.

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    # percentage = Number of Bachelor's / Total * 100
    bachelors_mask = df['education'] == 'Bachelors'
    percentage_bachelors = bachelors_mask.sum() / bachelors_mask.size * 100
    # percentage_bachelors = bachelors_mask.sum() / df['education'].size * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    higher_education = df.loc[mask]
    lower_education = df.loc[~mask]

    # percentage with salary >50K
    higher_education_rich = (higher_education['salary'] == '>50K').sum() / higher_education['education'].size * 100
    lower_education_rich = (lower_education['salary'] == '>50K').sum() / lower_education['education'].size* 100
    # I use 'education' column, and then .size in both dfs just to count the total of people in each respective one

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == min_work_hours # mask of people who work the minimum hours per week
    min_workers_df = df.loc[mask] # df of those people
    num_min_workers = mask.sum() # number or people who work the minimun hours

    rich_percentage =  (min_workers_df['salary'] == '>50K').sum() / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    # I calculate the series percentage through the total count of people whose salary is >50K of each country, 
    # dividing it by the total count of people of the respective country.
    s = df.loc[df['salary']=='>50K', 'native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = s[ s == s.max() ].index[0] # Filtering the max percentage, and getting the index of the first one 
    highest_earning_country_percentage = s.max() # max percentage

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[ (df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts().index[0]
    # I get occupation column from people whose native country is India and earn >50K
    # Then I use value_counts() for counting occupations and finally get the firs index wich is the most popular.
    
    # Rounding the calculations to the nearest tenth
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
