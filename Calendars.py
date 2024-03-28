class Calendar:
    def __init__(self, calendar_data):
        self.date = calendar_data["date"]
        self.format = calendar_data["format"]
        self.day = calendar_data["day"]
        self.weekday = calendar_data["weekday"]
        self.month = calendar_data["month"]
        self.year = calendar_data["year"]
        self.designation = calendar_data["designation"]
        self.lang = "en"

    def __str__(self):
        return f"""
        Date: {self.date}
        Format: {self.format}
        Day: {self.day}
        Weekday: {self.weekday[self.lang]}
        Month: {self.month[self.lang]}
        Year: {self.year}
        Designation: {self.designation["abbreviated"]}
        """

    def get_formatted_date(self):
        def day_suffix():
            if self.day in [1, 21, 31]:
                return "st"
            elif self.day in [2, 22]:
                return "nd"
            elif self.day in [3, 23]:
                return "rd"
            else:
                return "th"

        return f"{self.day + day_suffix()} of {self.month[self.lang]} {self.year}"


class Hijri(Calendar):
    def __init__(self, hijri_data):
        super().__init__(hijri_data)
        self.holidays = hijri_data["holidays"]


class Gregorian(Calendar):
    def __init__(self, gregorian_data):
        super().__init__(gregorian_data)
