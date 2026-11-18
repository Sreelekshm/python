# import matplotlib.pyplot as plt
# # values=["product A","product B", "product C "]
# # sales =[50,30,20]
# # plt.pie(sales,labels=values,autopct='%1.1f%%',explode=[0.1,0,0],startangle=90)
# # plt.show()


# # marks=[45,55,60,65,70,75,80,85,90,95]
# # plt.hist(marks,bins=5)
# # plt.title('marks distribution')
# # plt.xlabel('marks')
# # plt.ylabel('number of students')
# # plt.show()


# salaries =[25000,30000,32000,40000,100000]
# plt.boxplot(salaries)
# plt.title('salary distribution')
# plt.ylabel('salary')
# plt.show()







import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data ={
#     'department':['IT','HR','FINANCE','HR','IT'],
#     'salary':[50000,45000,60000,48000,70000]
# }
# df =pd.DataFrame(data)
# sns.barplot(x='department',y='salary',data=df)
# plt.title('average salary by department')
# plt.show()


# data={
#    'month':['Jan','Feb','Mar','Apr'],
#    'sales':[20000,25000,30000,28000]
# }
# df =pd.DataFrame(data)
# sns.lineplot(x='month',y='sales',data=df)
# plt.title('monthly sales trend')
# plt.show()




# data ={
#     'sales':[100,200,300,400,500],
#     'profit':[20,40,60,80,100],
#     'discount':[5,10,15,20,25]
#     }

# df =pd.DataFrame(data)
# corr=df.corr()
# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.title('correlation heatmap')
# plt.show()




data={
    'Age':[22,25,28,30,35],
    'Salary':[25000,30000,40000,45000,60000],
    'Experience':[1,2,4,5,8]
}
df=pd.DataFrame(data)
sns.pairplot(df)
plt.show()