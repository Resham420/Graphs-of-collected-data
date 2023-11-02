import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('EQ_fake.csv')


response_counts = df['Twitter _Intrested'].value_counts()


bar_colors = ['blue', 'green', 'orange', 'red']  
text_colors = 'black'


ax = response_counts.plot(kind='barh', color=bar_colors)  
plt.title('Survey Responses')
plt.xlabel('Count')
plt.ylabel('Options')

for i, v in enumerate(response_counts):
    ax.text(v + 1, i, str(v), color=text_colors, va='center', fontsize=10)


plt.show()

plt.savefig('survey_chart.png')
