package Java_tutorial.encapsulamento;

public class bigNum {
    /* Apenas uma classe pública pode existir por projeto */
    public static void main (String[] args) {
        System.out.println(Fatorial.fat(5));
    }
}

class Fatorial {
    /* O método é público: pode ser acessado por outras classes
       O método é estático: pode ser acessado sem instanciar um objeto  */

    public static int fat(int num) {
        if (num == 0) return 1;
        else return fat(num - 1)*num;
    }
}