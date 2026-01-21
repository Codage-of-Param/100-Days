# **📌 One Hot Encoding :**

### **1. 📊 What Is One Hot Encoding?**

- One Hot Encoding converts categorical data (words/labels) into numerical format that machine learning models can understand. <br>
- It turns each category into a **binary vector — a “1” at the position of the category and “0” elsewhere**.

- **Example**: Feature: Colors with 3 categories (3 different values) Brown, Blue, and Black

    ```css
    Red   → [1, 0, 0]  
    Blue  → [0, 1, 0]  
    Green → [0, 0, 1]
    (1 means present; 0 means absent.)
    ```

### **2. 🧠 Why Do We Use It?**

- ✨ **Models need numbers**: Most ML algorithms cannot work directly with text. 

- 🚫 **Avoid false order**: Simple numeric labels (e.g., Red = 0, Blue = 1) can mislead models to assume hierarchy — one hot encoding avoids that. <br>

- 📈 **Better representation**: It gives each category its own dimension so models treat them independently.<br>

### **3. 🔧 How It Works**

- Create a **new binary column** for every unique category.

- For each row, only the column for the actual category gets 1; all others get 0.

- Results in a **sparse matrix (mostly zeros)** when categories are many.

### **4. 💡 Example in Practice**

- Suppose a dataset with a categorical feature `Fruit`:

    ```css
    Apple  → [1,0,0]  
    Banana → [0,1,0]  
    Mango  → [0,0,1]
    Now it’s ready for ML input.
    ```

### **5. 📉 Pros & Cons**

- Pros ✅

    - Makes categorical data usable for models.

    - Prevents incorrect ordinal interpretation.

- Cons ❌

    - High dimensionality if many categories → more columns.

    - Can slow training or use more memory.

### **6. 🧪 Implementation (Common Tools)**

📍 **Pandas**: ***pd.get_dummies()*** automatically does one hot encoding.

📍 **Scikit-learn**: Use OneHotEncoder from sklearn.preprocessing.

Example (pseudo-Python):

```python
    from sklearn.preprocessing import OneHotEncoder

    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(categorical_feature)
```

### **7. 📌 When to Use**

✔ Nominal categorical data (no order) – e.g., Color, City, Brand.

✖ Not ideal for ordinal data with natural order (use label or ordinal encoding).

----

# **Dummy variable trap:**

### **📌 What is the Dummy Variable Trap?**

The dummy variable trap occurs **when you create dummy variables** (one-hot encoded columns) for all **categories** of a categorical feature and include all of them in a regression model.

### **🔢 Simple Example**

- Suppose a feature Color has 3 categories:

1. Red

2. Blue

3. Green

After one-hot encoding:

| Red | Blue | Green |
| --- | ---- | ----- |
| 1   | 0    | 0     |
| 0   | 1    | 0     |
| 0   | 0    | 1     |

***👉 One column is linearly dependent on others → Dummy Variable Trap ⚠️***

- Tree based models are not affected with this but linear models are affected

### **✅ How to Avoid Dummy Variable Trap**

- Drop one dummy column (called the reference category)

- Example (drop Green):

| Red | Blue |
| --- | ---- |
| 1   | 0    |
| 0   | 1    |
| 0   | 0    |

- You can drop any column you want we generally drop 1st column

- Now:

    - **No multicollinearity**

    - Model works correctly ✔️

### **syntax**

- Pandas:

    ```python
    pd.get_dummies(df['Color'], drop_first=True)
    ```

- Scikit-learn

    ```python
    OneHotEncoder(drop='first')
    ```

## **Key points**

🧠 Key Takeaways

🚫 Dummy Variable Trap = multicollinearity due to full dummy set

✔ Always use (n − 1) dummy variables for n categories

🎯 Drop one category to act as baseline/reference

📌 Especially important for regression models
