import datetime

def get_episode_date(episode_number):
    ##start date
    start_date = datetime.date(2008,7,28)

    ##calculate total week days
    weekdays_passed = episode_number-1

    # Calculate total days passed including weekends
    weeks_passed = weekdays_passed // 5

    extra_days = weekdays_passed % 5

    total_days_passed = weeks_passed * 7 + extra_days

    air_date = start_date + datetime.timedelta(days=total_days_passed)

    return air_date


# Example usage
episode_number = 11
print(f"Episode {episode_number} aired on {get_episode_date(episode_number)}")