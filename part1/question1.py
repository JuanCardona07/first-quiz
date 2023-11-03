################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
    temperature = None

    if city == "Quito":
        temperature = 22
    elif city == "Sao Paulo":
        temperature = 17
    elif city == "San Francisco":
        temperature = 16

    return temperature

def get_city_weather(city):
    temperature = get_city_temperature(city)
    sky_condition = None

    if temperature is not None:
        if city == "Sao Paulo":
            sky_condition = "cloudy"
        elif city == "New York":
            sky_condition = "rainy"
        elif city == "Quito":
            sky_condition = "sunny"
        elif city == "San Francisco":
            sky_condition = "foggy"
        else:
            sky_condition = "unknown"

        return f"{temperature} degrees and {sky_condition}"
    else:
        return "City temperature is unknown"

print(get_city_weather("Quito"))
print(get_city_weather("Sao Paulo"))
print(get_city_weather("San Francisco"))
print(get_city_weather("New York"))
print(get_city_weather("London"))