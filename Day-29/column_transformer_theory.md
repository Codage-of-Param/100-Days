### **1) What is ColumnTransformer?**

- ColumnTransformer is a utility from scikit-learn that lets you apply **different preprocessing steps to different columns of the same dataset in one unified pipeline**.

- In plain terms:<br>
    - Numeric columns may need scaling, categorical columns may need encoding, text may need vectorization—ColumnTransformer orchestrates all of this together.

### **2) Why do we need it?**

- Most real datasets are heterogeneous:

    - Numeric → scaling/normalization<br>
    - Categorical → one-hot / ordinal encoding<br>
    - Text → TF-IDF / CountVectorizer<br>

- Without ColumnTransformer, you risk:

    - Data leakage (fit transforms on full data)<br>
    - Inconsistent preprocessing between train/test<br>
    - Messy, error-prone code

- ColumnTransformer solves these by ***binding preprocessing to columns and executing it safely inside a pipeline.***

### 3) **Conceptual flow**

```pgsql
Input DataFrame
 ├─ Numeric columns → Scaler
 ├─ Categorical columns → Encoder
 └─ (Optional) Text columns → Vectorizer
           ↓
     Combined feature matrix
```

- All transformed features are **concatenated horizontally and passed forward.**

### 4) Parameters:

| Parameter                 | Meaning                              |
| ------------------------- | ------------------------------------ |
| `transformers`            | List of (name, transformer, columns) |
| `remainder='drop'`        | Drop columns not specified           |
| `remainder='passthrough'` | Keep unused columns as-is            |
| `sparse_threshold`        | Controls sparse vs dense output      |


### 5) **Syntax**

```python
from sklearn.compose import ColumnTransformer

ColumnTransformer(
    transformers=[
        ('name1', transformer1, columns1),
        ('name2', transformer2, columns2),
    ],
    remainder='drop'  # or 'passthrough'
)
```

### 6) **Example**

- Scenario:

    - `age`, `income` → numeric<br>
    - `city`, `gender` → categorical

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['age', 'income']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['city', 'gender'])
    ]
)
```

- What happens internally?

    - StandardScaler is applied only to `age`, `income`

    - OneHotEncoder is applied only to `city`, `gender`

    - **Outputs are merged into a single feature matrix**

- Use column transformer inside the pipeline is the best practice.

### 7) **Typical mistakes to avoid**

- Forgetting `handle_unknown='ignore'` in `OneHotEncoder`

- Applying scalers to categorical columns

- Fitting transformers outside the pipeline

- Using hard-coded column indices instead of names (when using DataFrames)

***⚠️NOTE:***

- **ColumnTransformer is for features (X) only, not target (y).** 

***In Short:***

- ColumnTransformer allows column-wise preprocessing by applying different transformations to different feature subsets and combining them into a single feature space, ensuring consistency, scalability, and **prevention of data leakage**.