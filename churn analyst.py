import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\Users\Sonal deep Gupta\Downloads\European_Bank.csv")
data = data.drop(columns=['Surname'])
data['geo_segment'] = data['Geography'].map({
    'France': 'France',
    'Spain': 'Spain',
    'Germany': 'Germany'
})
data["AgeGroup"] = pd.cut(
    data["Age"],
    bins=[0, 30, 45, 60, 100],
    labels=["<30", "30-45", "46-60", "60+"]
)
data["CreditScoreBand"] = pd.cut(
    data["CreditScore"],
    bins=[0, 579, 669, 850],
    labels=["Low", "Medium", "High"]
)
data['Tenure_group'] = pd.cut(
    data['Tenure'],
    bins=[0,1,3,50],
    labels=['New','Mid-term','Long-term']
)
data["BalanceSegment"] = pd.cut(
    data["Balance"],
    bins=[-1, 0, 50000, data["Balance"].max()],
    labels=["Zero-balance", "Low-balance", "High-balance"]
)
overall_churn_rate = data["Exited"].mean() * 100
geo_churn = data.groupby("Geography")["Exited"].mean() * 100
age_churn = data.groupby("AgeGroup", observed=False)["Exited"].mean() * 100
churn_contribution = (
    data[data["Exited"] == 1]
    .groupby("Geography")
    .size()
    / data[data["Exited"] == 1].shape[0]
) * 100
profile_comparison = data.groupby("Exited").mean(numeric_only=True)
gender_churn_rate = data.groupby("Gender")["Exited"].mean() * 100
gender_distribution = data["Gender"].value_counts(normalize=True) * 100
'''geo_age_churn = (
    data.groupby(["Geography", "AgeGroup"])["Exited"]
    .mean()
    .unstack()
) * 100'''
high_value = data[data["Balance"]=="High"]

high_value_churn = high_value["Exited"].mean()*100
print("High Value Customer Churn:", high_value_churn)
sns.scatterplot(x="EstimatedSalary", y="Balance", hue="Exited", data=data)
plt.show()
pivot = pd.pivot_table(
    data,
    values="Exited",
    index="Geography",
    columns="AgeGroup",
    aggfunc="mean",
    observed=False
)
print(pivot)
sns.heatmap(pivot, annot=True, cmap="coolwarm")
plt.show()

# KPI Calculation

data["Exited"].mean()*100
data.groupby("AgeGroup", observed=False)["Exited"].mean()*100
data.groupby("Geography")["Exited"].mean()*100
high_value["Exited"].mean()*100
print(data)


''' Insights Example (For Research Paper)

1.Germany has highest churn rate
2.Customers aged 46–60 churn more
3.Inactive members churn significantly higher
4.High-balance customers leaving = revenue risk'''

'''Recommendations

Banks should:
1.Target high-balance customers
2.Improve customer engagement programs
3.Monitor Germany region churn
4.Provide loyalty benefits for long-tenure customers'''


