def add_time(start, duration, day=None):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    # Parse start time
    t, p = start.split()
    h, m = map(int, t.split(":"))
    h = (h % 12) + (12 if p == "PM" else 0)
    start_minutes = h * 60 + m

    # Parse duration
    dh, dm = map(int, duration.split(":"))
    total_minutes = start_minutes + dh * 60 + dm

    # Days later
    days_later, total_minutes = divmod(total_minutes, 24 * 60)

    # Convert back
    h, m = divmod(total_minutes, 60)
    p = "AM" if h < 12 else "PM"
    h = h % 12 or 12

    # Result string
    result = str(h) + ":" + str(m).zfill(2) + " " + p

    # Add day if provided
    if day:
        day_index = days.index(day.capitalize())
        new_day = days[(day_index + days_later) % 7]
        result += ", " + new_day

    # Add days later info
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += " (" + str(days_later) + " days later)"

    return result
