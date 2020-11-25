# AstroCal.py
# Author : Alana Rust
# Date: 11-24-2020
name = input("Enter your name:")
day = 22 # add input 
month = "December" # add input 
sunSign = None 
 # def main():
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
elif month == "September":
    if day < 22:
        sunSign = "Virgo"
    else:
        sunSign = "Libra" 
elif month == "October":
    if day < 22:
        sunSign = "Libra"
    else: 
        sunSign = "Scorpio"
elif month == "November":
    if day < 21:
        sunSign = "Scorpio"
    else: sunSign = "Sagittarius" 
elif month == "December":
    if day < 21:
        sunSign = "Sagittarius"
    else:
        sunSign = "Capricorn"
elif month == "January":
    if day < 19:
        sunSign = "Capricorn"
    else:
        sunSign = "Aquarius"

