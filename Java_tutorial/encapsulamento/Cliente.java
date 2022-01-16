package Java_tutorial.encapsulamento;

public class Cliente {
    private String nome;
    private double saldo;
    private int numConta;

    public Cliente(String nome) {
        this.nome = nome;
        this.saldo = 0;
        this.numConta = (int)(Math.random()*1001) + 1;
    }

    public void deposito(double grana) {
        this.saldo += grana;
    }

    public void saque(double grana) {
        this.saldo -= grana;
    }

    public void impressao() {
        System.out.println("Ola, " + this.nome + " o seu saldo é: " + this.saldo);
    }

    public boolean compSaldo(double valor) {
        return this.saldo > valor;
    }

    public boolean comNome(String noom) {
        return this.nome.equals(nome);
    }

    public static void main(String[] args) {
        
    }
    
}
