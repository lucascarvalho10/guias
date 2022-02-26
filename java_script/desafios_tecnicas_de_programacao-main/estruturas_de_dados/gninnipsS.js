function spinWords(string){
    //Criando uma variável auxiliar que recebe um vetor com cada palavra de strings
    
    let temp = string.split(" ");
    
    //Verifica-se se a apalavra possuia mais do que cinco letras e, caso sim, é invertida
    for (let i = 0; i < temp.length; i++)
      //A lógica é a seguinte: quebramos a palavra em letras, invertemos e juntamos
      if (temp[i].length >= 5) temp[i] = temp[i].split("").reverse().join("");
    
    string = temp.join(" ");
    
    return string;
  }