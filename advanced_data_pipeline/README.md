# Project Guide: The Automated Retail & Supply Chain Intelligence Pipeline

## Case Study: Olist Brazilian E-Commerce
**1. Project Overview**
You are a Lead Data Analyst at Olist, the largest department store marketplace in Brazil. Leadership has provided you with a massive dump of raw data (100k orders from 2016-2018). Currently, this data is siloed in multiple files. Your task is to build a centralized MySQL database, automate the data flow with Python, and provide a deep-dive audit into logistics and customer satisfaction.

**2. Workplace Simulation: The Scenario**
**The Problem:** Olist is scaling fast, but shipping delays and high freight costs are hurting their reputation. The CEO needs to know: Where are the bottlenecks? Which product categories are actually profitable after shipping costs? And which states have the worst delivery performance?

**Your Mission:** Build a robust ETL (Extract, Transform, Load) pipeline. Use Python to clean the data and visualize early trends, MySQL to store the relational model, and SQL to perform a heavy-duty audit.

 <hr/>

**3. Phase 1: Environment & Schema Design (5 Hours)**

 - **Download the Data:** Get the Olist Dataset from Kaggle.

 - **MySQL Setup:** Create a new schema olist_intelligence.

 - **The Stack:**

   ```Bash
    pip install pandas sqlalchemy pymysql matplotlib
   ```

 - **Relational Mapping:** This is a Star Schema project. You must map out how order_items connects to products, sellers, and orders.
 
 <hr/>

**4. Phase 2: Python Cleaning & Matplotlib EDA (10 Hours)**
- **Data Cleaning:**
  - **Handle UTC Timestamps:** Convert all 5+ date columns (purchase, approved, delivered, etc.) into proper datetime objects.
  - **Price Validation:** Check for $0$ or negative prices in the items table.
  - **Geolocation:** Clean the zip_code_prefix to ensure it remains a string (to avoid losing leading zeros).

- **Visual Exploration (Matplotlib):**
 - **Order Volume:** Plot a Line Chart of orders per month to find peak holiday seasons.
 - **Delivery Performance:** Create a Box Plot of "Estimated vs. Actual" delivery days.
 - **Review Scores:** Create a Bar Chart showing the distribution of review scores (1–5 stars).
 
 <hr/>

**3. Phase 3: The MySQL ETL Engine (8 Hours)**
 - **The Pipeline:** Write a Python script using SQLAlchemy to automate the data transfer.

 - **Schema Enforcement:** When using .to_sql(), ensure you define the correct data types for MySQL (e.g., VARCHAR(50) for IDs, DECIMAL(10,2) for prices).

 - **Data Integrity:** Verify that the number of unique customer_ids in Python matches the count in MySQL after the transfer.

 <hr/>

**4. Phase 4: Advanced SQL Audit (12 Hours)**
Solve these 4 Business Challenges in MySQL:

 **1. Shipping Delay Audit:** Calculate the average "Delivery Lag" (Actual minus Estimated) per state. Which 3 states are slowest?

 **2. Top Earners:** Use DENSE_RANK() to find the top 5 sellers by revenue in each product category.

 **3. Payment Preferences:** Use a CASE statement to categorize orders by payment type (Boleto vs. Credit Card) and find the average order value for each.

 **4. Customer Lifetime Value:** Use CTEs to find customers who have spent more than the average and have placed more than 2 orders.

 <hr/>

**5. Phase 5: Documentation & Portfolio Delivery (5 Hours)**

 - **The README:** Document your "Data Cleaning Log" (e.g., "I handled 3% missing delivery dates by...").

 - **Visuals:** Embed your Matplotlib charts in your GitHub README.

 - **Final Deliverables:**

    - `etl_pipeline.py` (The Python script)

    - `analysis_queries.sql` (The 4 SQL challenges)

    - `project_report.md` (Executive summary of insights)

🚀 **Coming Next: Part 2 — The Executive Intelligence Suite
Building the Front-End with Excel & Power BI**

Once you have mastered the "Back-End" by building your automated pipeline, you will transition from a Data Engineer to a Business Intelligence (BI) Strategist. In the next phase of this project, you will use the "Golden Records" you’ve stored in MySQL to build a professional reporting suite.