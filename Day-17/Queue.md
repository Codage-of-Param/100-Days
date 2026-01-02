# **Queue**:

- A queue is a linear data structure that follows the ***First-In-First-Out (FIFO) principle***.

- **Example**: The first person to stand in line is also the first who can pay and leave the supermarket.

---

- Basic Operations in Queue: 

    - **Enqueue**: Adds a new element to the queue.

    - **Dequeue**: Removes and **returns the first (front) element** from the queue.

    - **Peek**: Returns the first element in the queue.

    - **isEmpty**: Checks if the queue is empty.

    - **Size**: Finds the number of elements in the queue.

- Implement Queue with:
    1. LIST
    2. CLASS
    3. COLLECTIONS(deque)

---

# **1. Queue with LIST**:

| ***Operation*** | ***Method Used***      | ***Time Complexity***      | ***Reason***                  |
| --------- | ---------------- | -------------------- | ----------------------- |
| Enqueue   | `list.append(x)` | **O(1)**  | Appends at end          |
| Dequeue   | `list.pop(0)`    | **O(n)**             | All elements shift left |
| Peek      | `list[0]`        | **O(1)**             | Direct indexing         |
| isEmpty   | `len(list)`      | **O(1)**             | Constant-time length    |
| Size      | `len(list)`      | **O(1)**             | Stored internally       |

* **Key Drawback**

    - **Dequeue is expensive (O(n)) due to *element shifting*.**

    - Performance degrades significantly for large queues

* **Internal Working**:
    ```scss
    LIST (Dynamic Array)
    [10][20][30][40]
     ↑
    pop(0) → shifts all elements → O(n)

    - Shift means 20 goes on 0th index, 30 goes on 1st index, ... 
    ```
---

# **2. Queue with CLASS**:

- Same as LIST

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | **O(1)**        |
| Dequeue   | **O(n)**        |
| Peek      | **O(1)**        |
| isEmpty   | **O(1)**        |
| Size      | **O(1)**        |

* **Important Insight**

    - Using a class does NOT improve time complexity

    - Class only provides abstraction, encapsulation, and readability

    - Internally, the list behavior remains unchanged<br>

---

# **3. Queue with COLLECTIONS(deque)**:

- Python provides **deque (double-ended queue)** in the collections module, which is the most efficient way to implement a queue.

| ***Operation***       | ***Method***          | ***Time Complexity*** | ***Explanation***          |
| --------------- | --------------- | --------------- | -------------------- |
| Enqueue         | `append(x)`     | **O(1)**        | Insert at right end  |
| Dequeue         | `popleft()`     | **O(1)**        | Remove from left end |
| Enqueue (left)  | `appendleft(x)` | **O(1)**        | Insert at left       |
| Dequeue (right) | `pop()`         | **O(1)**        | Remove from right    |
| Peek front      | `q[0]`          | **O(1)**        | Direct access        |
| Peek rear       | `q[-1]`         | **O(1)**        | Direct access        |
| isEmpty         | `len(q)`        | **O(1)**        | Stored length        |
| Size            | `len(q)`        | **O(1)**        | Constant             |

# ? Why `deque` is faster than LIST

| Feature            | `list`        | `deque`                  |
| ------------------ | ------------- | ------------------------ |
| Dequeue front      | O(n)          | **O(1)**                 |
| Internal structure | Dynamic array | **Doubly linked blocks** |
| Element shifting   | Yes           | **No shifting**          |
| Large-scale queues | Inefficient   | **Highly efficient**     |


# Internal Working:

```scss

    LIST (Dynamic Array)
    [10][20][30][40]
     ↑
pop(0) → shifts all elements → O(n)

    DEQUE (Block-linked structure)
    [10] <-> [20] <-> [30] <-> [40]
     ↑
popleft() → pointer shift → O(1)

```

# **Is `deque` [thread-safe](https://github.com/Codage-of-Param/100-Days/blob/main/Day-17/thread_safety.md)?**

- Append/pop operations are atomic in CPython, but not fully synchronized.

---

# **Real life application of QUEUE:**

| ***Use Case***              | ***Explanation***                    |
| --------------------- | ------------------------------ |
| **BFS traversal**     | Nodes processed level by level |
| **Task scheduling**   | OS job queues                  |
| **Printer queue**     | FIFO printing                  |
| **Producer–Consumer** | Data pipelines                 |
| **Sliding window**    | Max/min window problems        |
| **Request handling**  | Web servers                    |



# **Compare Stack vs Queue vs Deque**:

| Feature        | Stack           | Queue      | Deque          |
| -------------- | --------------- | ---------- | -------------- |
| Order          | LIFO            | FIFO       | Both           |
| Insert         | One end         | Rear       | Both ends      |
| Delete         | One end         | Front      | Both ends      |
| Python support | `list`          | `deque`    | `deque`        |
| Best use       | Undo, recursion | Scheduling | Sliding window |


