package Java_tutorial.heranca;

public class heranca {

    public String nome;
    public int idade;


    public heranca(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public static void main (String[] args) {
        herdar eu = new herdar();
        System.out.println(eu.nome);
    }

}


//A keyword extends permite herdar valores de uma superclass
class herdar extends heranca {

    public herdar (){
        super("Lucas", 19);
    }
}