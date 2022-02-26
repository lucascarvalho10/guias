const thousands = {
    "M": 1,
    "MM": 2,
    "MMM": 3
}

const hundreds = {
    "C": 1,
    "CC": 2,
    "CCC": 3,
    "CD": 4,
    "D": 5,
    "DC": 6,
    "DCC": 7,
    "DCCC": 8,
    "CM": 9
}

const tens = {
    "X": 1, 
    "XX": 2,
    "XXX": 3,
    "XL": 4,
    "L": 5,
    "LX": 6,
    "LXX": 7,
    "LXXX": 8,
    "XC": 9
}

const units = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9
}

function achar (num, estrutura) {
    //for in para varrer um objeto
    for (const valor in estrutura) {
        if (estrutura[valor] === num)
            return valor;
    }
}

function solution(number){
  // convert the number to a roman numeral
  let a;
  let temp = new Array();
  for (let i = 3; i >= 0; i--) {
      a = Math.floor(number/10**i);
      number -= a*(10**i);
      if (a != 0) {
          if (i === 3) a = achar(a, thousands);
          if (i === 2) a = achar(a, hundreds);
          if (i === 1) a = achar(a, tens);
          if (i === 0) a = achar(a, units);
          temp.push(a);
          
      }
  }
  
  return temp.join("");
}

console.log(solution(3123));