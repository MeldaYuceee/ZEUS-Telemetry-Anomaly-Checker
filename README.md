# 🔱 ZEUS – Telemetry Analysis Module

ZEUS is a lightweight telemetry analysis tool designed to evaluate basic consistency and safety indicators in UAV telemetry data.  
The project focuses on detecting abnormal speed values and sudden altitude changes using rule-based thresholds.

This module is intended for **educational and defensive analysis purposes**.

---

## 📌 Features

- Rule-based telemetry analysis
- Speed limit violation detection
- Sudden altitude jump detection
- Clean, table-formatted console output
- Summary statistics for detected anomalies

---

## 📂 Project Structure
checker.py
data.csv
README.md

- `checker.py` → Core analysis script  
- `data.csv` → Sample telemetry data  
- `README.md` → Project documentation  

---

## 📄 Telemetry Data Format

The input file must be a CSV file with the following structure:

```csv
time,lat,lon,alt,speed
0,39.92,32.85,120,14
1,39.9201,32.8501,121,14.2
2,39.9250,32.8600,140,30
