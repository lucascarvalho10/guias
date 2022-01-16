package Java_tutorial.classes;

public class Store {
    // instance fields
    String productType;
    int inventoryCount;
    double inventoryPrice;
    
    // constructor method
    public Store(String product, int count, double price) {
      productType = product;
      inventoryPrice = price;
      inventoryCount = count;
    }
    
    // main method
    public static void main(String[] args) {
        Store cookieShop = new Store("cookies", 12, 3.75);
  
        System.out.println(cookieShop.productType);
    }
  }