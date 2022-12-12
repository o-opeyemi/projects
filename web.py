from urllib.request import urlopen
import os
import psycopg2
import re
from random import randrange
# Filter out all colours
url = os.getcwd() + "\webapp\python_class_question.html"
page = open(url, 'r')
html = page.read()
html = html.replace("\n", "")
html = html.replace(" ", "")
r = re.findall("<td>([A-Z,]+)", html)
colors = []
for i in r:
    if "," in i:
        pass
    else:
        r.remove(i)
for i in r:
    day_colors = i.split(",")
    for color in day_colors:
        colors.append(color)

#  To find the mean
def mean_color(colors):
    color_dict = {}
    for i in colors:
        if i in color_dict.keys():
            color_dict[i] += 1
        else:
            color_dict[i] = 1
    color_dict = sorted(color_dict)
    print(color_dict)
    mean_value = len(colors) / len(color_dict)
    return mean_value

# Most colours worn throughtthe week
def most_color_worn(colors):   
    color_dict = {}
    for i in colors:
        if i in color_dict.keys():
            color_dict[i] += 1
        else:
            color_dict[i] = 1
    hightest_value = max(color_dict.values())
    for i in color_dict.keys():
        if hightest_value == color_dict[i]:
            return i
        else:
            pass

# Median Colour
def median_color(colors):
    color_dict = {}
    for i in colors:
        if i in color_dict.keys():
            color_dict[i] += 1
        else:
            color_dict[i] = 1
    median_value = len(colors)/2
    keys = sorted(color_dict.keys())
    summattion = 0
    for i in keys:
        summattion += color_dict[i]
        if summattion >= median_value:
            median_color_name = i
            break
        else:
            pass
    print(median_color_name)

# Convert generated Base 2 to Base `0`
def convert_4_digits_base_2_to_base_10():
    base2_list = []
    for i in range(4):
        base2_list.append(str(randrange(0, 2)))
    base2 = "".join(base2_list)
    base10 =int(base2, base=2)
    print(base10)
 
# Put data into postgresql
# connection establishment
conn = psycopg2.connect(
   database="data",
    user='postgres',
    password='root',
    host='localhost',
    port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()
sql = '''CREATE TABLE COLOURS(value int NOT NULL);'''
cursor.execute(sql)
color_dict = {}
for i in colors:
    if i in color_dict.keys():
        color_dict[i] += 1
    else:
        color_dict[i] = 1
columns= color_dict.keys()
for i in color_dict.values():
    sql2='''insert into DETAILS(value) VALUES{};'''.format(i)
 
    cursor.execute(sql2)
 
sql3='''select * from DETAILS;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
conn.commit()
conn.close()


# Calculate first 50 fibonacci
def fibonacci_first_50():
    x,y=0,1
    fibonacci_list = []
    while y<50:
        fibonacci_list.append(y)
        x,y = y,x+y
    return sum(fibonacci_list)
        