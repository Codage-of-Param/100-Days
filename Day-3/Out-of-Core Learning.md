### **Out-of-Core Learning (External Memory Learning):**



**Meaning -** 



~ Out-of-core learning is a machine learning approach **used when the dataset is too large to fit into RAM**. 

~ The model is trained by loading and **processing data in small chunks from disk** (HDD/SSD) instead of the entire dataset at once.



* This learning **fits into both type of learning,** Batch(Offline) learning and online learning.



##### 1\.  **Out-of-Core + Batch Learning:**



**How it works:**



* The dataset is too large to fit into RAM.
* Data is read chunk-by-chunk from disk, but the model update happens after processing the full dataset (or full epoch).



**Key Point**:



* ***Data loading is chunk-wise, but learning logic is still batch-oriented.***



**Example**:



=> Training a regression model on terabytes of historical sales data

=> Big data training using Spark (mini-batch style)



##### 2\. **Out-of-Core + Online Learning**:



**How it works**:



* Data arrives or is read from disk incrementally.
* The model is updated after each record or small chunk.



**Key Point**:



* ***Both data access and model updates are incremental.***



**Example**:



=> Clickstream fraud detection

=> Real-time log analysis systems





* ##### ***In short*** : 



Out-of-core learning is a data-handling technique and can be combined with both batch learning and online learning depending on how model updates are performed.

