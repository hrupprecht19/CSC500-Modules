#part1 Create a program that will ask the number of years then start a loop for the 12months
#start with a class
class RainfallTracker:
    def __init__(self):#make sure to have 2 _ in front and back #or errors
        self._monthly_rainfall = {}  # Store rainfall data
        self._total_rainfall = 0 #adding the _to the front makes it raw data
        self._total_months = 0
        # Define month names for validation and display
        self._month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
  
    def set_rainfall(self, year, month_name, amount):
        """Setter method to validate and store rainfall data"""
        if not isinstance(year, int):#isinstance() check is crucial for data validation 
            raise ValueError("Year must be an integer")
        if not isinstance(month_name, str):
            raise ValueError("Month must be a string")
        if amount < 0:
            raise ValueError("Rainfall amount cannot be negative")
            
        # Convert month name to number (1-12) for storage
        try:
            month_number = self._month_names.index(month_name.capitalize()) + 1
        except ValueError:
            raise ValueError(f"Invalid month name. Must be one of: {', '.join(self._month_names)}")
            
        key = (year, month_number)
        self._monthly_rainfall[key] = amount
        self._total_rainfall += amount
        self._total_months += 1
    
    @property #@property help with decorator is used to create read-only properties
    def total_months(self):
        """Getter for total months"""
        return self._total_months
    
    @property
    def total_rainfall(self):
        """Getter for total rainfall"""
        return self._total_rainfall
    
    @property
    def average_rainfall(self):
        """Getter for average rainfall"""
        if self._total_months == 0:
            return 0
        return self._total_rainfall / self._total_months

def main():
    tracker = RainfallTracker()
    
    # Get number of years
    num_years = int(input("Enter the number of years: "))
    
    # Collect rainfall data
    for year in range(1, num_years + 1):
        print(f"\nEnter rainfall amounts for Year {year}:")
        for month_name in tracker._month_names:
            while True:
                try:
                    amount = float(input(f"{month_name} rainfall (inches): "))
                    tracker.set_rainfall(year, month_name, amount)
                    break
                except ValueError as e:
                    print(f"Error: {e}")
    
    # Display results
    print("\nResults:")
    print(f"Total number of months: {tracker.total_months}")
    print(f"Total rainfall: {tracker.total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {tracker.average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()    