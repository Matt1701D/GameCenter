from Board import Board

class OthelloBoard(Board):

    def __init__(self, boardSize, delimeter):
        super().__init__(boardSize, delimeter)

        self.__pieceCount = {"B":2,"W":2,str(self._delimeter):(self._boardSize**2)-4}
        self.__tmpMove = []
        self._initBoard()

    # PROPERTIES

    @property
    def PieceCount(self):
        return self.__pieceCount

    # PUBLIC METHODS

    # ensure move is valid
    def validateMove(self, turn, coord):
        Y = int(coord[0])
        X = int(coord[1])
        
        if self._gameBoard[Y][X] != self._delimeter:
            return 0 
        else:
            return self.__isValidMove(turn, coord)

    # store turn in board and transposed board
    def makeMove(self, turn, coord):
        if self.validateMove(turn, coord):
            self._updateBoard(coord, turn)

    # check for winner
    def checkWinner(self):
        if 0 in self.__pieceCount.values():
            if self.__pieceCount["B"] > self.__pieceCount["W"] :
               return 0
            elif self.__pieceCount["B"] < self.__pieceCount["W"]:
              return 1
            else:
              return 2

    # PROTECTED METHODS

    def _initBoard(self):
        super()._initBoard(1)

        self._gameBoard[3][3] = self._gameBoard[4][4] = "W"
        self._gameBoard[3][4] = self._gameBoard[4][3] = "B"

    # update gameBoard
    def _updateBoard(self, coord, turn, isNewPos=False):
        if self.__tmpMove:
            Y = int(coord[0])
            X = int(coord[1])

            self._gameBoard[Y][X] = turn
            self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
            self.__pieceCount[self._delimeter] = int(self.__pieceCount[self._delimeter]) - 1

            opp = "B" if turn == "W" else "W"
            for p in self.__tmpMove:
                self._gameBoard[p[0]][p[1]] = turn
                self.__pieceCount[turn] = int(self.__pieceCount[turn]) + 1
                self.__pieceCount[opp] = int(self.__pieceCount[opp]) - 1

            self.__tmpMove = []

    # PRIVATE METHODS

    # check all 8 directions for valid move and store flips in tmp list
    def __isValidMove(self, turn, coord):
        if  not self.__tmpMove:
            Y = int(coord[0])
            X = int(coord[1])
            opp = "B" if turn == "W" else "W"
            tmpMove = []

            # Check horizontal right
            myPieceFound = False
            if X < self._boardSize - 2 and self._gameBoard[Y][X+1] == opp:
                for i in range(X+1, self._boardSize):
                    if self._gameBoard[Y][i] == opp:
                        tmpMove.append([Y,i])
                    elif self._gameBoard[Y][i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check horizontal left
            myPieceFound = False
            if X > 1 and self._gameBoard[Y][X-1] == opp:
                for i in range(X-1, -1, -1):
                    if self._gameBoard[Y][i] == opp:
                        tmpMove.append([Y,i])
                    elif self._gameBoard[Y][i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()
            
            # Check vertical down
            myPieceFound = False
            if Y < self._boardSize - 2  and self._gameBoard[Y+1][X] == opp:
                for i in range(Y+1, self._boardSize):
                    if self._gameBoard[i][X] == opp:
                        tmpMove.append([i,X])
                    elif self._gameBoard[i][X] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check vertical up
            myPieceFound = False
            if Y > 1  and self._gameBoard[Y-1][X] == opp:
                for i in range(Y-1, -1, -1):
                    if self._gameBoard[i][X] == opp:
                        tmpMove.append([i,X])
                    elif self._gameBoard[i][X] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check diagonal up and right
            myPieceFound = False
            if X < self._boardSize - 2 and Y > 1 and self._gameBoard[Y-1][X+1] == opp:
                maxMve = min(Y, self._boardSize-1-X)

                for i in range(1, maxMve+1):
                    if self._gameBoard[Y-i][X+i] == opp:
                        tmpMove.append([Y-i,X+i])
                    elif self._gameBoard[Y-i][X+i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check diagonal up and left
            myPieceFound = False
            if X > 1 and Y > 1 and self._gameBoard[Y-1][X-1] == opp:
                maxMve = min(Y, X)

                for i in range(1, maxMve+1):
                    if self._gameBoard[Y-i][X-i] == opp:
                        tmpMove.append([Y-i,X-i])
                    elif self._gameBoard[Y-i][X-i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check diagonal down and right
            myPieceFound = False
            if X < self._boardSize - 2 and Y < self._boardSize - 2 and self._gameBoard[Y+1][X+1] == opp:
                maxMve = min(self._boardSize-1-Y, self._boardSize-1-X)

                for i in range(1, maxMve+1):
                    if self._gameBoard[Y+i][X+i] == opp:
                        tmpMove.append([Y+i,X+i])
                    elif self._gameBoard[Y+i][X+i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

            # Check diagonal down and left
            myPieceFound = False
            if X > 1 and Y < self._boardSize - 2 and self._gameBoard[Y+1][X-1] == opp:
                maxMve = min(self._boardSize-1-Y, X)

                for i in range(1, maxMve+1):
                    if self._gameBoard[Y+i][X-i] == opp:
                        tmpMove.append([Y+i,X-i])
                    elif self._gameBoard[Y+i][X-i] == self._delimeter:
                        break
                    else:
                        myPieceFound = True

            if myPieceFound and tmpMove:
                self.__tmpMove.extend(tmpMove)
            tmpMove.clear()

        return False if not self.__tmpMove else True