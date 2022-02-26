function accum(s) {
    let temp = s.slice("");
      let nTemp = [];
  
      for (let i = 0; i < temp.length; i++) {
          for (let j = 0; j <= i; j++) {
              (j === 0) ? nTemp.push(temp[i].toUpperCase()) : nTemp.push(temp[i].toLowerCase());
          }
  
          if (i !== temp.length - 1) nTemp.push("-");
      }
  
      s = nTemp.join("");
  
      return s;
  }