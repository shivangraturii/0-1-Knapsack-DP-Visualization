import time
import os


# ---------------------------------------------------------
# Function to display the DP table
# ---------------------------------------------------------
def display_dp_table(dp, weights, values, current_item, W):

    # Clear terminal to create a live-animation effect
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n========== 0/1 KNAPSACK DP TABLE ==========\n")
    print(f"Items processed: {current_item}")

    if current_item > 0:
        print(
            f"Current Item -> Weight: {weights[current_item - 1]}, "
            f"Value: {values[current_item - 1]}"
        )

    print()

    # Print capacity numbers
    print("Item\\W |", end="")

    for w in range(W + 1):
        print(f"{w:4}", end="")

    print()

    # Print separator
    print("-" * (8 + 4 * (W + 1)))

    # Print DP table
    for i in range(current_item + 1):

        print(f"{i:6} |", end="")

        for w in range(W + 1):
            print(f"{dp[i][w]:4}", end="")

        print()

    print("\n===========================================\n")


# ---------------------------------------------------------
# 0/1 Knapsack Dynamic Programming Algorithm
# ---------------------------------------------------------
def knapsack(weights, values, W, visualize=True):

    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Show initial table
    if visualize:
        display_dp_table(dp, weights, values, 0, W)
        time.sleep(0.5)

    # Build DP table
    for i in range(1, n + 1):

        for w in range(W + 1):

            # Check if current item can fit
            if weights[i - 1] <= w:

                # Value if we INCLUDE the item
                include = (
                    values[i - 1]
                    + dp[i - 1][w - weights[i - 1]]
                )

                # Value if we EXCLUDE the item
                exclude = dp[i - 1][w]

                # Choose maximum value
                dp[i][w] = max(include, exclude)

            else:

                # Item cannot fit
                dp[i][w] = dp[i - 1][w]

        # Show live DP table after processing each item
        if visualize:
            display_dp_table(
                dp,
                weights,
                values,
                i,
                W
            )

            time.sleep(0.7)

    # Bottom-right cell contains final answer
    return dp[n][W]


# ---------------------------------------------------------
# Read all test cases from the input file
# ---------------------------------------------------------
def read_test_cases(filename):

    test_cases = []

    with open(filename, "r") as file:
        lines = file.readlines()

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        # A new test case starts
        if line.startswith("#Test"):

            i += 1

            # Skip empty lines
            while i < len(lines) and lines[i].strip() == "":
                i += 1

            # First line contains:
            # number of items (n) and capacity (W)
            n, W = map(int, lines[i].split())

            weights = []
            values = []

            # Read n weight-value pairs
            for _ in range(n):

                i += 1

                weight, value = map(
                    int,
                    lines[i].split()
                )

                weights.append(weight)
                values.append(value)

            # Store test case
            test_cases.append(
                (n, W, weights, values)
            )

        i += 1

    return test_cases


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
def main():

    input_file = "Knapsack data (2).txt"
    output_file = "result.txt"

    # Read all test cases
    test_cases = read_test_cases(input_file)

    results = []

    print(f"\nTotal Test Cases: {len(test_cases)}")

    # Solve each test case
    for test_number, test in enumerate(
        test_cases,
        start=1
    ):

        n, W, weights, values = test

        print("\n" + "=" * 60)
        print(f"TEST CASE {test_number}")
        print(f"Number of Items = {n}")
        print(f"Knapsack Capacity = {W}")
        print(f"Weights = {weights}")
        print(f"Values  = {values}")
        print("=" * 60)

        # Run 0/1 Knapsack
        result = knapsack(
            weights,
            values,
            W,
            visualize=True
        )

        # Save result
        results.append(
            (test_number, n, W, result)
        )

        print("\n--------------------------------")
        print(f"Maximum Total Value = {result}")
        print("--------------------------------")

        # Wait before next test
        input("\nPress ENTER for next test case...")


    # -----------------------------------------------------
    # Write results to result.txt
    # -----------------------------------------------------
    with open(output_file, "w") as file:

        for test_number, n, W, result in results:

            file.write(
                f"#Test{test_number} input ({n} {W}) "
                f"{result}\n"
            )


    print("\n========================================")
    print("ALL TEST CASES COMPLETED")
    print("Results stored successfully in result.txt")
    print("========================================")


# ---------------------------------------------------------
# Start Program
# ---------------------------------------------------------
if __name__ == "__main__":
    main()