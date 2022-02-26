function duplicateEncode(word){
    let temp = word.slice("");
    let temp2 = [];
    let cont = 0;

    for (let i = 0; i < temp.length; i++) {
    
        for (let j = 0; j < temp.length; j++) 
            if (temp[i].toUpperCase() === temp[j].toUpperCase()) cont++;

        (cont === 1) ? temp2.push("(") : temp2.push(")");
        cont = 0;
    }

    word = temp2.join("");
   
    return word;
}