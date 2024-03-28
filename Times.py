from Calendars import Hijri, Gregorian


class Times:
    def __init__(self, data=None, meta=None):
        self.meta = meta
        tracked_times = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
        if data is not None:
            self.prayer_times = {
                time: data["timings"][time] or None for time in tracked_times
            }
            self.hijri_date = Hijri(data["date"]["hijri"])
            self.gregorian_date = Gregorian(data["date"]["gregorian"])

            self.formatted_times = "\n".join(
                f"{time}: {self.prayer_times[time]}" for time in tracked_times
            )

    def __str__(self):
        return f"""
{self.hijri_date.get_formatted_date()}
{self.gregorian_date.get_formatted_date()}

{self.formatted_times}
        """
