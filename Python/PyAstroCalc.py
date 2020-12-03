# AstroCal.py
# Author : Alana Rust
# Date: 11-24-2020
name = input("Enter your name: ")
day = int(input("Enter your date of birth (Ex: 19): ")) 
month = (input("Enter your birth month (Ex: June): ")) 
# resolves any capitilization errors 
month = month.capitalize()
sunSign = None 
def main():
    # Aries + Pisces
    if month == "March": 
        if day > 21:
            sunSign = "Aries"
        else:
            sunSign = "Pisces"

    # Aries + Taurus
    elif month == "April":
        if day < 19:
            sunSign = "Aries"
        else: 
            sunSign = "Taurus"

    # Taurus + Gemini
    elif month == "May":
        if day < 20:
            sunSign = "Taurus"
        else:
            sunSign = "Gemini"

    # Gemini + Cancer 
    elif month == "June":
        if day > 20:
            sunSign = "Gemini"
        else:
            sunSign = "Cancer"

    # Cancer + Leo
    elif month == "July":
        if day < 23:
            sunSign = "Cancer"
        else: 
            sunSign = "Leo"

    # Leo + Virgo
    elif month == "August":
        if day < 22: 
            sunSign = "Leo"
        else: 
            sunSign = "Virgo"

    # Virgo + Libra
    elif month == "September":
        if day < 22:
            sunSign = "Virgo"
        else:
            sunSign = "Libra" 

    # Libra + Scorpio
    elif month == "October":
        if day < 22:
            sunSign = "Libra"
        else: 
            sunSign = "Scorpio"

    # Scorpio + Sag
    elif month == "November":
        if day < 21:
            sunSign = "Scorpio"
        else: sunSign = "Sagittarius" 

    # Sag + Capricorn
    elif month == "December":
        if day < 21:
            sunSign = "Sagittarius"
        else:
            sunSign = "Capricorn"

    # Capricorn + Aquarius
    elif month == "January":
        if day < 19:
            sunSign = "Capricorn"
        else:
            sunSign = "Aquarius"

    # Aquarius + Pisces
    elif month == "February":
        if day < 19:
            sunSign = "Aquarius"
        else:
            sunSign = "Pisces"
    print("Your sun sign is: " + sunSign)


main()
