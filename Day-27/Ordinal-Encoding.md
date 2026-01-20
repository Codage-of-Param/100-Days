# **Ordinal Encoding**

### **1. What is Ordinal Encoding?**

- Ordinal Encoding is a ***categorical encoding technique*** where categories are ***converted into numerical values based on their inherent order or ranking.***

- **It is used only when categories have a meaningful order.**

- Example: **Ratings**
 
    | Ratings    | Encoded Value |
    | ----------- | ------------- |
    | Good | 2             |
    | Poor  | 0             |
    | Average    | 1             |

- Here, the order matters, and the encoding preserves that order.

### **2. When Should You Use Ordinal Encoding?**

- Use Ordinal Encoding when:

  - The feature is **categorical**

  - The categories have a **natural ranking** (like 1,2,3....)

  - The order carries **real-world meaning**
 
### **3. When NOT to Use Ordinal Encoding 🚫**

- Do not use it when:

  - **Categories do not have any order.** (Basically when Nominal categories are there)

  - The order is **artificial or forced**
 
  - Example: Below example is wrong , You can't convert different colors in order
 
    | Color | Encoding |
    | ----- | -------- |
    | Red   | 1        |
    | Blue  | 2        |
    | Green | 3        |

- Colors have no ranking, so ordinal encoding is incorrect here.

### **4. Why Ordinal Encoding Works**

- Ordinal Encoding:

  - Preserves **relative ranking**

  - Allows models to **understand** **progression**

  - Is simple and **memory-efficient**

  - ⭐ Works well with ***tree-based models***

 ### **5. Impact on different ML models**

| Model Type          | Effect                             |
| ------------------- | ---------------------------------- |
| Linear Regression   | ⚠️ Can misinterpret distances (order difference)      |
| Logistic Regression | ⚠️ Risk of wrong weight assignment |
| **Decision Trees**      | ✅ **Very effective**                   |
| Random Forest       | ✅ Safe                             |
| Gradient Boosting   | ✅ Preferred                        |

### **6. Comparison with Other Encoding Methods**

| Encoding         | Use Case                    |
| ---------------- | --------------------------- |
| **_Ordinal Encoding_** | **_Ordered categories (ordinal categories)_**         |
| One-Hot Encoding | Unordered categories (nominal categories)       |
| ***Label Encoding***   | ***Mostly for target variables*** |
| Target Encoding  | High-cardinality features   |

### **7. Advantages ✅**

1. Simple to implement<br>
2. Preserves ranking<br>
3. Low dimensionality<br>
4. Efficient for large datasets<br>

### **8. Disadvantages ⚠️**

1. **Assumes equal distance between categories** <br>
2.  Can mislead linear models<br>
3.  Requires domain knowledge<br>
4.  Incorrect use can reduce model accuracy<br>

#### Note : 

- We don't use ordinal encoding in target columns, we use label encoding instead.

### ***In Short***

- **Definition**: Ordinal encoding converts ordered categorical variables into numerical values based on their natural ranking.

- **Key Requirement**: Categories must have a meaningful order (e.g., Low < Medium < High).

- **Use Case**: Education level, customer satisfaction, ratings, sizes.

- **Not Suitable For**: Unordered (nominal) categories like color or city names.

- **Target Variable**: Can be used only if the target is ordinal.

- **Model Compatibility**: Works best with tree-based models; may mislead linear models due to equal-distance assumption.

- **Advantage**: Simple, memory-efficient, preserves order.

- **Limitation**: Assumes equal spacing between categories.
