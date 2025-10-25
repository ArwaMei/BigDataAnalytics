# Handling Large CSV Files (5GB+) in Python

This notebook demonstrates how to handle large CSV files (5GB+) in Python using different techniques to optimize speed, memory usage, and storage efficiency.

---

## 🎯 Purpose
The goal of this experiment was to **compare different methods for processing large datasets** (telecom activity data from Milan) and determine the most efficient approach in terms of:
- Memory usage (RAM consumption)
- Processing time (execution speed)
- Storage efficiency (compressed vs. raw data)

---

## 📊 Main Techniques Tested

### 1. **Pandas Normal Read**
**What:** Loads the entire CSV directly into memory.

**Output:**
- Load time: **252.60 seconds**
- Memory used: **9.5 GB**

**Problem:**  
This approach requires massive RAM and may crash on systems with less than 8GB of memory. It’s not suitable for very large files.

---

### 2. **Pandas with Chunksize**
**What:** Reads the dataset in smaller chunks instead of loading everything at once.

**Tested Configurations:**
| Chunk Size | Load Time (s) | Memory Used | Average Internet Usage |
|-------------|----------------|--------------|--------------------------|
| 100,000 | 157.83 | Minimal (−16 MB net) | 37.47 |
| 50,000 | 164.47 | 15.68 MB | 37.73 |
| 10,000 | 163.59 | 1.37 MB | 41.14 |

**Interpretation:**  
All chunk sizes successfully processed the dataset and calculated the same statistic (average internet usage).  
Larger chunks reduced reading overhead, while smaller chunks minimized memory usage.  
Chunking is an effective trade-off between **memory efficiency** and **execution speed**.

---

### 3. **Dask (Parallel Processing)**
**What:** Uses Dask to process the CSV in parallel across multiple cores, handling data in partitions.

**Output:**
- Load + compute time: **74.99 seconds**
- Memory used: **900.77 MB**
- Average internet usage: **36.77**

**Interpretation:**  
Dask significantly reduced computation time while keeping memory usage reasonable.  
It’s ideal for large-scale data processing on multi-core machines or distributed systems.

---

### 4. **Compression (gzip)**
**What:** Applies gzip compression to the dataset and Dask outputs to save disk space.

**Output:**
- Original size: **9840.67 MB**
- Compressed size: **2471.86 MB** (≈ 75% reduction)
- Compression time: **≈ 45 minutes**

**Interpretation:**  
Compression drastically reduces disk usage but increases processing time.  
Best suited for **long-term storage or transfer**, not active computation.

---

## 📈 Final Comparison Table

| Method | Load Time (s) | Memory Usage | Notes |
|--------|----------------|--------------|--------|
| Pandas (normal) | 252.60 | 9.5 GB | Impractical for large files |
| Pandas (chunks) | ~160 | ~0.01 GB | Memory-efficient and stable |
| Dask | 74.99 | 0.90 GB | Fastest and scalable |
| gzip compression | ~2700 | 1.27 GB | Best for saving storage |

---

## ✅ Key Findings

- **🏆 Dask is the overall winner** — fastest method with reasonable memory usage, suitable for scalable big data workflows.  
- **🧠 Pandas chunking** is the best choice when memory is limited but time is not critical.  
- **💾 Compression** provides the best storage optimization, ideal for archiving or transferring large datasets.  
- **❌ Direct Pandas reading** is inefficient for 5GB+ files and prone to crashing on low-memory systems.

---

## 💡 Practical Recommendations

| Use Case | Recommended Method |
|-----------|--------------------|
| Fast analysis on large data | **Dask** |
| Low-memory environment | **Pandas with chunksize** |
| Archiving and storage | **Compression (gzip)** |
| Small to medium data | **Direct Pandas** |

---

### 🧭 Conclusion
Efficient big data handling depends on the specific context.  
When **speed and scalability** matter most, use **Dask**.  
When **memory constraints** are the main concern, use **chunked Pandas** reading.  
When **disk space** is the bottleneck, **compression** provides excellent long-term efficiency.
