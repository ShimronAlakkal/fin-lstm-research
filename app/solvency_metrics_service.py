# The SolvencyMetrics class contains methods for calculating various solvency metrics such as current
# ratio, quick ratio, interest coverage, and debt to net worth ratio.

class SolvencyMetrics:
    
    def __init__(self):
        pass

    def current_ratio(self,current_assets,current_liability):
        """
        The function calculates the current ratio by dividing current assets by current liabilities.
        
        :param current_assets: The current assets are the assets that a company expects to convert into
        cash or use up within one year. These assets include cash, accounts receivable, inventory, and
        prepaid expenses
        :param current_liability: The current liability refers to the amount of debt or obligations that
        a company is expected to pay within one year. This includes short-term loans, accounts payable,
        and other current liabilities
        :return: The current ratio, which is calculated by dividing the current assets by the current
        liabilities.
        """

        return current_assets/current_liability
    

    def current_ratio_prev(self,current_assets, cash_n_mark, total_assets):
        """
        The function calculates the current ratio by dividing the sum of current assets and cash by the
        total assets.
        
        :param current_assets: The current assets of a company, which include cash, accounts receivable,
        inventory, and other assets that are expected to be converted into cash within one year
        :param cash_n_mark: Cash and marketable securities
        :param total_assets: Total assets refers to the total value of all assets owned by a company.
        This includes both current assets (assets that can be easily converted into cash within a year)
        and non-current assets (assets that are expected to be held for more than a year). Examples of
        total assets include cash, accounts rece
        :return: the current ratio, which is calculated by dividing the sum of current assets and cash
        and marketable securities by the total assets.
        """
        
        return (current_assets + cash_n_mark)/total_assets
    
    
    def quick_ratio(self,cash_n_mark, accounts_reveivable, total_assets):
        """
        The function calculates the quick ratio by dividing the sum of cash and marketable securities
        and accounts receivable by total assets.
        
        :param cash_n_mark: The parameter "cash_n_mark" represents the amount of cash and marketable
        securities that a company has. This includes any cash on hand as well as any short-term
        investments that can easily be converted into cash
        :param accounts_reveivable: The amount of money owed to a company by its customers for goods or
        services that have been delivered but not yet paid for
        :param total_assets: The total assets refer to the sum of all the assets owned by a company.
        This includes both tangible assets (such as cash, inventory, and property) and intangible assets
        (such as patents and trademarks)
        :return: the quick ratio, which is calculated by adding the accounts receivable and cash and
        marketable securities, and then dividing that sum by the total assets.
        """
        return (accounts_reveivable + cash_n_mark)/total_assets
    
    
    def interest_coverage(self, operating_income, interest_expense):
        """
        The function calculates the interest coverage ratio by dividing operating income by interest
        expense.
        
        :param operating_income: The operating income is the profit generated from a company's core
        operations, before deducting interest and taxes. It represents the company's ability to generate
        profits from its main business activities
        :param interest_expense: The interest expense is the cost of borrowing money, typically in the
        form of interest payments on loans or debt. It represents the amount of money a company has to
        pay in interest on its outstanding debt
        :return: the interest coverage ratio, which is calculated by dividing the operating income by
        the interest expense.
        """
        return operating_income/interest_expense
    
    
    def debt_to_networth(self,total_liabilities,total_stockholders_equity_networth):
        """
        The function calculates the debt to net worth ratio by dividing total liabilities by total
        stockholders' equity (net worth).
        
        :param total_liabilities: The total amount of money that a company owes to its creditors or
        lenders. This includes both short-term and long-term liabilities
        :param total_stockholders_equity_networth: The total stockholders' equity net worth represents
        the total value of the company's assets that belong to the shareholders after deducting any
        liabilities. It includes items such as retained earnings, common stock, and additional paid-in
        capital
        :return: the debt to net worth ratio, which is calculated by dividing the total liabilities by
        the total stockholders' equity (net worth).
        """
        return total_liabilities / total_stockholders_equity_networth