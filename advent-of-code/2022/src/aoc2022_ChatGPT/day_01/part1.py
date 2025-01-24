def get_food_items(filepath):
      # open the file in read mode
    with open(filepath, 'r') as file:
      # read the contents of the file into a list, where each element is a line
      # in the file
      food_items = file.readlines()

    # convert each element in the list (which is a string) to an integer
    # food_items = [int(item) for item in food_items]
    
    return food_items

    # the list of food items is now stored in the food_items variable as a list
    # of integers


def get_result(food_items):
    # input: a list of food items and their corresponding Calories

    # initialize variables to keep track of the current Elf's Calories and the
    # maximum number of Calories seen so far
    current_elf_calories = 0
    max_calories = 0

    # iterate over the list of food items
    for item in food_items:
      # if the item is a blank line, we've reached the end of the current Elf's
      # inventory, so we can compare the current Elf's Calories to the maximum
      # and update the maximum if necessary
      if item == '':
        max_calories = max(max_calories, current_elf_calories)
        current_elf_calories = 0
      else:
        # if the item is not a blank line, we add its Calories to the current
        # Elf's Calories
        current_elf_calories += item

    # once we've reached the end of the list, we need to compare the final
    # current Elf's Calories to the maximum and update the maximum if necessary
    max_calories = max(max_calories, current_elf_calories)

    # return the maximum number of Calories seen
    return max_calories

get_food_items('/Users/brentbrewington/github/advent-of-code/2022/docs/day_01/example_input.txt')
get_result(get_food_items('/Users/brentbrewington/github/advent-of-code/2022/docs/day_01/example_input.txt'))