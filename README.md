# Flask Tic-Tac-Toe

A simple Tic-Tac-Toe game built using Flask, where a player can play against a computer using the Minimax algorithm for AI decision-making.

## Features
- Play Tic-Tac-Toe against a computer AI.
- AI uses the Minimax algorithm for optimal decision-making.
- Web-based UI using Flask and JavaScript.
- Simple and interactive game logic.

## Installation
### Prerequisites
- Python 3.x installed on your system.
- Flask library installed.

### Steps to Run
1. Clone the repository or download the project files.
   ```sh
   git clone https://github.com/your-repo/flask-tic-tac-toe.git
   cd flask-tic-tac-toe
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install flask
   ```
5. Run the application:
   ```sh
   python app.py
   ```
6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
### 1. Home Page
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Loads the game UI.

### 2. Make a Move
- **Endpoint:** `/move`
- **Method:** `POST`
- **Description:** Processes the player's move and allows the AI to respond.
- **Request Body (JSON):**
  ```json
  {
    "board": ["", "", "", "", "", "", "", "", ""],
    "player": "X",
    "move": 4,
    "mode": "computer"
  }
  ```
- **Response (JSON):**
  ```json
  {
    "board": ["", "", "", "", "X", "", "", "O", ""],
    "winner": null
  }
  ```

## Game Logic
- The game board is represented as a 9-element list.
- The AI uses the Minimax algorithm to find the optimal move.
- The game checks for a winner after every move.
- If the board is full, the game ends in a draw.

## Future Improvements
- Improve UI with CSS and JavaScript animations.
- Add multiplayer mode.
- Implement different difficulty levels for AI.

## License
This project is open-source and available under the MIT License.

## Author
Developed by Subham Mondal.

