# Mean Normalization:

## **1. What is Mean Normalization?**

- Mean normalization is a **feature scaling technique** used in data preprocessing to rescale numerical features so that:

  - The mean becomes 0

  - Values are centered around zero
 
## **2. Formula:**
​
<img width="523" height="236" alt="image" src="https://github.com/user-attachments/assets/938b597d-42cf-4131-9b8f-0905e14a9475" />

## **3. Step-by-Step Process**

- Calculate the mean of the feature

- Find the minimum and maximum values

- Subtract the mean from each value

- Divide by the range (Xmax - Xmin)

## **4. Key Characteristics**

- **Mean of transformed data ≈ 0**

- Values usually lie **between −1 and +1**

- Distribution shape remains unchanged

## **5. When to Use Mean Normalization**

  ✔ Gradient Descent–based algorithms <br>

  ✔ Linear Regression <br>

  ✔ Logistic Regression <br>

  ✔ Neural Networks <br>

  ✔ When features have different units or scales <br>

## **6. When NOT to Use**

  ✘ When data contains extreme outliers

  ✘ When min and max values are unstable

  ✘ Tree-based models (Decision Tree, Random Forest)

## **7. Advantages**

  - Improves convergence speed of gradient descent

  - Prevents dominance of large-scale features

  - Easy to interpret

## **8. Limitation**

  - Sensitive to outliers

  - Depends on min and max values

  - Less robust than Z-score normalization

### ***In short***:

  - Mean normalization rescales features by **subtracting the mean and dividing by the range** so that the ***transformed data is centered around zero***.

-----

# MaxAbsScaling:

## **1. What is MaxAbs Scaling?**

- MaxAbs Scaling is a feature scaling technique that **rescales numerical features by dividing each value by the maximum absolute value of that feature.**

  - The data is scaled to the range [−1, +1]

  - Zero remains zero
 
  - We use when there is a Sparse data/matrix (0’s or maximum number of 0’s)

  - No centering is performed (mean is not changed)
 
## **2. Formula**:

<img width="448" height="145" alt="image" src="https://github.com/user-attachments/assets/ccb78f6b-6769-4818-ba63-1ddba51b3f8e" />

## **3. Step-by-Step Process:**

- Find the absolute values of all data points

- Identify the maximum absolute value

- Divide each data point by this value

## ***4. Key Characteristics***

- Output range: [−1, +1]

- Sparse data preserved (zeros stay zero)

- No mean subtraction

- Linear transformation

## **5. When to Use MaxAbs Scaling**:

  ✔ Sparse datasets (text data, TF-IDF vectors)

  ✔ Data already centered around zero

  ✔ Linear models (SGD, Linear Regression)

  ✔ High-dimensional data

## **6. When NOT to Use**:

  ✘ Data with extreme outliers

  ✘ When centering is required

  ✘ Tree-based algorithms (Decision Tree, Random Forest)

## **7. Advantages**:

  - Very simple and fast

  - Preserves sparsity

  - No information loss

  - Suitable for large-scale ML systems

## **8. Limitations**:

  - Highly sensitive to outliers

  - Does not normalize variance

  - Mean is not centered

## ***In short***:

  - **MaxAbs Scaling rescales data by dividing each value by the maximum absolute value, preserving zero and sparsity.**

  - **MaxAbs = Divide by biggest magnitude, nothing else**

-----

# Robust Scaling:

## **1. What is Robust Scaling?**

- Robust Scaling is a **feature scaling technique** that rescales numerical data using **robust statistics—specifically the median and Interquartile Range (IQR)** —instead of the mean and standard deviation.

**👉 This makes it highly resistant to outliers.**

## **2. Formula**:

<img width="506" height="212" alt="image" src="https://github.com/user-attachments/assets/a3df4b09-8a19-4aad-a06e-164294ca1c68" />

## **3. Step-by-Step Process**:

  - Compute the median of the feature

  - Calculate Q1 (25%) and Q3 (75%)

  - Find IQR = Q3 − Q1

  - Subtract the median from each value

  - Divide by the IQR

## **4. Key Characteristics**:

  - Centered around median = 0

  - Resistant to outliers

  - Uses percentiles, not mean

  - Values are not bounded (can exceed ±1)

## **5. When to Use Robust Scaling**:

  ✔ Datasets with many outliers

  ✔ Financial data (income, prices, transactions)

  ✔ Real-world noisy data

  ✔ Linear & distance-based models

## **6. When NOT to Use**:

  ✘ Clean, normally distributed data

  ✘ When bounded output is required

  ✘ Tree-based models (Decision Tree, Random Forest)

## **7. Advantages**:

  - Very robust to extreme values

  - Stable scaling for skewed data

  - Better performance on noisy datasets

## **8. Limitations**:

  - Not suitable for normally distributed data

  - Does not constrain values to a fixed range

  - Slightly slower due to percentile computation

## **9. Real-World Use Case**:

  1. Salary normalization

  2. Credit risk modeling

  3. Fraud detection

  4. Transaction amount preprocessing

## ***In short***:

  - Robust Scaling normalizes data using median and interquartile range, making it resistant to outliers.

  - **Outliers present? → Think RobustScaler**
