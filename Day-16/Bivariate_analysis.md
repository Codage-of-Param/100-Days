# **Bivariate Analysis**:

- Bivariate analysis studies the ***relationship between two variables***.

# A. Numerical vs Numerical:

- When both variables are numeric (continuous):

1. Scatter Plot:

    - Plots each observation as a point.

    - Useful to observe correlation or trend between two numeric variables.

    - Positive/negative relationship or no relationship can be seen. 

2. Line Plot:

    - Used when one numeric variable represents time.

    - Helps observe trends/changes over time.

  # B. Numerical vs Categorical:

- This involves one numeric and one categorical variable:

1. Bar Plot:

    - Plots aggregated values (mean, count, sum) of the numeric variable for each category.

    - Easy comparison of category-wise numeric distribution. 

2. Box Plot:

    - Displays median, quartiles, and outliers.

    - Useful to compare spread, skewness, and outliers across categories. 

3. Distribution Plot (DistPlot):

    - Shows the distribution curve of a numeric variable.

    - With categorical distinction (hue), shows distributions by category.

# C. Categorical vs Categorical:

- This includes **two categorical variables**.

1. Heatmap:

    - Visual grid showing the frequency of combinations of categories.

    - Color intensity represents magnitude.
---

# **Multivariate Analysis**

* Multivariate analysis looks at relationships among **more than two variables** simultaneously.

* **Key Methods Covered** :

1. Pairplot

    - Displays pairwise relationships for all variables in a dataset.

    - Useful to observe correlation patterns and distribution across multiple features.

  | Objective                            | Effective Plot          |                
| ------------------------------------ | ----------------------- |  
| Understand numeric-numeric relations | Scatter Plot, Line Plot |                
| Compare category-level numeric stats | Bar Plot, Box Plot      |                
| See distribution patterns            | DistPlot                |                
| Analyze joint category occurrences   | Heatmap                 |                
| Inspect all variable pairs           | Pairplot                |

# **Summary: Bivariate & Multivariate EDA Steps** :

1. Start Simple -

    - Check **numerical vs numerical relationships with scatter/line plots**.

2. Group by Categories - 

    - Use box and bar plots to compare numeric summaries across categories.

3. Distribution Insights - 

    - Use **distplots to understand how data spreads**.

4. Association Between Categories - 

    - Use **heatmaps to observe co-occurrences**.

5. Multiple Variable Relationships -

    - Pairplots help in deeper multivariate insights.
  
  ---
  
# Practical Use Cases

- Detecting correlation between features (e.g., age vs income).

- Comparing different segment behaviors (e.g., product ratings by region).

- Visual identification of outliers or data group trends.

- Screening variables before modeling or feature engineering.

----

# Typical Workflow

1. Load Data

2. Check data types (Numeric/Categorical)

3. Plot appropriate relationships

4. Interpret visual insights

5. Decide further modeling steps
