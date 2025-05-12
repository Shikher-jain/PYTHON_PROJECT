let gameBoard = [];
let currentPlayer = "X";
let winner = null;

for (let i = 0; i < 9; i++) {
    gameBoard.push("");
    document.getElementById(`cell-${i}`).addEventListener("click", makeMove);
}

function makeMove(event) {
    const cellIndex = event.target.id.split("-")[1];
    if (gameBoard[cellIndex] === "") {
        gameBoard[cellIndex] = currentPlayer;
        event.target.classList.add(currentPlayer.toLowerCase());
        checkWin();
        currentPlayer = currentPlayer === "X"? "O" : "X";
    }
}

function checkWin() {
    const winConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for (let i = 0; i < winConditions.length; i++) {
        const condition = winConditions[i];
        if (gameBoard[condition[0]] === gameBoard[condition[1]] && gameBoard[condition[1]] === gameBoard[condition[2]] && gameBoard[condition[0]]!== "") {
            winner = gameBoard[condition[0]];
            alert(`Player ${winner} wins!`);
            return;
        }
    }

    if (!gameBoard.includes("")) {
        alert("It's a draw!");
    }
}