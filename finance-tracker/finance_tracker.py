import pandas as pd #Python library for data manipulation
import matplotlib.pyplot as plt #Plotting library


# Initialize or load the DataFrame
try:
    df = pd.read_csv('finance_tracker.csv') #Checks to see if the file exists
except FileNotFoundError:
    df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type']) #If the file doesn't exist, this creates it
    df.to_csv('finance_tracker.csv', index=False)



def add_transaction(df, date, category, description, amount, t_type): #Creating a function that gives the user the ability to add transactions
    new_transaction = pd.DataFrame({ #Creating a DataFrame for new transactions
        'Date': [date], 
        'Category': [category], 
        'Description': [description], 
        'Amount': [amount], 
        'Type': [t_type]
    })
    df = pd.concat([df, new_transaction], ignore_index=True) #Adding the transaction to the DataFrame
    df.to_csv('finance_tracker.csv', index=False)
    print("Transaction added successfully.")
    return df

def view_transactions():
    print(df)

def calculate_totals():
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    net_balance = total_income + total_expense
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Net Balance: ${net_balance:.2f}")

def visualize_spending():
    expense_df = df[df['Type'] == 'Expense']
    category_totals = expense_df.groupby('Category')['Amount'].sum()
    
    category_totals.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Spending by Category")
    plt.ylabel('')
    plt.show()

def main():
    global df  # Declare df as global to access it throughout the program

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Totals")
        print("4. Visualize Spending")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Rent): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            t_type = input("Enter the type (Income/Expense): ")
            df = add_transaction(df, date, category, description, amount, t_type)
        
        elif choice == '2':
            view_transactions()
        
        elif choice == '3':
            calculate_totals()

        elif choice == '4':
            visualize_spending()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
