package Java_tutorial.heranca;
public class acesso {
    //Podemos utilizar outras keywords para restrição de acesso:

    /*
        Public: acesso global
        Private: apenas na classe
        Protected: não é global, mas o memso package e filhos têm acesso
        no modifier: apenas a classe e o package
    */

    protected String nome;
    protected String regiao;

    public acesso(String nome, String regiao) {
        this.nome = nome;
        this.regiao = regiao;
    }

    //A keyword final diz que as classes filhas não podem modificar esse método
    final public static void fala() {
        System.out.println("OI");
    }

}