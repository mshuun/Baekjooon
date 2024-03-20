def zodiac(date):
    month_day = int(date[5:7] + date[8:10])
    if (month_day >= 321 and month_day <= 419):
        return "Aries"
    elif (month_day >= 420 and month_day <= 520):
        return "Taurus"
    elif (month_day >= 521 and month_day <= 620):
        return "Gemini"
    elif (month_day >= 621 and month_day <= 722):
        return "Cancer"
    elif (month_day >= 723 and month_day <= 822):
        return "Leo"
    elif (month_day >= 823 and month_day <= 922):
        return "Virgo"
    elif (month_day >= 923 and month_day <= 1022):
        return "Libra"
    elif (month_day >= 1023 and month_day <= 1122):
        return "Scorpio"
    elif (month_day >= 1123 and month_day <= 1221):
        return "Sagittarius"
    elif (month_day >= 1222 or month_day <= 119):
        return "Capricorn"
    elif (month_day >= 120 and month_day <= 218):
        return "Aquarius"
    else:
        return "Pisces"


date = input().strip()
print(zodiac(date))
