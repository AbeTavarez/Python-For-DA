# Phase 4: Advanced SQL Business Audit

Goal: Answer 4 critical business questions using advanced relational logic (Subqueries & CTEs).

 **1. Shipping Delay Audit**
    The Goal: Find out which states are struggling with delivery promises.
    Logic: Use `DATEDIFF` to compare the "Estimated" date vs. the "Actual" date.

    <PSEUDOCODE>
    -- SELECT the customer state
    -- CALCULATE the average difference in days (Actual Date - Estimated Date)
    -- JOIN the Orders table with the Customers table
    -- FILTER for only 'delivered' orders
    -- GROUP the results by state
    -- ORDER by the largest delay (descending)
    -- LIMIT to the top 3
    <PSEUDOCODE/>

 **2. Top Earners per Category (The Subquery Method)**
    The Goal: Find the top 5 sellers in every single category without using a rank function.
    Logic: This uses a Correlated Subquery. For every seller, we "count" how many other sellers in that same category have a higher revenue.

    <PSEUDOCODE>
    -- STEP 1: Create a base query that sums Revenue per Seller per Category
    -- STEP 2: In the main WHERE clause, write a Subquery
    -- STEP 3: The Subquery should count all Sellers (t2) in the same Category as Seller (t1)
    --         WHERE t2.Revenue > t1.Revenue
    -- STEP 4: FILTER for rows where that count is LESS THAN 5
    -- STEP 5: ORDER by Category and Revenue
    <PSEUDOCODE/>

 **3. Payment Preferences (The Logic Method)**
    The Goal: Group messy payment types into clean categories.
    Logic: Use a CASE statement to bucket the data.

    <PSEUDOCODE>
    -- SELECT a CASE statement:
    --   WHEN type is 'credit_card' THEN 'Credit Card'
    --   WHEN type is 'boleto' THEN 'Boleto'
    --   ELSE 'Other'
    -- CALCULATE the average payment value
    -- COUNT the total number of transactions
    -- GROUP BY the CASE statement result
    <PSEUDOCODE/>

 **4. Customer Lifetime Value (The CTE Method)**
    The Goal: Isolate "Power Users" (High spend + High frequency).
    Logic: Find customers with above-average spend and high frequency.

    <PSEUDOCODE>
    1. DEFINE THE INNER MOST QUERY (The "Engine")
        -- Aggregate total payments and count orders
        -- Group them by the 'customer_unique_id'
        -- This becomes your main "data source" in the FROM clause

    2. DEFINE THE COMPARISON QUERY (The "Benchmark")
        -- Perform the same aggregation as above inside a second subquery
        -- Calculate the AVG() of those totals to get one single number
        -- This is nested in a JOIN so every row can see the benchmark

    3. APPLY THE FILTERS (The "Audit")
        -- Filter rows where the individual spend is higher than the benchmark subquery result
        -- Filter for individuals with more than 2 orders
        -- Sort the list to find your "VIP" customers
    <PSEUDOCODE/>