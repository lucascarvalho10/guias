// Podemos/devemos tipar as funções com o seu retorno especificado
const soma = (num1: number, num2: number): number => {
  return num1 + num2;
};

console.log(soma(2, 3));

const imprimeNome = (nome: string): string => {
  return `Me chamo ${nome}`;
};

console.log(imprimeNome("Lucas"));

type pessoa = {
  nome: string;
  idade: number;
};

const geraPessoa = (nome: string, idade: number): pessoa => {
  return { nome, idade };
};

const imprimePessoa = (minhaPessoa: pessoa): void => {
  console.log(`Me chamo ${minhaPessoa.nome} e tenho ${minhaPessoa.idade} anos`);
};

const Lucas: pessoa = geraPessoa("Lucas", 19);
imprimePessoa(Lucas);

const { nome, idade } = Lucas;
console.log(nome, idade);
