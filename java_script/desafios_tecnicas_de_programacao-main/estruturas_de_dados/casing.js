String.prototype.toJadenCase = function () {
    let returnString = [];
    let words = this.toLowerCase().split(' ');
    
    for (let i = 0; i < words.length; i++) {
        word = words[i];
        returnString.push(word[0].toUpperCase() + word.slice(1));
    }
    return returnString.join(" ");
  };