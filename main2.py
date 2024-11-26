import random

class SnakeWaterGunGame:
    def __init__(self):
        self.choices = {"s": 1, "w": -1, "g": 0}
        self.reverse_choices = {1: "snake", -1: "water", 0: "gun"}
        self.computer_choice = None
        self.user_choice = None

    def get_computer_choice(self):
        self.computer_choice = random.choice([-1, 0, 1])

    def get_user_choice(self, user_input):
        if user_input in self.choices:
            self.user_choice = self.choices[user_input]
        else:
            raise ValueError("Invalid input. Choose 's' for snake, 'w' for water, or 'g' for gun.")

    def determine_winner(self):
        if self.computer_choice == self.user_choice:
            return "It's a draw!"
        elif (
            (self.computer_choice == -1 and self.user_choice == 1) or
            (self.computer_choice == 1 and self.user_choice == 0) or
            (self.computer_choice == 0 and self.user_choice == -1)
        ):
            return "You win!"
        else:
            return "You lose!"

    def play(self, user_input):
        self.get_computer_choice()
        self.get_user_choice(user_input)

        print(f"You chose: {self.reverse_choices[self.user_choice]}")
        print(f"Computer chose: {self.reverse_choices[self.computer_choice]}")

        result = self.determine_winner()
        print(result)

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()
    try:
        game = SnakeWaterGunGame()
        game.play(user_input)
    except ValueError as e:
        print(e)
2+