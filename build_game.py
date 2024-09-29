import os

# Directory where the project will be created
project_dir = 'memory-game'

# Project files content
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memory Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Jeu de Mémoire</h1>
    <p>Score: <span id="score">0</span></p>
    <p>Temps restant: <span id="time">60</span> secondes</p>
    <div class="game-board" id="game-board"></div>
    <script src="script.js"></script>
</body>
</html>
'''

css_content = '''body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f2f2f2;
}

h1 {
    color: #4CAF50;
}

p {
    font-size: 20px;
}

.game-board {
    display: grid;
    grid-template-columns: repeat(4, 100px);
    grid-gap: 10px;
    justify-content: center;
    margin-top: 20px;
}

.card {
    width: 100px;
    height: 100px;
    background-color: #f1f1f1;
    border: 2px solid #4CAF50;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 50px;
    color: white;
}

.card img {
    display: none;
}

.card.flipped img {
    display: block;
}

.card.flipped {
    background-color: white;
}
'''

js_content = '''const cardsArray = [
    { name: 'cheetah', img: 'https://cdn.pixabay.com/photo/2015/11/17/14/36/cheetah-1045990_960_720.jpg' },
    { name: 'cheetah', img: 'https://cdn.pixabay.com/photo/2015/11/17/14/36/cheetah-1045990_960_720.jpg' },
    { name: 'lion', img: 'https://cdn.pixabay.com/photo/2013/05/29/15/00/lion-114130_960_720.jpg' },
    { name: 'lion', img: 'https://cdn.pixabay.com/photo/2013/05/29/15/00/lion-114130_960_720.jpg' },
    { name: 'elephant', img: 'https://cdn.pixabay.com/photo/2017/08/01/08/29/elephant-2567437_960_720.jpg' },
    { name: 'elephant', img: 'https://cdn.pixabay.com/photo/2017/08/01/08/29/elephant-2567437_960_720.jpg' },
    { name: 'giraffe', img: 'https://cdn.pixabay.com/photo/2017/02/10/19/00/giraffe-2053516_960_720.jpg' },
    { name: 'giraffe', img: 'https://cdn.pixabay.com/photo/2017/02/10/19/00/giraffe-2053516_960_720.jpg' }
];

let gameBoard = document.getElementById('game-board');
let scoreElement = document.getElementById('score');
let timeElement = document.getElementById('time');
let score = 0;
let flippedCards = [];
let matchedCards = [];
let timeRemaining = 60;
let timer;

function shuffle(array) {
    array.sort(() => 0.5 - Math.random());
}

function createBoard() {
    shuffle(cardsArray);
    cardsArray.forEach((card, index) => {
        let cardElement = document.createElement('div');
        cardElement.classList.add('card');
        cardElement.dataset.name = card.name;
        cardElement.innerHTML = `<img src="${card.img}" alt="${card.name}">`;
        cardElement.addEventListener('click', flipCard);
        gameBoard.appendChild(cardElement);
    });
}

function flipCard() {
    if (flippedCards.length < 2 && !this.classList.contains('flipped')) {
        this.classList.add('flipped');
        flippedCards.push(this);

        if (flippedCards.length === 2) {
            checkForMatch();
        }
    }
}

function checkForMatch() {
    let [card1, card2] = flippedCards;
    if (card1.dataset.name === card2.dataset.name) {
        matchedCards.push(card1, card2);
        score += 10;
        scoreElement.textContent = score;
        flippedCards = [];
        if (matchedCards.length === cardsArray.length) {
            clearInterval(timer);
            alert('Congratulations! You have matched all the cards.');
        }
    } else {
        setTimeout(() => {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
            flippedCards = [];
        }, 1000);
    }
}

function startTimer() {
    timer = setInterval(() => {
        timeRemaining--;
        timeElement.textContent = timeRemaining;
        if (timeRemaining === 0) {
            clearInterval(timer);
            alert('Time is up! Game over.');
        }
    }, 1000);
}

window.onload = () => {
    createBoard();
    startTimer();
};
'''

package_json_content = '''{
  "name": "memory-game",
  "version": "1.0.0",
  "description": "A simple memory game built with HTML, CSS, and JavaScript",
  "main": "index.html",
  "scripts": {
    "start": "live-server --port=8080"
  },
  "keywords": [
    "memory",
    "game",
    "html",
    "css",
    "javascript"
  ],
  "author": "Your Name",
  "license": "MIT",
  "devDependencies": {
    "live-server": "^1.2.1"
  }
}
'''

# Function to create files
def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Create project directory if it doesn't exist
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Change working directory to project directory
os.chdir(project_dir)

# Create the necessary files
create_file('index.html', html_content)
create_file('styles.css', css_content)
create_file('script.js', js_content)
create_file('package.json', package_json_content)

print("Files created successfully!")
