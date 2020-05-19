def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


user_input = float(input ("Enter the Temperature:"))
print(weather_condition(user_input))
    