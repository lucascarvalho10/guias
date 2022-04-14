type pessoas = {
  nome: string;
  idade: Number;
};

type aluno = {
  nome: string;
  idade: Number;
  turma: string;
};

class Pessoa<pessoas> {
  nome: string;
  idade: Number;
  constructor(nome: string, idade: Number) {
    this.nome = nome;
    this.idade = idade;
  }

  getPessoa = () => {
    console.log(`Me chamo ${this.nome} e tenhi ${this.idade} anos`);
  };

  setPessoa = (nome: string, idade: Number) => {
    this.nome = nome;
    this.idade = idade;
  };
}

class Aluno extends Pessoa<aluno> {
  turma: string;
  constructor(nome: string, idade: Number, turma: string) {
    super(nome, idade);
    this.turma = turma;
  }
}
