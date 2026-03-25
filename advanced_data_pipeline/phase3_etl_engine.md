# PHASE 3: THE ETL ENGINE LOGIC

## Sudo Code:

```python
# PHASE 3: THE ETL ENGINE LOGIC

# 1. INITIALIZE CONNECTIONS
# Define MySQL credentials (User, Password, Host, Database)
# Create a SQLAlchemy engine using the 'mysql+mysqlconnector' driver

# 2. DEFINE SCHEMA ENFORCEMENT (Data Mapping)
# Create a dictionary to map Python DataFrame columns to MySQL Data Types:
#   - IDs (order_id, customer_id) -> VARCHAR(50)
#   - Status (order_status) -> VARCHAR(20)
#   - Dates (purchase_time, delivery_time) -> DATETIME
#   - Financials (price, freight) -> DECIMAL(10, 2)

# 3. THE LOAD PROCESS (The "L" in ETL)
# FOR each cleaned DataFrame (Orders, Items, Customers, etc.):
#   A. Use the .to_sql() method
#   B. Set destination table name
#   C. Pass the SQL engine connection
#   D. Set 'if_exists' to 'replace' (to ensure a clean overwrite during testing)
#   E. Apply the 'dtype' dictionary created in Step 2
#   F. Disable index (index=False) to keep the table clean

# 4. DATA INTEGRITY AUDIT (The Verification)
# A. Get the count of unique IDs from the Python DataFrame: len(df['id'].unique())
# B. Open a connection to the MySQL database
# C. Execute a RAW SQL query: "SELECT COUNT(DISTINCT id) FROM table_name"
# D. COMPARE the two results:
#    - IF counts match: Print "SUCCESS: Data Integrity Verified"
#    - ELSE: Print "ERROR: Row mismatch detected"

# 5. CLOSE CONNECTIONS
# Dispose of the engine to free up database resources
```