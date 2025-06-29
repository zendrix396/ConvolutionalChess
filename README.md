# Chess Engine

* Establish the Search Tree
* Neural Net to ***prune*** the Search Tree
##
## Converting Board State to Vector

**State(Board):**

Pieces (2+7*2=16)
* Universal
    * Blank
    * Blank (En Passant)
* Pieces
    * Pawn
    * Bishop
    * Knight
    * Rook
    * Rook (can castle)
    * Queen
    * King

Extra State:
* which one to move

> **8x8x4+1 = 257 bits (vectors of 0 or 1)**


### Bellman Equation
>Value(Current State) = Immediate_Reward + Value(Next_state)
### MiniMax
>Calculating the next best possible move considering the opponent has also selected the it's best possible move