# **📌 Pandas Profiling -**

## **1. 📊 What Is Pandas Profiling?**

- Pandas Profiling is a Python tool used to automatically **generate detailed exploratory data analysis (EDA) reports from a Pandas DataFrame**.

- It provides statistical summaries and visual insights without writing much code, saving time in early data exploration.

## **2. 🧠 Why Use Pandas Profiling?**

- **Automates the EDA process (fast and efficient)**.

- Helps understand overall dataset structure quickly.

- Produces rich HTML reports with insights for data cleaning and preparation.

- **Useful before building machine learning models.**

## **3. 🛠 Installation & Setup**:

- Install Pandas Profiling (now known as `ydata-profiling`):

```bash
    pip install ydata-profiling
```

**OR**

```bash
    conda install -c conda-forge ydata-profiling
```

- Then import in your Python script/notebook:

```python
    from ydata_profiling import ProfileReport
```

- Generate a profile report by passing your DataFrame:

```python
    profile = ProfileReport(df)
    profile.to_file("report.html")
```

*(Note: actual syntax may vary slightly based on library version)*

## **4. 📈 What the Report Includes**:

* Overview

    - Number of rows & columns

    - Total missing values

    - Data types and memory usage

    - Duplicates and sample records

* Variables Summary

    - For each feature/column:

    - Distribution (histograms)

    - Key statistics (mean, median, percentiles)

    - Unique values and cardinality

* Missing Values

    - Count and pattern of missing data

    - Matrix visuals showing where missing values occur

* Correlations

    - Pairwise relationships (Pearson, Spearman, etc.)

    - Heatmaps to visualize strong correlations

* Interactions

    - Scatterplots and cross-variable comparisons

    - All this is curated automatically to give a clear picture of the data.

## **5. 🎯 Key Benefits**:

- Saves hours of manual EDA.

- Quick visualization and detection of issues like:

    i. Missing values<br>
   ii. Outliers<br>
  iii. Skewed columns<br>
   iv. High correlations

- Helps decide preprocessing decisions early.

## **6. ⚠️ Limitations**:

- Can be **slow on very large datasets** (performance may degrade).

- Reports are best used for initial insights — still require interpretation.

## **7. 📌 Best Practice (In Short)**

1. Use Pandas Profiling as a first step in EDA.

2. After generating the report, follow with:

    - Data cleaning

    - Feature engineering

    - Visualization customization<br>
to prepare data for modelling.

***[CODE](https://github.com/Codage-of-Param/100-Days/blob/main/Day-20/Video%2BGames%2Bsales_profiling.ipynb)***
