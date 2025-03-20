let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let gameMode = '';

function startGame(mode) {
    gameMode = mode;
    board = ['', '', '', '', '', '', '', '', ''];
    currentPlayer = 'X';
    updateBoard();
    document.getElementById('status').textContent = '';

    // Hide the buttons and show the board
    document.getElementById('buttons').style.display = 'none';
    document.getElementById('board').style.display = 'grid';
    document.getElementById('restart').style.display = 'block';
}

function makeMove(index) {
    if (board[index] !== '' || gameMode === '') return;

    board[index] = currentPlayer;
    updateBoard();

    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            board: board,
            player: currentPlayer,
            move: index,
            mode: gameMode
        })
    })
    .then(response => response.json())
    .then(data => {
        board = data.board;
        updateBoard();

        if (data.winner) {
            document.getElementById('status').textContent = `${data.winner} wins!`;
            gameMode = ''; // End the game
        } else if (board.every(cell => cell !== '')) {
            document.getElementById('status').textContent = "It's a tie!";
            gameMode = ''; // End the game
        } else {
            if (gameMode === 'computer' && currentPlayer === 'X') {
                currentPlayer = 'O';  // Computer's turn
                setTimeout(() => {
                    currentPlayer = 'X';  // Switch back to player
                }, 500); // Delay the switch back to give a clear sequence
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';  // Normal switch
            }
        }
    });
}


function restartGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    currentPlayer = 'X';
    gameMode = '';

    // Reset the board and status
    updateBoard();
    document.getElementById('status').textContent = '';
    document.getElementById('board').style.display = 'none';
    document.getElementById('buttons').style.display = 'block';
    document.getElementById('restart').style.display = 'none';
}

function updateBoard() {
    const boardElement = document.getElementById('board');
    boardElement.innerHTML = '';
    board.forEach((cell, index) => {
        const cellElement = document.createElement('div');
        cellElement.classList.add('cell');
        cellElement.textContent = cell;
        cellElement.addEventListener('click', () => makeMove(index));
        boardElement.appendChild(cellElement);
    });
}
