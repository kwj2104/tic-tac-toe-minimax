class Board:

    def __init__(self):
        self.__board = [[0 for x in range(3)] for y in range(3)]
        self.__complete = False
        self.__tie = False
        self.__move_count = 0
        self.__row = 0
        self.__column = 0

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, values):

        row, column, value, player = values
        self.__row = row
        self.__column = column
        self.__board[self.__row][self.__column] = value
        self.__move_count += 1

    def check_board(self):

        #Check for completed rows and columns after current move
        row_values = [self.__board[self.__row][x] for x in range(3)]
        column_values = [self.__board[x][self.__column] for x in range(3)]
        if (len(set(row_values)) <=1 or len(set(column_values)) <=1) and self.__move_count != 0:
            self.__complete = True

        #Check for completed diagonals regardless of move
        diag_values_left = [self.__board[x][x] for x in range(3)]
        diag_values_right = [self.__board[x][2 - x] for x in range(3)]
        if len(set(diag_values_left)) <= 1 and sum(diag_values_left) != 0:
            self.__complete = True
        if len(set(diag_values_right)) <= 1 and sum(diag_values_right) != 0:
            self.__complete = True

        #Check for a tie
        if (self.__move_count == 9) and self.__complete == False:
            self.__tie = True
            self.__complete = True

        return self.__complete, self.__tie

    def display_board(self):
        def display_icons(x):
            if x == 0:
                return " "
            elif x == 1:
                return "o"
            else:
                return "x"

        icon_list = [list(map(display_icons, x)) for x in self.__board]

        for x in range(3):
            print("[ {} {} {} ]".format(icon_list[x][0], icon_list[x][1], icon_list[x][2]))










