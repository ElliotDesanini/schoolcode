
const maxColors = 100;

let backgroundColors = [];

for (let colorAmount = 0; colorAmount != maxColors; colorAmount++) {
    function rgbRandom(...args) {
        if (args.length === 1) {
            return `rgb(${Math.floor(Math.random() * args[0])}, ${Math.floor(Math.random() * args[0])}, ${Math.floor(Math.random() * args[0])})`;
        }

        else if (args.length === 3) {
            return `rgb(${Math.floor(Math.random() * args[0])}, ${Math.floor(Math.random() * args[1])}, ${Math.floor(Math.random() * args[2])})`;
 
        }

        else {
            throw new Error("there must be exactly 1 or 3 arguments.");
        }
    }

    let newColor = rgbRandom(60)
    backgroundColors.push(newColor);
};

console.log(backgroundColors)


document.getElementById('logo').onclick = function () {
    document.getElementById('logo').classList.toggle('big_logo');
    document.getElementById('container').style.backgroundColor = backgroundColors[Math.floor(Math.random() * backgroundColors.length)];
};