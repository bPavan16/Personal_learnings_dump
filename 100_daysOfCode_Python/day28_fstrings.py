""" Fstring is used for string formatting and it has made it easy to format stings """

letter = "Hey my name is {1} and I am From {0}"
country = "India"
name = "Pavan"

print(letter.format(country, name))

print(f"Hey my Name is {name} and I am from {country}")

price = 4.9823

txt = f"For Only {price:.2f} dollars"

print(txt)

print(f"The value of {2 * 30}")

# We want to lierally print The fString Literally Then we use

print(f"Hey my Name is {{name}} and I am from {{country}}")
