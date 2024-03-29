# The OpsEfficiencyMetrics class contains methods to calculate various operational efficiency metrics
# such as sale to receivable ratio, average days to collect accounts receivable, inventory turnover,
# average days to sell accounts receivable, sales to total assets ratio, and year-over-year growth in
# operating cash flow.

class OpsEfficiencyMetrics:
    
    def __init__(self):
        pass
    
    def sale_to_receivable(self, total_revenue, acc_rec_recent, acc_rec_prev):
        """
        The function calculates the sales to receivable ratio by dividing the total revenue by the average
        of the recent and previous accounts receivable.
        
        :param total_revenue: The total revenue is the total amount of money earned from sales during a
        specific period of time. It represents the income generated by the business
        :param acc_rec_recent: The parameter "acc_rec_recent" represents the recent accounts receivable
        balance. It is the amount of money that customers owe to the company for goods or services that have
        been delivered or provided recently
        :param acc_rec_prev: The parameter "acc_rec_prev" represents the accounts receivable balance at the
        end of the previous accounting period
        :return: the ratio of total revenue to the average of the recent and previous accounts receivable.
        """
        return total_revenue / ((acc_rec_prev + acc_rec_recent)/2)
    

    def avg_days_to_collect_acc_rec(self, sale_to_rec):
        """
        The function calculates the average number of days it takes to collect accounts receivable based
        on the sales to receivables ratio.
        
        :param sale_to_rec: The parameter "sale_to_rec" represents the number of days it takes for a
        sale to be converted into a receivable
        :return: the average number of days it takes to collect accounts receivable.
        """
        return 365 / sale_to_rec

    
    def inventory_turnover(self, cost_of_rev, inv_recent, inv_prev):
        """
        The function calculates the inventory turnover ratio by dividing the cost of revenue by the
        average of the recent and previous inventory levels.
        
        :param cost_of_rev: The cost of revenue is the total cost incurred to produce or acquire the
        goods that were sold during a specific period. It includes the cost of raw materials, direct
        labor, and other production costs
        :param inv_recent: The parameter "inv_recent" represents the value of inventory at the end of
        the recent period
        :param inv_prev: The inventory value at the beginning of the period
        :return: the inventory turnover ratio.
        """
        return cost_of_rev / ((inv_prev + inv_recent)/2)
    

    def avg_days_to_sell_acc_rec(self,inv_turnover):
        """
        The function calculates the average number of days it takes to sell accounts receivable based on
        the inventory turnover ratio.
        
        :param inv_turnover: The parameter "inv_turnover" represents the inventory turnover ratio. This
        ratio measures the number of times a company sells and replaces its inventory within a given
        period. It is calculated by dividing the cost of goods sold by the average inventory
        :return: the average number of days it takes to sell accounts receivable, based on the given
        inventory turnover ratio.
        """
        return 365/inv_turnover
    
    
    def sales_to_total_assets(self, total_rev, total_ass):
        """
        The function calculates the sales to total assets ratio by dividing total revenue by total
        assets.
        
        :param total_rev: The total revenue generated by the company
        :param total_ass: The total assets of a company. This includes all of the company's resources,
        such as cash, inventory, property, and equipment. It represents the value of everything the
        company owns
        :return: the ratio of total revenue to total assets.
        """
        return total_rev/ total_ass
    
    
    def growth_yoy_opcashflow(self,cflow_recent, cflow_prev):
        """
        The function calculates the year-over-year growth rate of operating cash flow.
        
        :param cflow_recent: The recent operating cash flow value
        :param cflow_prev: The previous year's operating cash flow
        :return: the year-over-year growth rate of operating cash flow.
        """
        return (cflow_recent - cflow_prev)/cflow_prev
    
    
    