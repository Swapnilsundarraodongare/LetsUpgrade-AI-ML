# IPython log file

import pandas as pd
data1=pd.read_csv("general_data.csv")
data1.head()
#[Out]#    Age Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
#[Out]# 0   51        No  ...                       0                    0
#[Out]# 1   31       Yes  ...                       1                    4
#[Out]# 2   32        No  ...                       0                    3
#[Out]# 3   38        No  ...                       7                    5
#[Out]# 4   32        No  ...                       0                    4
#[Out]# 
#[Out]# [5 rows x 24 columns]
d={"Yes":1,"No":0}
data2=data1.replace(d)
data2.isnull
#[Out]# <bound method DataFrame.isnull of       Age  Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
#[Out]# 0      51          0  ...                       0                    0
#[Out]# 1      31          1  ...                       1                    4
#[Out]# 2      32          0  ...                       0                    3
#[Out]# 3      38          0  ...                       7                    5
#[Out]# 4      32          0  ...                       0                    4
#[Out]# ...   ...        ...  ...                     ...                  ...
#[Out]# 4405   42          0  ...                       0                    2
#[Out]# 4406   29          0  ...                       0                    2
#[Out]# 4407   25          0  ...                       1                    2
#[Out]# 4408   42          0  ...                       7                    8
#[Out]# 4409   40          0  ...                       3                    9
#[Out]# 
#[Out]# [4410 rows x 24 columns]>
data2.dropna()
#[Out]#       Age  Attrition  ... YearsSinceLastPromotion YearsWithCurrManager
#[Out]# 0      51          0  ...                       0                    0
#[Out]# 1      31          1  ...                       1                    4
#[Out]# 2      32          0  ...                       0                    3
#[Out]# 3      38          0  ...                       7                    5
#[Out]# 4      32          0  ...                       0                    4
#[Out]# ...   ...        ...  ...                     ...                  ...
#[Out]# 4404   29          0  ...                       1                    5
#[Out]# 4405   42          0  ...                       0                    2
#[Out]# 4406   29          0  ...                       0                    2
#[Out]# 4407   25          0  ...                       1                    2
#[Out]# 4408   42          0  ...                       7                    8
#[Out]# 
#[Out]# [4382 rows x 24 columns]
from scipy.stats import manwhitneyu
from scipy.stats import mannwhitneyu
data_yes=dataframe(data2.Attrition!="NO")
data_yes=dataframe[data2.Attrition!="NO"]
data_yes=dataframe[[data2.Attrition!="NO"]]
data_yes=data2[data2.Attrition!="NO"]
data_yes=data2[data2.Attrition!=1]
data_NO=data2[data2.Attrition!=1]
data_Yes=data2[data2.Attrition!=0]
data_yes=data2[data2.Attrition!=0]
stats,p=mannwhitneyu(data_yes.MonthlyIncome,data_NO.MonthlyIncome)
data_yes=data2[data2.JobLevel!={1,2,3}]
data_Job4=data2[data2.JobLevel!={1,2,3}]
data_Job1=data2[[data2.JobLevel!=4,data2.JobLevel!=3,data2.JobLevel!=2]

data_Job1=data2[[data2.JobLevel!=4,data2.JobLevel!=3,data2.JobLevel!=2]
data_Job1=data2[[data2.JobLevel!=4,data2.JobLevel!=3,data2.JobLevel!=2]]
data_Job1=data2[[data2.JobLevel!=4 &data2.JobLevel!=3 & data2.JobLevel!=2]]
data_Job1=data2[[data2.JobLevel!=4 & data2.JobLevel!=3 & data2.JobLevel!=2]]
data_Job1=data2[(data2.JobLevel!= 4) & (data2.JobLevel!=3) & (data2.JobLevel!=2)]
data_Job2=data2[(data2.JobLevel!= 4) & (data2.JobLevel!=3) & (data2.JobLevel!=1)]
data_Job3=data2[(data2.JobLevel!= 4) & (data2.JobLevel!=2) & (data2.JobLevel!=1)]
data_Job4=data2[(data2.JobLevel!= 3) & (data2.JobLevel!=2) & (data2.JobLevel!=1)]
from scipy.stats import krushkal
from scipy.stats import kruskal
kruskal_value=kruskal(data_Job1,data_Job2,data_Job3,data_Job4)
kruskal_value=kruskal(data_Job1.JobLevel,data_Job2.JobLevel,data_Job3.JobLevel,data_Job4.JobLevel)
kruskal_value=kruskal(data_Job1.MonthlyIncome,data_Job2.MonthlyIncome,data_Job3.MonthlyIncome,data_Job4.MonthlyIncome)
kruskal_value=kruskal(data_Job1.MonthlyIncome,data_Job2.MonthlyIncome,data_Job3.MonthlyIncome,data_Job4.MonthlyIncome)
from scipy.stats import chi2_contingency
chitable=data2.crosstab(data2.Gender,data2.JobLevel)
chitable=data2.crosstab(data2.Gender,data2.JobLevel)
data2.crosstab(data2.Gender,data2.JobLevel)
chtable=crosstab(data2.Gender,data2.JobLevel)
import researchpy
chtable=data2.crosstab(data2.Gender,data2.JobLevel)
chtable=pd.crosstab(data2.Gender,data2.JobLevel)
chi_test=chi2_contingency(chtable)
stats_chi,p_chi,dof,expeted=chi2_contingency(chtable)
