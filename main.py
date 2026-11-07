import pandas as pd
import numpy as np

# 1
# s = pd.Series(np.linspace(0, 20, 15))
# s1 = s / s.shift(1)
# result = s1[s1 <= 1.5].mean()
# print(result)

# 2
# s = pd.Series(data=['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98],
#               index=range(6, 26, 2))
# s_new = pd.Series(data=s.values, index=range(2, 12))
# result_sum = s_new.iloc[2] + s_new.iloc[4]
# print(result_sum)
# only_digits = [x for x in s if type(x) == int]
# dispersia = np.var(only_digits)
# print(round(dispersia, 2))

# 3
# np.random.seed(242)
# s = pd.Series(np.random.normal(size=100))
# s = s ** 3
# s.index = s.index * 3
# result_sum = s[(s < 2.6) & (s.index % 2 != 0)].sum()
# negative_count = (s < 0).sum()
# print(result_sum)
# print(negative_count)

# 4
# tr_type = pd.read_csv("data/tr_types.csv", sep=";")
# sample = tr_type.sample(n=100, random_state=242)
# share = (sample["tr_description"]
#          .str.lower()
#          .str.contains("плата")
#          .mean())
# print(round(share, 2))

# 5
# transactions = pd.read_csv("data/transactions.csv")
# top = transactions["tr_type"].value_counts()
# print(top.head(5))

# 6
# transactions = pd.read_csv("data/transactions.csv")
# transactions = transactions.set_index("customer_id")
# max_amount = transactions["amount"].max()
# customer_max = transactions["amount"].idxmax()
# print(customer_max, max_amount)

# 7
# transactions = pd.read_csv("data/transactions.csv", nrows=1000000)
# tr_mcc_codes = pd.read_csv("data/tr_mcc_codes.csv", sep=";")
# tr_types = pd.read_csv("data/tr_types.csv", sep=";")
# gender_train = pd.read_csv("data/gender_train.csv")
#
# transactions = transactions.merge(tr_mcc_codes, on="mcc_code", how="inner")
# transactions = transactions.merge(tr_types, on="tr_type", how="inner")
# transactions = transactions.merge(gender_train, on="customer_id", how="left")
# print(len(transactions))

# 8
# transactions = pd.read_csv("data/transactions.csv")
# tr_mcc_codes = pd.read_csv("data/tr_mcc_codes.csv", sep=";")
# tr_types = pd.read_csv("data/tr_types.csv", sep=";")
# gender_train = pd.read_csv("data/gender_train.csv")
#
# transactions = transactions.merge(tr_mcc_codes, on="mcc_code", how="inner")
# transactions = transactions.merge(tr_types, on="tr_type", how="inner")
# transactions = transactions.merge(gender_train, on="customer_id", how="left")
#
# spends = transactions[transactions["amount"] < 0]
# groups_by_gender = spends.groupby("gender")["amount"].mean()
#
# women = groups_by_gender.iloc[0]
# men = groups_by_gender.iloc[1]
#
# diff = abs(men - women)
# print(round(diff, 2))

# 9
transactions = pd.read_csv("data/transactions.csv")
tr_mcc_codes = pd.read_csv("data/tr_mcc_codes.csv", sep=";")
tr_types = pd.read_csv("data/tr_types.csv", sep=";")
gender_train = pd.read_csv("data/gender_train.csv")

transactions = transactions.merge(tr_mcc_codes, on="mcc_code", how="inner")
transactions = transactions.merge(tr_types, on="tr_type", how="inner")
transactions = transactions.merge(gender_train, on="customer_id", how="left")

transactions["mcc_code_tr_type"] = (
    transactions["mcc_code"].astype(str) + "_" + transactions["tr_type"].astype(str)
)
transactions_negative = transactions[transactions["amount"] < 0]
print(transactions_negative)