# Display a welcome message to the user
print("Welcome to the square game")

# Get the initial number of coins from the user
coins_number = int(input("Enter number of coins: "))

# Save the initial number of coins for reference
X = coins_number

# Start the main game loop
while coins_number > 0:
    # Player 1's turn
    p1 = int(input("Player 1, choose a number: "))
    
    # Validate player 1's input
    while True:
        if int(p1**0.5)**2 == p1 and p1 <= coins_number and p1 < X:
            break
        else:
            p1 = int(input("Please enter a valid number: "))

    # Update the number of coins after player 1's move
    coins_number = coins_number - p1
    
    # Display the updated number of coins
    print("Number of coins left: ", coins_number)

    # Check if player 1 has won
    if coins_number == 0:
        print("Player 1 wins")
        break
    
    # Player 2's turn
    p2 = int(input("Player 2, choose a number: "))
    
    # Validate player 2's input
    while True:
        if int(p2**0.5)**2 == p2 and p2 <= coins_number: 
            break
        else:
            p2 = int(input("Please enter a valid number: "))

    # Update the number of coins after player 2's move
    coins_number = coins_number - p2
    
    # Display the updated number of coins
    print("Number of coins left: ", coins_number)

    # Check if player 2 has won
    if coins_number == 0:
        print("Player 2 wins")
        break
