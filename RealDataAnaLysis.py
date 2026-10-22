import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# 1. فهم البيانات
print(df.shape)
print(df.info())
print(df.isna().sum())

# 2. التنظيف
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.drop(columns=["Cabin"])

# 3. التحليل
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())

# 4. الرسم
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("نسبة النجاة حسب الدرجة")
plt.ylabel("نسبة النجاة")
plt.savefig("survival_by_class.png")
plt.show()