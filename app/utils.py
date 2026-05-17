import re

# Custom Decorator to print messages before functions
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[System Log] Now working on: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Regex validation: checks if input is a normal number
def check_number_format(input_string):
    my_pattern = r"^\d+(\.\d+)?$"
    if re.match(my_pattern, input_string):
        return True
    return False

# Custom Generator for processing history items
def loops_through_weights(history):
    for item in history:
        yield item['weight']

# Functional Programming Tools (lambda, map, filter)
def find_bad_bmis(history):
    # Filters BMIs higher than 25 (overweight) and maps them
    bad_list = list(map(lambda x: x['bmi'], filter(lambda x: x['bmi'] > 25, history)))
    return bad_list

# ASCII Progress Graph using basic symbols
def print_ascii_chart(history):
    print("\n=== YOUR WEIGHT GRAPH ===")
    for weight in loops_through_weights(history):
        # Draw bars using # symbol
        total_hashes = int(weight / 2)
        print(f"Weight: {weight:5.1f} kg | {'#' * total_hashes}")
    print("=========================\n")