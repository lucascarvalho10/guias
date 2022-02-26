/* ========== Inheritance in ES6 ========== */

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

class StudentCl extends PersonCl {
    constructor(fullName, birthYear, course) {
        //Sempre precisa para acontecer antes - super
        super(fullName, birthYear);
        this.course = course;
    }

    introduce() {
        console.log(`My name is ${this.fullName} and I study ${this.course}`);
    }
}

const Ann = new StudentCl('Ann Taylor', 2001, 'Design');
Ann.introduce();