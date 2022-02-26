const enumerarLetras = (palavra) => {
    palavra = palavra.toLowerCase();
    let numeros = [];
    palavra.split('').map(function(letra){
        numeros.push((letra.charCodeAt(0) - 97) + 1);
    });
    let soma = 0;
    
    numeros.map(elemento => {
        soma += elemento;
    });
    return soma;
}

// var myArray = [1, 5, 6, 2, 3];
// var m = Math.max(...myArray);
// console.log(m)

function high(x){
    let max, nTemp;
    let temp = [];
    x.map(palavra => {
        temp.push(enumerarLetras(palavra));
    })
    max = Math.max(...temp);
    nTemp = temp.indexOf(max);

    return x[nTemp];
}


console.log(high(["abc", "aaa", "bxb", "x"]));