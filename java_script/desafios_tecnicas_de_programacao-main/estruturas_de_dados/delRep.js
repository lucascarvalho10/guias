function deleteNth(arr,n){
    // numeros.splice(numeros.indexOf(3), 1);
    let qtd;
    arr.map(element => {
        qtd = arr.filter(x => x === element).length;  
        if (qtd > n) 
            arr.splice(arr.indexOf(element, n), qtd - n); 
    });

    return arr;
}

console.log(deleteNth([20,37,20,21],1));