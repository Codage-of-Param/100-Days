# **Thread Safety**

- **Definition**

    - Thread safety is the property of code (class, method, or function) that ensures **correct and consistent behavior** when accessed by multiple threads simultaneously.

- **Primary Objective**

    - To **maintain data integrity** and prevent inconsistent or corrupted state during concurrent execution.

- **Core Problem Addressed**

    - **Prevents data races**, where program output depends on the *unpredictable timing* and interleaving of thread execution.

- **Cause of Issues**

    - Occurs due to unsynchronized concurrent access to shared mutable resources.

    ? **How Thread Safety Is Achieved**

        1. Locks / Mutexes – ensure mutual exclusion

        2. Synchronization mechanisms – coordinate thread access

        3. Atomic operations – guarantee indivisible updates

- **Encapsulation of Synchronization**

    - ***Thread-safe components internally manage synchronization***

    - Callers do not need to implement explicit locking

- **Examples** of Thread-Safe Collections

    1. C#: ConcurrentDictionary

    2. Java: ConcurrentHashMap

- **Key Benefit:**

    - Enables ***safe concurrent access*** without race conditions or inconsistent results.

- **Trade-off:**

    - Thread safety may introduce ***performance overhead*** due to synchronization.