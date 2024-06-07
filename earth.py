def compare_countries(country1, country2):
    print("The result of " + str(country1) + " comes first in the dictionary than " + str(country2) + " is " + str(country1 < country2))
    print("The result of " + str(country2) + " comes first in the dictionary than " + str(country1) + " is " + str(country2 < country1))

X = "Bangladesh"
Y = "Barbados"

compare_countries(X, Y)

