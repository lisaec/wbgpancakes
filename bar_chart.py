import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

survey = pd.read_csv('survey_clean.csv')

#Making a bar chart of class and locations visited
class_loc = survey[['What is your Social Class?','Number of locations']]
class_loc.columns = ['class', 'num_loc']

avg_loc = class_loc.groupby(['class']).mean()
class_loc['class'].value_counts()

ax = avg_loc.plot.barh(figsize = [12,6],width=0.8, color = 'mediumorchid', rot = 0, fontsize = 12, linewidth = 1)
ax.tick_params(length=0)
[ax.spines[i].set_visible(False) for i in ax.spines]
plt.xlabel('Average Number of Restaurants Visited',fontsize = 16)
plt.ylabel('Social Class',fontsize = 16)
plt.yticks([4,3,2,1,0], labels = ['Graduate Students\n(3)', 'Class of 2027 \n(7)',
                                  'Class of 2026\n(21)','Class of 2025\n(39)','Class of 2024\n(42)'])

for i in range(len(ax.patches)):
    x,y,width,height = ax.patches[i].get_x(), ax.patches[i].get_y(), ax.patches[i].get_width(),\
        ax.patches[i].get_height()
    label = round(width, 2)
    plt.text(x+width-.4, y+height/2, label, ha = 'center', va = 'center', color = 'white', weight = 'bold')
    

ax.set_title('How Many of Williamsburg\'s Breakfast Restaurants Has the Average Student Visited?', x = 0.45, y = 1,
              size = 20, loc = 'center', ha = 'center')
ax.get_legend().remove()

plt.savefig('class_loc.png', bbox_inches = 'tight')