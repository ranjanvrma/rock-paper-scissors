# 🎮 Rock Paper Scissors – Python Game

A **Python** console application that lets you play the classic **Rock Paper Scissors** game against the computer.  
This project demonstrates core programming concepts like **loops**, **conditionals**, **user input handling**, and **randomization**.  
In future, this will be upgraded into a full **web app** using Flask, HTML, CSS, and JavaScript.

---

## 🚀 Features

- **Interactive CLI Gameplay:** Play directly in the terminal.
- **Random Computer Moves:** The computer randomly chooses between `rock`, `paper`, and `scissors`.
- **Input Validation:** Handles invalid inputs gracefully and asks the user to try again.
- **Replay Support:** Option to play multiple rounds without restarting the program.
- **Exit Anytime:** Type `exit` to quit the game gracefully.
- **Modular Code Structure:** Game logic is separated into reusable functions for easy extension.

---

## 🧠 Game Logic

The game follows standard Rock Paper Scissors rules:

- **rock** beats **scissors**
- **paper** beats **rock**
- **scissors** beats **paper**

Outcome conditions:
- Same choices → **Draw**
- Computer’s choice beats yours → **You lose** (`"Better Luck Next Time!"`)
- Your choice beats computer’s → **You win** (`"You Won!"`)

---

## 🛠️ Installation & Usage

1️⃣ **Clone the Repository**

```
git clone <your-github-repo-url>
cd rock-paper-scissors
```

2️⃣ **Run the Game**

```
python app.py
```
Make sure you have Python 3 installed on your system.

---

## 🧮 Game Flow

When you run the program, it:
1. Greets you and shows instructions.
2. Asks for your move: rock, paper, scissors, or exit.
3. Validates your input:
   - If invalid → shows an error and asks again.
   - If exit → thanks you and quits.
4. Randomly selects the computer’s move.
5. Displays:
  - Computer’s choice
  - Result: Draw, You Win, or You Lose
6. Asks:
  Want to Play Again? (yes / no):
    - yes → new round
    - no → exits with a goodbye message

---

## 🧭 Example Run

```
Rock Paper Scissors Game
Type Your Choice: Rock / Paper / Scissors
Type Exit to Terminate the Game

Your Move: rock
Computer Chose: scissors
You Won!
Want to Play Again? (yes / no): yes

Your Move: paper
Computer Chose: scissors
Better Luck Next Time!
Want to Play Again? (yes / no): no
Thanks for Playing!
```

---

## 🧠 How It Works
- Randomization: Uses random.choice() from Python’s standard library to select computer moves.
- Looping: A while True loop runs the game until the user exits.
- Input Handling: Uses .lower() to make user input case-insensitive.
- Game Outcome: A set of if/elif/else conditions compares user and computer choices to decide the result.

---

## 🧱 File Structure

```
rock-paper-scissors/
|
├── app.py        # Main Python script containing the game logic
└── README.md     # Project documentation
```
(Additional files like templates/, static/, and requirements.txt will be added later when converting to a web app.)

---

## 🧑‍💻 Tech Stack

- Language: Python 3
- Libraries: Python Standard Library (random)

---

## 💡 Future Enhancements

- Reuse existing game logic to build a web API backend.
- Add a basic **Flask backend** to run the game logic on a server.
- Create a simple **web interface** using HTML, CSS, and JavaScript.
- Connect the web UI to the backend using API requests.
- Add a **score tracker** for wins, losses, and draws.
- Improve input validation and error messages.
- Add simple UI effects and animations for button clicks.
- Add light/dark theme toggle for the web interface.

---

## 👨‍💻 Author

Ranjan Verma | ranjanverma2310@gmail.com | [Github Profile](https://github.com/ranjanvrma)
