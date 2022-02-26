function comp(array1, array2){
    //var quantidadeElementos = teste.filter(x => x === "oi").length;
    if (array1 === null || array2 === null) return false;
    let temp = true;
    array1.map(element => {
       if (array2.filter(x => x === element**2).length != array1.filter(x => x === element).length) temp = false;
    })
    
    return temp;
}

console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))