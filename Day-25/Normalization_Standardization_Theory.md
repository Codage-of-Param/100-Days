# 1. **Normalization:**


- Normalization in machine learning is a **data preprocessing technique** that rescales numeric features to a **common range**, typically 0 to 1, to ensure all features contribute equally to model training.

- Use methods like ***MinMax Scaling*, Mean normalization, Max absolute scaling, Robust scaling**

# - MinMax Scaling: 

- **Xi’ = (Xi - Xmin) / (Xmax - Xmin)**<br>

  - Where,<br>
    	Xi’ = Transformed value <br>
	    Xi = Current value <br>
	    Xmax = Maximum value in set <br>
	    Xmin = Minimum value in set <br>

- ***Always value of Xi’(min max scale) is between [0,1].***

---

# 2. **Standardization:**

- also called **Z-Score Normalization**

- **What to do ?**

    - First copy the same column and transform it.

- **How to transform ?**

    - Use this formula **Xi’ = (Xi - µ) / σ** 

    - Where : <br>

        Xi’ = Transformed value, <br>
        Xi = Value for transformation, <br>
        σ =  Standard deviation, <br>
        µ = Mean <br>


- for Xi’ ,It’s **Mean = 0 and SD = 1** which is confirm.

-  ***Mean = 0 => It’s also called Mean Centering***

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
```

- **NOTE:**

    -  Standardization does not work on outliers, we have to implement explicit methods for removing outliers.

    example of standardization : https://github.com/campusx-official/100-days-of-machine-learning/tree/main/day24-standardization
