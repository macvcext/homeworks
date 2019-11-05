## Solution for the Third Homework

Class, I have coded our homework and implemented Fisher-Yates algorithm for the random colors. You may refresh the page to generate a new set.

```javascript
function setup() {
    const colors = [
        () => fill(255, 119, 126), // Shorthand function return
        () => fill(195, 34, 98),
        () => fill(18, 174, 253),
        () => fill(66, 103, 178),
        () => fill(255, 241, 145),
        () => fill(58, 135, 174),
        () => fill(239, 165, 42),
        () => fill(242, 232, 207),
        () => fill(30, 176, 137),
        () => fill(4, 73, 168),
        () => fill(253, 194, 5),
        () => fill(239, 154, 154),
    ];
    createCanvas(500, 500);
    background(200);
    translate(width / 2, height / 2);
    for (let i = 0; i < 10; i++) {
        shuffle(colors)[0](); // Using Fisher-Yates and calling the function
        ellipse(0, 30, 20, 80);
        rotate(PI / 5);
    }
    ellipse(0, 0, 30, 30);

}

// Fisher-Yates Algorithm
function shuffle(array) {
    var currentIndex = array.length,
        temporaryValue, randomIndex;

    while (0 !== currentIndex) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}
```

