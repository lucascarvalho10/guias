//Relação de Stifel

const pascal = (power) => {
    let line = new Array();
    let i, j;
    for (i = 0; i < power; i++) {
        line[i] = new Array();
        for (j = 0; j <= i; j++) {
            if (j === 0 || j === i)  line[i][j] = 1;
            else  line[i][j] = line[i - 1][j] + line[i - 1][j - 1];
        }
    }
    
    for (i = 0; i < power; i++) 
            console.log(line[i]);
}

pascal(5);