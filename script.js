const cardsArray = [
    { name: 'cheetah', img: './images/cheetah.jpeg' },
    { name: 'cheetah', img: './images/cheetah.jpeg' },
    { name: 'lion', img: './images/lion.jpg' },
    { name: 'lion', img: './images/lion.jpg' },
    { name: 'elephant', img: './images/elephant.jpg' },
    { name: 'elephant', img: './images/elephant.jpg' },
    { name: 'giraffe', img: './images/giraffe.jpeg' },
    { name: 'giraffe', img: './images/giraffe.jpeg' }
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
