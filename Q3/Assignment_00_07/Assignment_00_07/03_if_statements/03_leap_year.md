def is_leap_year(year):
  """
  Checks if a given year is a leap year according to the Gregorian calendar rules.

  Args:
    year: An integer representing the year.

  Returns:
    True if the year is a leap year, False otherwise.
  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Get input from the user
try:
  year_input = int(input("Enter a year: "))

  # Check if it's a leap year and print the result
  if is_leap_year(year_input):
    print("That's a leap year!")
  else:
    print("That's not a leap year.")

except ValueError:
  print("Invalid input. Please enter a valid integer for the year.")