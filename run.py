import gspread #Imports entire gspread library
from google.oauth2.service_account import Credentials #imports credentials class

#Settings to access worksheet data

#Set the scope. Lists what APIs the user has access too. IAM(Identity and Access Managem3ent) config
#As the scope won't change, it's written in as a constant, which gets all caps.
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
print(data)

