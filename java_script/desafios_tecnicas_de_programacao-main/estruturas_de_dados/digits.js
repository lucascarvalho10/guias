function digPow(n, p){
    let temp = n.toString().split('');
    let soma = 0;

    temp.map(element => {
        element = Math.pow(element, p);
        p++;

        soma += element;
    })

    return (soma%n === 0) ? soma/n : -1; 
 }