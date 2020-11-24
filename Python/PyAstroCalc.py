# AstroCal.py
# Author : Alana Rust
# Date: 11-24-2020
day = 22
month = "December"
sunSign = None 

# Aries + Pisces
if month == "March": 
    if day > 21:
        sunSign = "Aries"
    else:
        sunSign = "Pisces"
if month == "April":
    if day < 19:
        sunSign = "Aries"
    else: 
        sunSign = "Taurus"
if month == "May":
    if day < 20:
        sunSign = "Taurus"
    else:
        sunSign = "Gemini"
if month == "June":
    if day > 20:
        sunSign = "Gemini"
    else:
        sunSign = "Cancer"
if month == "July":
    if day