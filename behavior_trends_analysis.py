import pandas as pd

# Function to import data
def import_data(filename: str) -> pd.DataFrame:
    """Import the dataset from an Excel or CSV file into a DataFrame."""
    if filename.endswith('.xlsx'):
        df = pd.read_excel(filename)
    elif filename.endswith('.csv'):
        df = pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format")
    return df

# Function to filter the data
def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter the data by removing rows with missing CustomerID and excluding rows with negative values."""
    df = df.dropna(subset=['CustomerID'])  # Drop rows with missing CustomerID
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]  # Filter out negative values
    return df

# Function to identify loyal customers
def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    """Identify loyal customers based on a minimum purchase threshold."""
    customer_purchases = df.groupby('CustomerID').size()
    loyal_customers = customer_purchases[customer_purchases >= min_purchases].reset_index()
    loyal_customers.columns = ['CustomerID', 'PurchaseCount']
    return loyal_customers

# Function to calculate quarterly revenue
def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the total revenue per quarter."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    revenue_per_quarter = df.groupby('Quarter')['Revenue'].sum().reset_index()
    revenue_per_quarter.columns = ['Quarter', 'TotalRevenue']
    return revenue_per_quarter

# Function to identify high-demand products
def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """Identify the top_n products with the highest total quantity sold."""
    product_demand = df.groupby('StockCode')['Quantity'].sum().nlargest(top_n).reset_index()
    product_demand.columns = ['Product', 'TotalQuantitySold']
    return product_demand

# Function to summarize purchase patterns
def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary showing the average quantity and average unit price for each product."""
    product_summary = df.groupby('StockCode').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    product_summary.columns = ['Product', 'AvgQuantity', 'AvgUnitPrice']
    return product_summary

# Function to answer conceptual questions
def answer_conceptual_questions() -> dict:
    """Returns answers to the multiple-choice questions."""
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A"},
        "Q5": {"A"}
    }
    return answers

# Main script to run the functions
if __name__ == "__main__":
    # Load the dataset
    df = import_data("Customer_Behavior.xlsx")
    
    # Filter the data
    df = filter_data(df)
    
    # Identify loyalty customers with a minimum purchase threshold, e.g., 50
    loyal_customers_df = loyalty_customers(df, min_purchases=50)
    print("Loyal Customers:\n", loyal_customers_df)
    
    # Calculate quarterly revenue
    quarterly_revenue_df = quarterly_revenue(df)
    print("Quarterly Revenue:\n", quarterly_revenue_df)
    
    # Get high-demand products (e.g., top 10)
    high_demand_products_df = high_demand_products(df, top_n=10)
    print("High Demand Products:\n", high_demand_products_df)
    
    # Analyze purchase patterns
    purchase_patterns_df = purchase_patterns(df)
    print("Purchase Patterns:\n", purchase_patterns_df)
    
    # Answer conceptual questions
    answers = answer_conceptual_questions()
    print("Conceptual Questions Answers:\n", answers)
