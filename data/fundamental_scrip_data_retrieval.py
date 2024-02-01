# The ScripFundamentalData class provides methods to retrieve historical data, balance sheet, cash
# flow statement, and income statement for a given stock symbol.
class ScripFundamentalData:
    
    def __init__(self, scrip):
        """
        The function initializes an object with a given scrip and retrieves data using the yf.Ticker
        method.
        
        :param scrip: The parameter "scrip" is used to store the ticker symbol of a stock. It is passed
        as an argument to the constructor of the class
        """
        self.scrip = scrip
        self.data = yf.Ticker(self.scrip)
    

    def get_history(self):
        """
        The function `get_history` returns the history data of an object.
        :return: the data variable, which is the history of the self.data object.
        """
        data = self.data.history()
        return data

    
    def get_balance_sheet(self):
        """
        The function "get_balance_sheet" returns the balance sheet data.
        :return: The balance sheet data.
        """
        b_sheet = self.data.balance_sheet
        return b_sheet

    
    def get_cflow_stmt(self):
        """
        The function `get_cflow_stmt` returns the cashflow statement from the `data` attribute.
        :return: the value of the variable "cflow_stmt".
        """
        cflow_stmt = self.data.cashflow
        return cflow_stmt
    

    def get_income_stmt(self):
        """
        The function "get_income_stmt" returns the income statement data.
        :return: The income statement data.
        """
        income_stmt = self.data.income_stmt
        return income_stmt