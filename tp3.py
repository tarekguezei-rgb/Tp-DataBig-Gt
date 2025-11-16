import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('sales_data_large.csv')

# Clean
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)
data['date'] = pd.to_datetime(data['date'])

# Outliers
data = data[(zscore(data['sales']) < 3)]

# EDA
print(data.describe())
sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()

data.groupby('date')['sales'].sum().plot(kind='line')
plt.show()

# Top products
top_products = data.groupby('product')['sales'].sum().nlargest(10)
top_products.plot(kind='bar')
plt.show()

# Regression example
X = data.select_dtypes(include=['number']).drop(columns=['sales'])
y = data['sales']

model = LinearRegression()
model.fit(X, y)
preds = model.predict(X)
preds[:5]