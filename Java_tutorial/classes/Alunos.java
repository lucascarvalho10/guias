package Java_tutorial.classes;

public class Alunos {
    private String nome;
    private char classe;
    private int idade;

    public Alunos(String nome, char classe, int idade) {
        this.nome = nome;
        this.classe = classe;
        this.idade = idade;
    }

    public void get() {
        System.out.println("Meu nome e " + this.nome + " sou da classe " + this.classe + " e tenho " + this.idade);
    }

    public static void main (String[] args) {
        Alunos Lucas = new Alunos ("Lucas", 'A', 19);
        Lucas.get();
    }
}
