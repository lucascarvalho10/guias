function persistence(num) {
    if (num/10 < 1) return 0;

    let mult = 1, total = 0;
    let valor = new Array();

    do {
        valor = num.toString().split("");
        valor.map(num => {
            mult *= parseInt(num);
        })
      
        num = mult;
        mult = 1;
        total++;
    } while (num >= 10);

    return total;
}

console.log(persistence(128));