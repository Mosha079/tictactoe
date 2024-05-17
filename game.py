""" Simple Tic-Tac-Toe Game.

Author: Matthew Epstein
"""


class Game:
    """Class the holds all the parts of the game.
    """

    def __init__(self):
        self.objects = {
            (0, 0): "_",
            (1, 0): "_",
            (2, 0): "_",
            (0, 1): "_",
            (1, 1): "_",
            (2, 1): "_",
            (0, 2): "_",
            (1, 2): "_",
            (2, 2): "_"
        }

    def get_match(self, num):
        """Location of each square on the board.

        Args:
            num (int): The number associated with the square 

        Returns:
            tuple: The coordinates of the square
        """
        match num:
            case 1:
                return (0, 0)
            case 2:
                return (1, 0)
            case 3:
                return (2, 0)
            case 4:
                return (0, 1)
            case 5:
                return (1, 1)
            case 6:
                return (2, 1)
            case 7:
                return (0, 2)
            case 8:
                return (1, 2)
            case 9:
                return (2, 2)

    def update(self, square, obj):
        """Updates the board.

        Args:
            square (int): Square on the board
            obj (str): The X or the O to place
        """
        current = self.objects.get(self.get_match(square))
        while not current == "_":
            print(f"There is already a \"{current}\" there, try again")
            square = int(input("Please enter square number: "))
            current = self.objects.get(self.get_match(square))
        self.objects[self.get_match(square)] = obj

    def design(self):
        """Prints the board to screen.
        """
        for row in range(3):
            print(f"{self.objects.get((0, row))}", end="")
            print(f"|{self.objects.get((1, row))}", end="")
            print(f"|{self.objects.get((2, row))}")

    def judge(self):
        """Two massive if statements to determine winner or tie.

        Returns:
            bool: whether game ended or not
            str: the letter that won, or tie if no one did
        """
        count = 0
        for value in self.objects.values():
            if not value == "_":
                count += 1
        if count > 5:
            if ((self.objects.get(self.get_match(1))) == "X" and (self.objects.get(self.get_match(2))) == "X" and (self.objects.get(self.get_match(3))) == "X") or (
                    (self.objects.get(self.get_match(1))) == "X" and (self.objects.get(self.get_match(5))) == "X" and (self.objects.get(self.get_match(9))) == "X") or (
                    (self.objects.get(self.get_match(1))) == "X" and (self.objects.get(self.get_match(4))) == "X" and (self.objects.get(self.get_match(7))) == "X") or (
                    (self.objects.get(self.get_match(2))) == "X" and (self.objects.get(self.get_match(5))) == "X" and (self.objects.get(self.get_match(8))) == "X") or (
                    (self.objects.get(self.get_match(3))) == "X" and (self.objects.get(self.get_match(5))) == "X" and (self.objects.get(self.get_match(7))) == "X") or (
                    (self.objects.get(self.get_match(3))) == "X" and (self.objects.get(self.get_match(6))) == "X" and (self.objects.get(self.get_match(9))) == "X") or (
                    (self.objects.get(self.get_match(4))) == "X" and (self.objects.get(self.get_match(5))) == "X" and (self.objects.get(self.get_match(6))) == "X") or (
                    (self.objects.get(self.get_match(7))) == "X" and (self.objects.get(self.get_match(8))) == "X" and (self.objects.get(self.get_match(9))) == "X"):
                return True, "X"

            elif ((self.objects.get(self.get_match(1))) == "O" and (self.objects.get(self.get_match(2))) == "O" and (self.objects.get(self.get_match(3))) == "O") or (
                    (self.objects.get(self.get_match(1))) == "O" and (self.objects.get(self.get_match(5))) == "O" and (self.objects.get(self.get_match(9))) == "O") or (
                    (self.objects.get(self.get_match(1))) == "O" and (self.objects.get(self.get_match(4))) == "O" and (self.objects.get(self.get_match(7))) == "O") or (
                    (self.objects.get(self.get_match(2))) == "O" and (self.objects.get(self.get_match(5))) == "O" and (self.objects.get(self.get_match(8))) == "O") or (
                    (self.objects.get(self.get_match(3))) == "O" and (self.objects.get(self.get_match(5))) == "O" and (self.objects.get(self.get_match(7))) == "O") or (
                    (self.objects.get(self.get_match(3))) == "O" and (self.objects.get(self.get_match(6))) == "O" and (self.objects.get(self.get_match(9))) == "O") or (
                    (self.objects.get(self.get_match(4))) == "O" and (self.objects.get(self.get_match(5))) == "O" and (self.objects.get(self.get_match(6))) == "O") or (
                    (self.objects.get(self.get_match(7))) == "O" and (self.objects.get(self.get_match(8))) == "O" and (self.objects.get(self.get_match(9))) == "O"):
                return True, "O"
            elif count == 9:
                return True, "T"
        return False, ""


def main():
    """What runs the game."""
    print("Welcome to my Tic Tac Toe!")
    print("To say which square you wish to place X/O, type the number it correlates with")
    print("It follows this pattern:\n1 2 3\n4 5 6\n7 8 9")
    run = Game()
    three_row = (False, "")
    moves = 0
    while not three_row[0]:
        if moves % 2 == 0:
            turn = "O"
        else:
            turn = "X"
        run.design()
        print(f"It is {turn} turn")
        position = int(input("Please enter square number: "))
        run.update(position, turn)
        three_row = run.judge()
        moves += 1
    run.design()
    if three_row[1] == "T":
        print("The game ended in a tie")
    else:
        print(f"Congratulations {three_row[1]} won in {moves} moves!")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
