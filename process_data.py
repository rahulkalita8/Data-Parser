from helper import Helper


class ProcessData:
    """
    This classes processes the stock data and does all the powerlifting to solve the four questions
    """

    def __init__(self, args):
        """
        Initializing the class with all possible arguments
        :param args: Argument class
        """
        self.data = Helper.read_CSV(args.csvFilePath)
        self.filtered_data = self.data
        self.sort = args.sort
        self.stockName = args.stockName
        self.startDate = args.startDate
        self.endDate = args.endDate
        self.filter_data()

    def filter_data(self):
        """
        Get the filtered data based on the provided parameters
        :return: None
        """
        if self.stockName:
            self.filtered_data = self.filtered_data.loc[self.filtered_data['Name'] == self.stockName].reset_index(drop = True)
        if self.startDate:
            if self.endDate:
                self.filtered_data = self.filtered_data[(self.filtered_data['date'] >= self.startDate) & (self.filtered_data['date'] <= self.endDate)].reset_index(drop = True)
            else:
                self.filtered_data = self.filtered_data[(self.filtered_data['date'] >= self.startDate)].reset_index(drop = True)

    def question_one(self):
        """
        Solve Question 1: Sort the data according to stock name and date
        Write the data in CSV file
        :return: None
        """
        if not self.sort:
            self.sort = "asc"
        isAscending = True if self.sort == "asc" else False
        sortByColumns = ["Name", "date"]
        sorted_data = self.data.sort_values(sortByColumns, ascending=isAscending).reset_index(drop = True)

        sorted_data.to_csv("result/soln1.csv", index=False)

        sorted_data = self.filtered_data.sort_values(sortByColumns, ascending=isAscending).reset_index(drop = True)
        sorted_data.to_csv("result/soln1_filtered.csv", index=False)

    def question_two(self):
        """
        Solve Question 2: Find the highest value of stock. Highest value will always be in 'high' column.
        Write the data in JSON format
        :return: None
        """
        highest_data = self.filtered_data.loc[self.filtered_data.reset_index(drop = True).groupby(['Name'])['high'].idxmax()]
        highest_data.to_json("result/soln2.json", orient="records")

    def question_three(self):
        """
        Solve Question 3: Calculate max and min difference between opening and closing prices
        Write the result in a JSON file
        :return: None
        """
        diff_data = self.filtered_data
        diff_data = diff_data.drop(["high", "low"], axis=1)
        diff_data = diff_data.sort_values(["volume"], ascending=False).reset_index(drop = True)
        diff_data["difference_value"] = diff_data['open'] - diff_data['close']

        # Get the maximum value
        max_data = diff_data.loc[diff_data.reset_index(drop = True).groupby(['Name'])['difference_value'].idxmax()]
        max_data['operation'] = 'max'

        # Get the minimum value
        min_data = diff_data.loc[diff_data.reset_index(drop = True).groupby('Name')['difference_value'].idxmin()]
        min_data['operation'] = 'min'

        result_data = max_data.append(min_data)
        result_data = result_data.reset_index(drop = True).drop(["operation"], axis=1)

        result_data.to_json("result/soln3.json", orient="records")

    def question_four(self):
        """
        Solve Question 4: Given a time range, find out the lowest and highest price of the given stock in between the range
        Write the result in a JSON file
        :return: None
        """

        """
        Do not run if both start date and end date is not present
        """
        if not self.startDate or not self.endDate:
            print("Both Start Date and end Date must be provided")
            return

        # Get the highest value
        max_data = self.filtered_data.loc[self.filtered_data.reset_index(drop = True).groupby(['Name'])['high'].idxmax()]

        # Get the lowest value
        min_data = self.filtered_data.loc[self.filtered_data.reset_index(drop = True).groupby(['Name'])['low'].idxmin()]

        result_data = max_data.append(min_data)
        result_data.to_json("result/soln4.json", orient="records")


