// numbers = [x for x in range(1, 9)]
// letters = [chr(i) for i in range(ord('a'), ord('h')+1)]

// return {(letter + str(number)): (number-1, ord(letter) - ord('a'))
//         for number in numbers for letter in letters}

const create_coordinates = () => {
    const numbers = Array.from({ length: 8 }, (_, i) => i);
    const letters = Array.from({ length: 8 }, (_, i) => String.fromCharCode('A'.charCodeAt(0) + i));
    const coords = {};

    for (const number of numbers) {
        for (const letter of letters) {
            const squareName = letter + (parseInt(number)+1).toString();
            coords[squareName] = [number, letter.charCodeAt(0) - 'A'.charCodeAt(0)];
        }
    }

    return coords;
};

const retrieve_coordinate = (square) => {
    return create_coordinates()[square.toUpperCase()]
}