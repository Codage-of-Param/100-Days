# 📁 Working with CSV Files — Day 10 of 100 Days of Machine Learning

## Overview

This lesson introduces how to work with **CSV (Comma Separated Values)** data in Python — a common task in data science and machine learning. Topics include:

* What a CSV file is
* Why CSV files are important in data science
* Reading CSV files with Python
* Manipulating and exploring data
* Basic operations for machine learning preprocessing

---

## What Is a CSV File?

A **CSV file** is a simple text format used to store tabular data. Each line represents a row, and commas separate columns.

Example:

```
name,age,height
Alice,30,5.5
Bob,25,6.0
```

---

## Why Use CSV in Machine Learning?

* Universal format supported by most tools
* Easy to import/export
* Can be opened in spreadsheets
* Often used for datasets in ML competitions

---

## Python Tools for CSV

### Pandas

Pandas is the most commonly used library in Python for handling CSV data.

```python
import pandas as pd
```

---

## Reading a CSV File

### Basic CSV Load

```python
df = pd.read_csv('data.csv')
```

* `df` becomes a DataFrame — a table-like structure
* Pandas automatically infers column names

---

## Exploring the Data

### View First Few Rows

```python
df.head()
```

* Shows first 5 rows by default

### Check Shape

```python
df.shape
```

* Returns (rows, columns)

### Column Names

```python
df.columns
```

### Summary Statistics

```python
df.describe()
```

* Shows count, mean, std, min, max for numeric columns

---

## Accessing Columns

```python
df['column_name']
```

or multiple columns:

```python
df[['col1', 'col2']]
```

---

## Filtering Data

Example: rows where a value meets a condition:

```python
df[df['age'] > 30]
```

---

## Handling Missing Data

### Check for Missing

```python
df.isnull().sum()
```

### Drop Missing Rows

```python
df.dropna(inplace=True)
```

### Fill Missing Values

```python
df.fillna(0, inplace=True)
```

---

## Exporting to CSV

After manipulation, save the DataFrame:

```python
df.to_csv('clean_data.csv', index=False)
```

* `index=False` prevents saving row numbers as a column

---

## Using CSV for Machine Learning

Typical ML workflow with CSV data:

1. Load data
2. Clean and preprocess
3. Select features/labels
4. Split into train/test sets
5. Fit ML model
6. Evaluate

Example of splitting:

```python
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## Summary

* CSV files are foundational to data handling in ML
* Pandas simplifies reading and writing CSV files
* Explore and clean data before modeling
* Use common ML utilities (like scikit-learn) for preprocessing and training

---
