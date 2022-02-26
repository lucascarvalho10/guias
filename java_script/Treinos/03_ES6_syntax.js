/* ============ ES6: Classes  ============== */

//Class expression
// const PersonCl = class {}

class PersonCl {
    constructor(firstName, birthYear) {
        this.fullName = firstName;
        this.birthYear = birthYear;
    }

    calcAge() {
        console.log(2021 - this.birthYear);
    }

    static otherAge(age) {
        return 2022 - age;
    }

    get age() {
        return 2022 - this.birthYear;
    }

    set fullName(name) {
        if(name.includes(' ')) this._fullName = name;
        else console.log('Erro');
    }
}

//Tente mudar aqui para um nome completo
const Ann = new PersonCl ('Ann', 2001);
console.log(Ann);

Ann.calcAge();

/*   
    ==== Observação ====
    Classes are not hoisted
    Cidadãos de primeira classes: passados como parâmetros e retornáveis
    Executed in strict mode
*/


/* ================ Get and Set =============== */

//Propriedades de acessos

const account = {
    owner: 'Lucas',
    movements: [200, 530, 120, 300],

    get latest() {
        return this.movements.slice(-1).pop();
    },

    set latest(mov) {
        this.movements.push(mov);
    }
};

console.log(account.latest);
account.latest = 50;
console.log(account.latest);


//Método estático
console.log(PersonCl.otherAge(2000));


//Object.create

const PersonPhoto = {
    calcAge() {
        console.log(2022 - this.birthday);
    }
};

const Lucas = Object.create(PersonPhoto);

console.log(Lucas);


/* ========== Segundo Desafio ========== */

class Car {
    constructor(carName, carSpeed) {
        this._mark = carName;
        this._speed = carSpeed;
    }

    get SpeedUS() {
        return (this._speed)/1.6;
    }

    //Sempre apenas um argumento
    set SpeedUS(speed) {
        this._speed = speed*1.6;
    }
}

const Ford = new Car ('Ford', 120);
console.log(Ford);
console.log(Ford.SpeedUS);
Ford.SpeedUS = 50;
console.log(Ford.SpeedUS);