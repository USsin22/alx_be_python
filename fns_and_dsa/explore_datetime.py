from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format and print the current date and time as YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt the user for number of days
    days = int(input("Enter the number of days to add to the current date: "))
    # Save the future date
    future_date = datetime.now() + timedelta(days=days)
    # Print the future date in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
