###############################################################################
#
#Consider Share prices for a N number of companies given for each month since year     
#1990 in a CSV file.  Format of the file is as below with first line as header.
# 
#Year,Month,Company A, Company B,Company C, .............Company N
#1990, Jan, 10, 15, 20, , ..........,50
#1990, Feb, 10, 15, 20, , ..........,50
#.
#.
#.
#.
#2013, Sep, 50, 10, 15............500
#
# This program is used to List for each Company year and month in which the share price was highest.
#
# Module Name: highest_share_price.py
#
# Author: Prateek Jain
#
# Created: Jun 23, 2014
#
##############################################################################

import csv


class HighestSharePrice(object):
    """ These methods helps to find list for each Company
	    year and month in which the share price was highest.
    """

    def __init__(self):
        self.companies_data = self.read_file()

    def read_file(self):
        """ Loading CSV File to the program, which
            contains stock data of multiple companies.
        """
        with open('D:\Highest--Company-Share-Price-master\companies_stock_data.csv') as csv_file:
            reader = csv.reader(csv_file)
            file_data = [row for row in reader]

        return file_data

    def get_total_rows(self):
        """ Get total number of rows in CSV file.
        """

        return (sum(1 for row in self.companies_data)) -1

    def get_total_columns(self):
        """ Get total number of columns in CSV file.
        """

        columns_found = False
        start_column = 1

        while columns_found == False:
            start_column += 1
            try:
                identify_column = self.companies_data[0][start_column]
            except:
                columns_found = True
				
        column_count = start_column - 1

        return column_count

    def get_highest_share_price(self):
        """ This function return's the list for each Company,
       		Year and Month in which the share price was highest.
        """

        best_company_share_price = []
        company_index = 2
        row_count = self.get_total_rows()
        column_count = self.get_total_columns()

        while company_index <= (column_count):

            # Reseting the row_index and highest_share_index for every new company in loop.
            row_index = 1
            highest_share_index = row_index
        
            # Looping to go through each row of years.
            while row_index <= row_count:
                # Comparing if data is above or equal to current max
                if int(self.companies_data[highest_share_index][company_index]) <= int(self.companies_data[row_index][company_index]):
                    highest_share_index = row_index
        
                # Moving on to next row
                row_index += 1
        
            # Creating Best Company by adding Company Name + year + month + value.
            best_company_share_price.append(str(self.companies_data[0][company_index])+": "+str(self.companies_data[highest_share_index][0]) +", "+str(self.companies_data[highest_share_index][1])+", "+str(self.companies_data[highest_share_index][company_index]))
        
            # Moving on to next company
            company_index += 1

        return best_company_share_price

if __name__ == '__main__':
    shares_price = HighestSharePrice()
    results = shares_price.get_highest_share_price()
    for final_result in results:
        print final_result