'use strict';

/* =============    Noções intuitivas ======================== */

//Não podemos utilizar funções lambda -> não há acesso à keyword this
const Person = function(firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
}

const Lucas = new Person('Lucas', 2001);
const Alex = new Person('Alex', 2010);
console.log(Lucas, Alex);

// Lucas é instância de Person, em sentido aberto
console.log(Lucas instanceof Person);

/* =============== O que está rolando ============ 

   1. New () é criado
   2. a função é chamada, this = {}
   3. {} ligado ao protóptipo (prototype)
   4. A função automaticamente retorna {}

   Obs: nunca declare métodos no construtor. Isso
   vai ser terrível para a performance do programa.
*/