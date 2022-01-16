package Java_tutorial.encapsulamento;
//Algumas classes internas do Java possuem métodos estáticos interessantes, como o Math

public class aleatorios {

    public static void impressao() {
        for (int i = 0; i < 20; i++) {

            //Aleatórios entre 0 e 100
            System.out.println((int)(Math.random()*100) + 1);
        }
    }
    public static void main (String[] args) {
        impressao();
    }
}
