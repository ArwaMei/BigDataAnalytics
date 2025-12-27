#  Hadoop & Spark Startup + Streaming Demo (WSL)

This guide shows how to start Hadoop services, verify HDFS data, and run a Spark Streaming demo.

---

## 🔹 Step 1 — Open Ubuntu (WSL)

Open an Ubuntu terminal.

---

## 🔹 Step 2 — Start SSH (Required for Hadoop)

```bash
sudo service ssh start
```

---

## 🔹 Step 3 — Start HDFS

```bash
start-dfs.sh
```

### Verify HDFS daemons:

```bash
jps
```

You should see:

* `NameNode`
* `DataNode`
* `SecondaryNameNode`

---

## 🔹 Step 4 — Start YARN

```bash
start-yarn.sh
```

### Verify YARN daemons:

```bash
jps
```

You should see:

* `ResourceManager`
* `NodeManager`

---

## 🔹 Step 5 — Verify HDFS Data Persistence

```bash
hdfs dfs -ls /
```

Expected output:

```
/input
/out-spark
/out-spark2
/user/arwa/file1.count
```

✔ Confirms that HDFS still contains previous data
✔ Ready for teacher evaluation

---

# ⭐ Spark Streaming Demonstration

## 🖥 Terminal 1 — Start Streaming Input

```bash
cd /mnt/f/bigdata
nc -lk 9999
```

(Type text here to simulate a real-time data stream)

---

## 🖥 Terminal 2 — Run Spark Streaming Job

```bash
cd /mnt/f/bigdata/stream
spark-submit \
  --class spark.streaming.tp22.Stream \
  --master local \
  stream-1.jar > out
```

➡️ Type text in **Terminal 1**
➡️ Observe processed output in **Terminal 2**

---

## 🔁 Quick Restart & Verification (If Needed)

```bash
sudo service ssh start
start-dfs.sh
start-yarn.sh
jps
```

Then show:

* `hdfs dfs -ls /out-spark`
* `hdfs dfs -cat /out-spark/part-00000`
* (Optional) Re-run Spark Streaming

