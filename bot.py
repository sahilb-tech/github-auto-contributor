from datetime import datetime
from pathlib import Path

# Get the current date and time
now = datetime.now()

# Create an activity message
activity = f"Activity recorded on {now.strftime('%Y-%m-%d %H:%M:%S')}\n"

# Define the activity file
activity_file = Path("activity/daily.md")

# Create the activity folder if it doesn't exist
activity_file.parent.mkdir(parents=True, exist_ok=True)

# Add the activity to the file
with activity_file.open("a", encoding="utf-8") as file:
    file.write(activity)

print(f"Activity recorded: {activity.strip()}")