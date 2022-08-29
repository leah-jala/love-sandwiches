import gspread
from google.oauth2.service_account import Credentials


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
    print("Please enter sales data from the last Market.")
    print("Data should include 6 numbers, separated by commas")   
    print("Example: 10, 20, 30, 40, 50, 60")    

    data_str = input("Enter your data here:")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values to integers
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        if len(values) !=6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")

get_sales_data()                                                                                                                                                                                                                                                                                                                                                                                                                                         
