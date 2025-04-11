def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    count = 0

    while count < 5:
        user_input = int(input(f"Enter integer #{count + 1}: "))
        total += user_input
        count += 1

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    print(main())  # Print the total so user can see the result
