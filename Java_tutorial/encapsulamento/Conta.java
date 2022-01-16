package Java_tutorial.encapsulamento;

public class Conta {
    public static void main (String[] args) {
        Criacao minhaConta = new Criacao("Lucas", 123, 100000.00);
        minhaConta.getInfo();
        minhaConta.setSaldo(500);

        minhaConta.setSenha(123, 456);

        minhaConta.resetarConta();
    }
}

class Criacao {
    private String nome;
    private int senha;
    private double saldo;

    public Criacao (String nome, int senha, double saldo) {
        this.nome = nome;
        this.senha = senha;
        this.saldo = saldo;
    }

    public void getInfo() {
        System.out.println(this.nome + ", seu saldo é de: " + this.saldo);
    }

    public void setSaldo(double soma) {
        this.saldo += soma;
        System.out.println(this.nome + ", seu novo saldo é de: " + this.saldo);
    }

    public void setSenha(int antigaSenha, int novaSenha) {
        if (this.senha != antigaSenha) System.out.println("Senha incorreta! ");
        else { 
            this.senha = novaSenha;
            System.out.println("Senha alterado com sucesso! ");
        }
    }

    public void resetarConta() {
        this.saldo = 0;
        this.senha = 123;
        System.out.println(this.nome + " sua conta foi resetada com sucesso");
    }
}