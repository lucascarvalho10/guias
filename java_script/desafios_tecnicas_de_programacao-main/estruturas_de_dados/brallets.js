class Pilha {
    constructor() {
        this.elemento = [];
        this.total = 0;
    }

    empilha(elemento) {
        this.elemento.push(elemento);
        this.total++;
    }

    desempilha() {
        let retorno = this.elemento[this.total - 1];
        this.elemento.pop();
        this.total--;
        return retorno;
    }
}

function validBraces(braces){
    //Utilizaremos uma estrutura de pilha: LIFO

    let nTemp, rFinal = true;
    let temp = braces.toString().split("");

    let pilha = new Pilha();

    temp.map(element => {
        if (element === '(' || element === '{' || element === '[') pilha.empilha(element);
        else {
            nTemp = pilha.desempilha();
            if ((nTemp === '(' && element !== ')') || (nTemp === '[' && element !== ']') || (nTemp === '{' && element !== '}')) rFinal = false;
        }
    });

    if (pilha.total != 0) rFinal = false;

    return rFinal;
}

console.log(validBraces("({[[[]]]})(){}[]{}(({}))]"));