class ticker:
    # ... existing methods ...

    def summary(self):
        # Implementation of summary method
        pass

    def statistics(self):
        # Implementation of statistics method
        pass

    def profile(self, description=True):
        # Implementation of profile method
        pass

    def get_stock_data(self):
        # Call the existing methods and store their results
        summary_data = self.summary()
        statistics_data = self.statistics()
        profile_data = self.profile(description=False)

        # Create a dictionary to hold the results
        stock_data = {
            'summary': summary_data,
            'statistics': statistics_data,
            'profile': profile_data
        }

        # Return the dictionary
        return stock_data
