# # #Soru 1 Cevabı: 

# # import seaborn as sns
# # import pandas as pd
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', 500)

# # df = sns.load_dataset("car_crashes")
# # df.columns
# # print(df.head())


# # name_changer = [("NUM_" + col.upper()) if df[col].dtypes in ["int64", "float64"] else col.upper() for col in df.columns]

# # print(name_changer)


# #Soru 2 Cevabı: 
# # import seaborn as sns
# # import pandas as pd
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', 500)

# # df = sns.load_dataset("car_crashes")
# # df.columns

# # name_changer_2 = [(col + "FLAG") for col in df.columns if not "no" in col]
# # print(name_changer_2)

# #Soru 3 Cevabı: 
# # import seaborn as sns
# # import pandas as pd
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', 500)

# # df = sns.load_dataset("car_crashes")
# # df.columns 

# # og_list = ["abbrev", "no_previous"]

# # new_df_creator = [col for col in df.columns if not col in og_list]

# # new_df = pd.DataFrame(df[new_df_creator])

# # print(new_df.head())



# #Pandas Alıştırmaları 
# #Soru 1 Cevabı: 
# # import numpy as np
# # import seaborn as sns
# # import pandas as pd
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', 1000)

# # df = sns.load_dataset("Titanic")


# # #Soru 2 Cevabı
# # import numpy as np
# # import seaborn as sns
# # import pandas as pd
# # pd.set_option('display.max_rows', None)
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.width', 1000)

# # df = sns.load_dataset("titanic")

# # print(df.head())
# # print(df["sex"].value_counts())



# #Soru3 
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")





# print(df.nunique())


# #Soru 4 

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")





# print(df["pclass"].unique())

# #Soru 5 

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")





# print(df[["pclass","parch"]].nunique())


# #Soru 6

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")





# print(df["embarked"].dtypes)

# df["embarked"].astype('category')

# print(df["embarked"].dtypes)

#Soru 7 

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")


# new_df = df[df["embarked"] == "C"]

# print(new_df)



#Soru 8

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")


# new_df = df[df["embarked"] != "S"]

# print(new_df.head())

#Soru9

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# new_df = df[(df["age"] < 30) & (df["sex"] == "female")]
# print(new_df)

#Soru10 
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# new_df = df[(df["fare"] > 500) | (df["age"] > 70)]
# print(new_df)

#Soru 11
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# print(df.isnull().sum(axis = 0))

#Soru 12 

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# df.drop(columns = ['who'],inplace=True)
# print(df.head())

# #Soru 13
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# print(df["deck"].isnull().any())

# df["deck"].fillna(df["deck"].mode(), inplace = True)

# print(df["deck"].isnull().any())

# #Soru14
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# print(df["age"].isnull().any())

# df["age"].fillna(df["age"].median(), inplace = True)

# print(df["age"].isnull().any())


#Soru 15
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# print(df.groupby(["pclass","sex"])["survived"].aggregate([sum,'count','mean']))

#Soru 16 

# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("titanic")

# def changer(df):
#     new_df = df["age"].apply(lambda x: 1 if x < 30 else 0)
#     print(new_df.head())
    

# changer(df)

#Soru 17 -18
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("tips")

# print(df.head())

# print(df.groupby("time")["total_bill"].aggregate([sum,min,max,mean]))

#Soru 19 
# from statistics import mean
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("tips")

# print(df.head())

# print(df.groupby(["day","time"])["total_bill","tip"].aggregate([sum,min,max,mean]))

#Soru20(Diğer değerleri Null olark elde ettim, başardım sayılır ama dönüp bakacağım tekrar.)

# from statistics import mean
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("tips")

# print(df.head())

# print(df.query('sex == "Female" and time == "Lunch"').groupby(["time","sex"])["total_bill","tip"].aggregate([sum,min,max,mean]))

#Soru 21 

# from statistics import mean
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("tips")
# print(df.head())
# print(df.query('size < 3 and total_bill > 10').groupby("size")["total_bill"].mean())

# #Soru 22 -23

# from statistics import mean
# import numpy as np
# import seaborn as sns
# import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# df = sns.load_dataset("tips")
# print(df.head())

# df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

# print(df.sort_values(by="total_bill_tip_sum", ascending = False))




