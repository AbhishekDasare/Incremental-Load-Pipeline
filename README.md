# Incremental-Load-Pipeline

## Project Overview

This project demonstrates an Incremental Data Load Pipeline using PySpark.

The pipeline reads existing customer records from a source dataset and processes newly arrived records from an incremental dataset. Both datasets are merged and written into a target dataset.

This approach is commonly used in Data Engineering to process only newly arrived data instead of reloading the entire dataset.

---

## Technologies Used

- Python
- PySpark
- Apache Spark
- CSV Files
- ETL Pipeline

## ETL Process

### Step 1
Read source customer dataset.

### Step 2
Read newly arrived incremental dataset.

### Step 3
Merge source and incremental datasets.

### Step 4
Write final dataset to target location.

### Step 5
Generate processed output for analytics and reporting.

---

## Business Use Case

Organizations receive new records every day.

Instead of processing the entire dataset repeatedly, Incremental Loading processes only newly arrived records and appends them to the existing dataset.

Benefits:

- Faster Processing
- Reduced Compute Cost
- Improved Performance
- Scalable Data Pipelines

## Key Features

- Incremental Data Processing
- Data Merge Operations
- ETL Pipeline Development
- PySpark Data Engineering
- Analytics Ready Output

---

## Skills Demonstrated

- PySpark
- Apache Spark
- Data Engineering
- ETL Development
- Incremental Loading
- Data Processing
- Data Transformation
- Data Pipeline Design

---

## Future Enhancements

- Delta Lake Integration
- AWS S3 Storage
- AWS Glue Jobs
- Data Quality Checks
- Change Data Capture (CDC)
- Real-Time Streaming Integration

---

## Author

**Abhishek Dasare**

Data Engineer | PySpark | AWS | SQL | ETL | Data Engineering
