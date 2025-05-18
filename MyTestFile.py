import os # Bug: Unused import (depending on SonarQube rules)

def greet(name, title):
  """Greets a person with their name and title."""
  # Bug: Potential for inconsistent capitalization if title is not controlled
  message = "Hello, " + title.capitalize() + " " + name.capitalize() + "!"
  print(message)
  # Bug: Redundant print statement (could be a SonarQube 'code smell')
  print("Greeting complete.")

def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  # Bug: Unused variable 'perimeter'
  perimeter = 2 * (length + width)
  if length <= 0 or width <= 0:
    # Bug: Returning None implicitly, could lead to issues if not handled by caller
    print("Error: Length and width must be positive.")
    return
  area = length * width
  return area

def get_user_info(user_id):
  """Retrieves user information."""
  # Bug: Hardcoded sensitive information (Security Hotspot)
  db_password = "supersecretpassword123"
  if user_id == 1:
    # Bug: Inconsistent return type (dict vs None)
    return {"name": "Alice", "email": "alice@example.com"}
  # Missing return statement for other user_ids, will implicitly return None

def main():
  # Bug: Variable 'unused_var' is assigned but never used
  unused_var = "I am not used"

  greet("bob", "mr")
  greet("alice", "ms") # Bug: Potential for 'ms' not being the desired capitalization

  area1 = calculate_area(5, 10)
  if area1: # Potentially problematic if None is returned and not explicitly checked
    print(f"Area 1: {area1}")

  area2 = calculate_area(-5, 10) # Will print error and return None
  # Bug: Attempting to use the result of calculate_area which might be None
  # This could raise an AttributeError if you try to operate on area2 assuming it's a number
  if area2 is not None:
      print(f"Area 2: {area2}")
  else:
      print("Area 2 could not be calculated.")


  user = get_user_info(1)
  # Bug: Accessing a key that might not exist if get_user_info returns None (e.g., for user_id=2)
  # SonarQube might flag this as a potential NullPointerException equivalent
  if user:
    print(f"User Name: {user['name']}")

  user2 = get_user_info(2) # Will return None
  if user2: # This check prevents the error for user2
      print(f"User Name: {user2['name']}")
  else:
      print("User 2 not found.")

  # Bug: Division by zero
  # SonarQube should flag this as a critical issue.
  # However, SonarQube's static analysis might not always catch runtime errors
  # that depend on specific execution paths not easily determined statically.
  # Let's make it more obvious for static analysis.
  denominator = 0
  if denominator == 0: # This makes the check trivial for some analyzers
      print("Attempting to divide by zero (statically detectable path)")
      # result = 10 / denominator # Uncomment to see SonarQube flag it (if it can)
                                  # or a runtime error.
                                  # For a guaranteed SonarQube finding, a more direct
                                  # division by a literal zero might be needed,
                                  # but this is a common pattern.

  # Bug: Inefficient string concatenation in a loop (Code Smell)
  my_list = ["a", "b", "c", "d", "e"]
  result_string = ""
  for item in my_list:
    result_string += item + "," # More efficient to use "".join()
  print(f"Concatenated string: {result_string}")


if __name__ == "__main__":
  main()
