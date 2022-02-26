/* ========== Encapsulation and Privacy ========== */

/* Class fields: um pouco de private de verdade
    1) Public fields
    2) Private fields
    3) Public methods
    4) Private methods
*/

class Account {
    //1) Public fields (instances)
    locale = 'Brazil, SP';

    //2) Private fields
    #movements = [];
    #pin;

    constructor (owner, currency, pin) {
        this.owner = owner;
        this.currency = currency;
        //Protected property
        this.#pin = pin;
        // this._movements = [];
        // this.locale = 'Brazil, SP';

        console.log(`Thanks for opening an account, ${this.owner}`);
    }

    //3) Public methods: aquilo já fizemos
    getMovements() {
        return this.#movements;
    }

    deposit(val) {
        this.#movements.push(val);
        return this;
    }

    withdraw(val) {
        this.#movements.push(-val);
        return this;
    }

    requestLoan(val) {
        if (this.#approveLoan(val)) {
            this.deposit(val);
            console.log(`Loan approved`);

            return this;
        }
    }

    //4) Private methods

    #approveLoan(val) {
        return true;
    }
}

const acc1 = new Account ('Lucas', 'BRL', 1234);
console.log(acc1);

//Como encadear um monte de coisas - simultaneidade
acc1.deposit(300).deposit(500).withdraw(100).requestLoan(1000);

console.log(`The movements are: ${acc1.getMovements()}`);
