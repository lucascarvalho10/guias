/* ==================== Notação padrão ========================= */

const Person = function(firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
}

Person.prototype.calcAge = function() {
    //Ainda precisamos da keyword 'this' para referenciar o objeto que a chama
    console.log(2022 - this.birthYear);
}

//Student "herda" propriedades e métodos de Person

const Student = function (firstName, birthYear, course) {
    Person.call(this, firstName, birthYear);
    //A keyword call permite essa interface
    this.course = course;
}

//Herança do protóttipo
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

const Lucas = new Student ('Lucas', 2001, 'Electrical Engineering');
console.log(Lucas);
Lucas.calcAge();

console.log(Lucas.__proto__);


/* ====== Desafio 03: Carro Elétrico ====== */

const Car = function(carName, carSpeed) {
    this.name = carName;
    this.speed = carSpeed;
}

Car.prototype.accelerate = function(a) {
    this.speed += a;
    console.log(this.speed);
}

const ElectricCar = function (carName, carSpeed, battery) {
    Car.call(this, carName, carSpeed);
    this.battery = battery;
}

ElectricCar.prototype = Object.create(Car.prototype);

ElectricCar.prototype.accelerate = function() {
    this.speed += 20;
    this.battery -= 1;
}

const Tesla = new ElectricCar ('Tesla', 120, 90);
Tesla.accelerate();

console.log(Tesla);

/* ================== ES6 Syntax  =====================*/

