import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження даних
df = pd.read_csv('Walmart.csv')

# Перетворення колонки 'Date' на формат дати
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Загальний огляд даних
print(df.head())
print(df.info())

# Описова статистика
print(df.describe())

# Візуалізація продажів по тижнях
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Weekly_Sales'], marker='o', linestyle='-', color='b')
plt.title('Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.grid(True)
plt.show()

# Візуалізація продажів по магазинам
plt.figure(figsize=(14, 7))
sns.boxplot(x='Store', y='Weekly_Sales', data=df)
plt.title('Weekly Sales Distribution by Store')
plt.xlabel('Store')
plt.ylabel('Weekly Sales')
plt.show()

# Вплив святкових тижнів на продажі
plt.figure(figsize=(14, 7))
sns.boxplot(x='Holiday_Flag', y='Weekly_Sales', data=df)
plt.title('Impact of Holidays on Weekly Sales')
plt.xlabel('Holiday Flag (0 = Non-Holiday, 1 = Holiday)')
plt.ylabel('Weekly Sales')
plt.show()

# Взаємозв'язок між ціною на паливо та продажами
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Fuel_Price', y='Weekly_Sales', data=df, hue='Store', palette='tab10')
plt.title('Fuel Price vs Weekly Sales')
plt.xlabel('Fuel Price')
plt.ylabel('Weekly Sales')
plt.legend(title='Store')
plt.show()

# Взаємозв'язок між безробіттям та продажами
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Unemployment', y='Weekly_Sales', data=df, hue='Store', palette='tab10')
plt.title('Unemployment vs Weekly Sales')
plt.xlabel('Unemployment')
plt.ylabel('Weekly Sales')
plt.legend(title='Store')
plt.show()

# Взаємозв'язок між CPI та продажами
plt.figure(figsize=(14, 7))
sns.scatterplot(x='CPI', y='Weekly_Sales', data=df, hue='Store', palette='tab10')
plt.title('CPI vs Weekly Sales')
plt.xlabel('CPI')
plt.ylabel('Weekly Sales')
plt.legend(title='Store')
plt.show()

# Взаємозв'язок між температурою та продажами
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Temperature', y='Weekly_Sales', data=df, hue='Store', palette='tab10')
plt.title('Temperature vs Weekly Sales')
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.legend(title='Store')
plt.show()
