import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


# Settings to access worksheet data

# Set the scope. Lists what APIs the user has access too. 
# IAM(Identity and Access Managem3ent) config
# As the scope won't change, it's written in as a constant

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales') #reference to the tab

data = sales.get_all_values()

#Step one - create a flow chart to work out the logic path of program tasks

def get_sales_data():
    """
    Get sales data figures, with input from User
    """
    while True:
        print("Please enter sales data from the last Market.")
        print("Data should include 6 numbers, separated by commas")   
        print("Example: 10, 20, 30, 40, 50, 60")    

        data_str = input("Enter your data here:")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break
    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values to integers
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) !=6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
    return True

def update_worksheet(data, worksheet):
    """
    Update sales and surplus worksheets, add new row with the list data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully\n")


def calculate_surplus_data(sales_row):
    """
    Calculate surplus stock
    - positive numbers equal surplus/waste
    - negative numbers  indicate extra was made when stock was sold out
    """
    print("Calculating surplus data...")
    stock = SHEET.worksheet("stock").get_all_values()
    pprint(stock)
    stock_row = stock[-1]

    surplus_data =[]
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data



def main():

    """
    Run all Program functions
    """
    data = get_sales_data()   
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")

print("Welcome to Love Sandwiches Data Automation")
main()                                                                                                                                                                                                                                                                                                                                                                                                                            
