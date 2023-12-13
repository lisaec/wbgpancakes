import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pywaffle import Waffle

#importing survey results
survey = pd.read_csv('survey_clean.csv')


#Creating Waffle plot
waffle = survey['pancakes_waffles'].dropna().value_counts()

waffle = (waffle/waffle.sum()*100).apply(round)

colors=['pink','mediumorchid']
title = {'label': "Most Respondents Preferred\nPancakes to Waffles",
        'loc': 'center',
        'fontdict': {'fontsize': 22}}

fig = plt.figure(
    figsize = [8,8],
    FigureClass=Waffle,
    columns=10,
    values=list(waffle.values),
    colors=colors,
    font_size=10,
    vertical= True,
    starting_location = 'NW',
    title=title
    )


plt.text(1.03, 0.62, '81 students prefer pancakes', va = 'bottom', color = 'dimgrey', weight = 'bold', fontsize = 14)
plt.text(1.03, 0.11, '30 students prefer waffles', va = 'bottom', color = 'dimgrey', weight = 'bold', fontsize = 14)
plt.savefig('pancake_waffle.png', bbox_inches = 'tight')
