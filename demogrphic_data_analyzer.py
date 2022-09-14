from collections import Counter
import pandas as pd
import numpy as np

def calculate_demographic_data(print_data = True):
    # Read data from file
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    csv = pd.read_csv("./adult.data.csv")

    # Race count
    race = csv['race']
    race_list = [i for i in race]
    race_dict = {}
    race_dict["race_count"] = {}
    for i in race_list:
        if i in race_dict["race_count"].keys():
            race_dict["race_count"][i] += 1
        else:
            race_dict["race_count"][i] = 1
    race_count = pd.DataFrame(race_dict)
    race_count.set_index("race_count")
    
    # Average Men Age
    men = csv.loc[csv['sex'] == 'Male']
    men_age = men['age']
    men_list = [i for i in men_age]
    average_age_men = round(sum(men_list) / len(men_list), 1)

    # Bachelor Percentage
    education = csv['education']
    bachelors = csv.loc[csv['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / len(education) * 100), 1)

    # Higher education rich
    advance_education = csv.loc[csv['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich = advance_education.loc[advance_education['salary'] == '>50K']
    higher_education_rich = round(((len(rich) / len(advance_education)) * 100), 1)

    # Lower education rich
    lower_education = csv.loc[~csv['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich = lower_education.loc[lower_education['salary'] == '>50K']
    lower_education_rich = round(((len(rich) / len(lower_education)) * 100), 1)

    # Min work hours
    min_work_hours = min(csv['hours-per-week'])

    # Rich percentage
    min_hours = csv.loc[csv['hours-per-week'] == 1]
    salary_for_min_hours = min_hours.loc[min_hours['salary'] == '>50K']
    rich_percentage = int(((len(salary_for_min_hours) / len(min_hours)) * 100))

    # Highest earning country
    con_sm = csv.loc[csv['salary'] == '>50K']
    con_li = [i for i in con_sm['native-country']]
    mc = Counter(con_li).most_common()
    highest_earning_country = mc[0][0]
    highest_earning_country_percentage = ((mc[0][1]) / len(con_li)) * 100

    # Top occupation in india
    india = csv.loc[csv['native-country'] == 'India']
    india_rich = india.loc[india['salary'] == '>50K']
    india_rich_list = [i for i in india_rich['occupation']]
    most_common = Counter(india_rich_list).most_common()
    top_IN_occupation = most_common[0][0]
    if print_data == True:
        print(race_count)
        print(average_age_men)
        print(percentage_bachelors)
        print(higher_education_rich)
        print(lower_education_rich)
        print(min_work_hours)
        print(rich_percentage)
        print(highest_earning_country) 
        print(highest_earning_country_percentage)
        print(top_IN_occupation)
    else:
        data = {}
        data['race_count'] = race_count 
        data['average_age_men'] = average_age_men
        data['percentage_bachelors'] = percentage_bachelors
        data['higher_education_rich'] = higher_education_rich
        data['lower_education_rich'] = lower_education_rich
        data['min_work_hours'] = min_work_hours
        data['rich_percentage'] = rich_percentage
        data['highest_earning_country'] = highest_earning_country
        data['highest_earning_country_percentage'] = highest_earning_country_percentage
        data['top_IN_occupation'] = top_IN_occupation
        return data
    
