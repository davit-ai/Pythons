from datetime import datetime, timedelta


# Function to calculate age and days until next birthday
def calculate_age_and_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)

    # Adjust next birthday if it has already passed this year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    # Calculate age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Calculate days until next birthday
    days_until_birthday = (next_birthday - today).days

    return age, next_birthday.strftime('%Y-%m-%d'), days_until_birthday


# Run the function with user-provided birthdate
if __name__ == "__main__":
    your_birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    age, upcoming_birthday, days_remaining = calculate_age_and_birthday(your_birthdate)

    print(f"Your current age is: {age}")
    print(f"Your upcoming birthday is on: {upcoming_birthday}")
    print(f"Days remaining until your birthday: {days_remaining}")
