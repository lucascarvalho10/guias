/* =================== Prototypes =====================  

Protótipos se referem diretamente aos objetos 
*/
const d = new Date();
let currentYear = d.getFullYear();


const Person = function(firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
}

//Utilizamos um protótipo para declarar métodos
Person.prototype.calcAge = function() {
    //Ainda precisamos da keyword 'this' para referenciar o objeto que a chama
    console.log(currentYear - this.birthYear);
}

Person.prototype.species = 'Homo Sapiens';

const Lucas = new Person('Lucas', 2001);
Lucas.calcAge();

console.log(Lucas.__proto__);

/* ============ Build in objects ============= */
console.dir(Person.prototype.constructor);

const arr = [3, 4, 6, 6, 10, 2, 15, 20, 10, 4];
console.log(arr.__proto__ === Array.prototype);

//Adicionando novos métodos aos protótipos
Array.prototype.unique = function () {
    return [...new Set(this)];
}

console.log(arr.unique());



/* ========== Desafio ==========  */

const Car = function(carName, carSpeed) {
    this.name = carName;
    this.speed = carSpeed;
}

Car.prototype.accelerate = function(a) {
    this.speed += a;
    console.log(this.speed);
}

const CAR1 = new Car ('BMW', 120);
const CAR2 = new Car ('Mercedes', 95);