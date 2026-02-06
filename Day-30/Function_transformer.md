### 🎯 **Core Topic: Function Transformers in Data Preprocessing**

- This concept explains how specific mathematical functions are applied to data to make it **more suitable for machine learning models**, especially when the **distribution is skewed** (not normal/ bell-shaped).

---

### 1) 🔄 **What Is a Function Transformer?**

- A **Function Transformer** applies a mathematical function to every value in a dataset so that:

* The data becomes **less skewed**,
* Patterns become easier for models to recognize,
* Outliers distort less influence on learning.

For example:

> If you have income data that’s heavily right-skewed (big incomes are rare but huge), you apply a **log transform** to reduce the spread and make the distribution more manageable for algorithms.

---

### 2) 📊 **Types of Transformations Explained**

- Here’s how each type works — with a quick numeric example:

#### 🧮 a. **Log Transform**

* Applies the logarithmic function to data.
* Formula: ( y = \log(x) )
* Best for **right-skewed** data (where values grow rapidly).

**Example:**
Original values:
`[10, 100, 1000]` → After log:
`[1, 2, 3]` (approx)

**Effect:** Large numbers compress; patterns become linear. 

---

#### 🔁 b. **Reciprocal Transform**

* Uses the reciprocal ( y = 1 / x )
* Helps tame large values even more dramatically than log.

**Example:**
Original: `[1, 2, 10]` → Reciprocal:
`[1.0, 0.5, 0.1]`

**Effect:** Larger original values shrink much more. 

---

#### 🔢 c. **Square Root Transform**

* Applies the square root: ( y = \sqrt{x} )
* Good for **moderately skewed** distributions, especially count data.

**Example:**
Original: `[4, 9, 16]` →
Square root: `[2, 3, 4]`

**Effect:** Dampens the scale gradually without over-compressing. 

---

### 3) 🧠 **Why Use These Transformers?**

Transformations help:

* **Normalise skewed data**
* Make distributions more bell-shaped (closer to a normal distribution)
* Improve performance of regression and classification algorithms
* Reduce impact of extreme values (outliers)

For **example**, housing price data often benefits from log transformation so that models don’t get overwhelmed by a few extremely expensive homes. 

---

### 4) 🚀 **When to use Each**

| Transformation  | Best For         | Typical Use                         |               
| --------------- | ---------------- | ----------------------------------- | 
| **Log**         | Right-skewed     | Income, sales figures               |               
| **Reciprocal**  | Extreme outliers | Small technical measurements        | 
| **Square Root** | Moderate skew    | Count data (e.g., number of events) |

---

### 5) 💡 **Relation to Machine Learning**

- This topic is part of **feature engineering** — a critical preprocessing step in ML where raw data is transformed into a form that algorithms can better learn from.

- Transformers like these are often used with tools such as:

    ```python
    from sklearn.preprocessing import FunctionTransformer
    transformer = FunctionTransformer(func=np.log1p)
    transformed_data = transformer.fit_transform(data)
    ```

(Here `log1p` means `log(x + 1)` to handle zero values safely.) 

---

## 📝 **Detailed Notes (Bullet Format)**

**✅ Function Transformer Definition**

* Applies mathematical functions to entire dataset.
* Improves distribution properties for ML models. 

**✅ Log Transform**

* ( y = \log(x) )
* Reduces effect of large numbers.
* Works best on right-skewed data. 

**✅ Reciprocal Transform**

* ( y = 1/x )
* Greatly diminishes large values.
* Useful when high values dominate. 

**✅ Square Root Transform**

* ( y = \sqrt{x} )
* Moderates skew without heavy compression.
* Often used for count-based features. 

**✅ Significance in Machine Learning**

* Part of **feature engineering & preprocessing**.
* Helps satisfy algorithms’ assumptions about normality.
* Reduces influence of skew and outliers. 

---

## 🧠 **Summary**

1. **Log Transform** – gentle compression.
2. **Reciprocal** – strong compression.
3. **Square Root** – moderate compression.

- Each is chosen based on the **distribution characteristics** of your data. Proper use helps improve model performance. 
