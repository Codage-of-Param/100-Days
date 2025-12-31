# **Exploratory Data Analysis (EDA)**

- Exploratory Data Analysis (EDA) is ***the process of analyzing and summarizing datasets to understand their main characteristics before applying statistical modeling*** or machine learning.

- It mostly uses **statistical measures** and **visual representations**.

- EDA helps discover **patterns, spot anomalies, and check assumptions**.

---

# **Univariate Analysis** 

* Definition: 

    - Univariate analysis is the simplest form of EDA that ***focuses on one variable at a time***.

    - It helps you understand the **distribution, central tendency, dispersion**, and overall characteristics of that single variable without considering relationships with other variables

    - Dispersion is is the extent to which a distribution is stretched or squeezed.

 
# Purposes of Univariate Analysis

- To summarize data for one variable.

- To understand distribution (shape, spread, outliers) of data.

- To detect anomalies/outliers.

- To choose appropriate transformations or preprocessing for modeling

# ? Why Univariate Analysis Matters

- It *simplifies understanding* of individual data attributes.

- Helps choose correct preprocessing steps (like scaling, encoding).

- Provides initial insights before advanced modeling.

---

# Two primary types of data:

1. Numerical (Quantitative) – e.g., age, salary.

2. Categorical (Qualitative) – e.g., gender, city.

3. Mixed (Numerical and Categorical) - e.g., Train Ticket

---

# **Key Techniques and Measures**

# 1. Staristical Measure

Used to describe and summarize the variable numerically using `df.describe()`

| *Measure*                                                                                 | *What It Tells*                |
| --------------------------------------------------------------------------------------- | ---------------------------- |
| **Mean**                                                                                | Average of values            |
| **Median**                                                                              | Middle value                 |
| **Mode**                                                                                | Most frequent value          |
| **Range**                                                                               | Max – Min (spread)           |
| **Variance / Standard Deviation**                                                       | How data spreads around mean |
| **Quartiles / Interquartile Range**                                                     | Spread of middle 50% values  |

# 2. Frequencies and Counts

- For *categorical data,* count how often each category appears.

- **Use frequency tables and bar charts** to check proportions and dominance.

> **Visualization techniques:**

| *Plot Type*     | *Useful For*                           |
| ------------- | ------------------------------------ |
| **Histogram** | Shows distribution of numerical data |
| **Bar Chart** | Displays category counts             |
| **Box Plot**  | Highlights median, IQR, and outliers |
| **Pie Chart** | Shows proportion of categories       |

- These plots give insights into shape, spread, and skewness of the data


------

# **Key Points**:


* Counting values: value_counts() (in Python/pandas).

* **Plotting histograms or boxplots for numeric distributions**.

* **Bar charts for category frequency**.

* **Detecting outliers with box plots**.

=> These are typical steps shown in the EDA univariate video (e.g., using Titanic dataset to explore features like Age, Fare, etc.).

---

# ***In short***

1. Identify variable type (numerical or categorical)

2. Compute descriptive statistics

3. Visualize distribution

4. Spot outliers and anomalies

5. Draw insights for further modeling
