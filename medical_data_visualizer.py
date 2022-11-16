import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', header=0)

# Calculating the BMI
bmi = df['weight'] / (df['height']/100)**2 
# Creating a new column that represents the BMI.
df["overweight"] = bmi

# Normalize data by making 0 always good and 1 always bad.
# If the value of overweight is greater than 25 make the value 1 or else make the value 0
df.overweight = df.overweight.apply(lambda x: 1 if x > 25 else 0)
# If the value of cholestorol  is 1, make the value 0 or else if the value is more than 1, make the value 1.
df.cholesterol = df.cholesterol.apply(lambda x: 1 if x> 1 else 0)
# If the value of gluc is 1, make the value 0 or else if the value is more than 1, make the value 1.
df.gluc = df.gluc.apply(lambda x: 1 if x> 1 else 0)

# Draw Cat Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', col='cardio', hue='value', data=df_cat, kind='count')
    g.set_axis_labels("variable", "total")
    fig = g.fig

    # Generate the catplot image
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
	df_heat = df 

    # Clean the data
	df_heat = df_heat[(df_heat["ap_lo"] <= df_heat["ap_hi"]) &
	(df_heat['height'] >= df_heat["height"].quantile(0.025)) &
	(df_heat['height'] <= df_heat["height"].quantile(0.975)) &
	(df_heat['weight'] >= df_heat["weight"].quantile(0.025)) &
	(df_heat['weight'] <= df_heat["weight"].quantile(0.975))
	]

    # Calculate the correlation matrix
	corr = df_heat.corr()

    # Generate a mask for the upper triangle
	mask = np.triu(corr)
	corr = round(corr, 1)
    
    # Draw the heatmap
	with sns.axes_style("white"):
		fig, axis = plt.subplots(figsize=(15, 12))
		axis = sns.heatmap(corr, vmin=0.05, vmax=0.25, mask=mask, 
			fmt='.1f',
			annot=True,
        )
    

    # Do not modify the next two lines
	fig.savefig('heatmap.png')
	return fig