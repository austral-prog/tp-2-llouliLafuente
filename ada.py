def ada(first_name, last_name):
    lower_case = f"{first_name.lower()} {last_name.lower()}"
    upper_case = f"{first_name.upper()} {last_name.upper()}"
    title_case = f"{first_name.capitalize()} {last_name.capitalize()}"
    lower_case_with_dot = f"{lower_case}."
    return lower_case, upper_case, title_case, lower_case_with_dot

first_name = "AdA"
last_name = "LoVeLAce"

lower_case, upper_case, title_case, lower_case_with_dot = ada(first_name, last_name)

print(lower_case)
print(title_case)
print(upper_case)
print(lower_case_with_dot)
