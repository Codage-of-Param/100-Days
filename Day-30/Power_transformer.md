### 🎯 **Purpose of Power Transformations**

- In many real-world datasets, features are **skewed** — meaning **they are not symmetric** and are stretched toward one side. 

- Skewed data can reduce the performance of ML models like** linear regression or logistic regression** because these models assume the data is more *normally* distributed.

- **Power transformers** change the shape of a distribution—all while preserving the order of values—so it becomes more symmetric and suitable for modeling. 

---

## 📌 **1) Box-Cox Transform**

### 💡 **Definition**

- The **Box-Cox transform** is a family of power transformations that** stabilizes variance** and makes the data as close to normal as possible **using a parameter λ (lambda)**.

- It’s defined only for **positive values**.

### 🧮 **Formula Example**

If ( x ) is a positive feature and λ is the transform parameter:

* If ( λ != 0 ):
  ( y = (x^λ -1) / λ )
* If ( λ = 0 ):
  ( y = log(x) )

**Example:**
Original values: `[1, 2, 4, 10]`

* If λ = 0.5:
  Square root-like scaling compresses large values.
* If λ = 0:
  Equivalent to log transform.

- lambda is in range of -5 to 5

- **Effect:** Large values are pulled in and the distribution gets more symmetric.

### 🧠 **When Box-Cox Helps**

* You have skewed positive numerical features like salary, house price, or count data.
* **Your goal is to improve performance of regression models by normalizing feature distribution.** 

---

## 📌 **2) Yeo-Johnson Transform**

### 💡 **Definition**

- The **Yeo-Johnson transform** is similar to Box-Cox but has one major advantage:
➡️ **It works on both positive and negative values.** 

### 🧮 **How It Works**

- It uses separate formulas depending on whether a data point is negative or non-negative.
- That flexibility allows you to transform features that cross zero without clipping or arbitrarily shifting them first.

**Example:**
Original data: `[-10, -2, 0, 5, 20]`

* Negative part and positive part are each transformed differently.
* Result: Less skew and more Gaussian-like shape.

**Effect on distribution:** Especially useful when data has negative and positive values with different behavior but still needs variance stabilization. 

---

## 🧠 **3) How These Transformations Are Used in Practice**

### 🏷 **In Feature Engineering**

- ML models often run better when input data is closer to a normal distribution. Transformations like Box-Cox or Yeo-Johnson:

    * Stabilize variance
    * Reduce skew
    * Improve predictive performance
    are commonly applied during preprocessing (before scaling and training).

### 🛠 **Code Example (Python / scikit-learn)**

```python
from sklearn.preprocessing import PowerTransformer

# For positive data only
boxcox_transformer = PowerTransformer(method='box-cox')

# For data that may have negative values
yeo_johnson_transformer = PowerTransformer(method='yeo-johnson')

X_transformed = yeo_johnson_transformer.fit_transform(X)
```

**Effect in code:** Automatically finds the best λ values to normalize features.

---

## 📝 **Structured Notes**

### ✅ **What Power Transformers Are**

* Group of mathematical functions that **normalize** skewed distributions.
* Aimed at making data more suitable for ML modeling. 

---

### Box-Cox Transform

* Requires **positive** values.
* Defines a family of transforms via λ.
* **λ = 0 → becomes a log transform**.
* Helps with skewed numeric features.

---

### Yeo-Johnson Transform

* Works on both **positive** and **negative** values.
* Ideal for mixed distributions crossing zero.
* Also finds a power parameter automatically. 

---

### **When to Use Each**

| Method      | Input Requirements         | Best For                              | 
| ----------- | -------------------------- | ------------------------------------- | 
| Box-Cox     | Only positive values       | Strong skew with all positive data    | 
| Yeo-Johnson | Negative & positive values | Mixed skewed data with negative parts |  

---

### - **Overall Benefits**

* Normalizes skewed distributions.
* Reduces impact of extreme values.
* Often **improves performance of linear and tree-based models.** 

