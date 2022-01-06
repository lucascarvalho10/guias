public class Stores {
  // instance fields
  String productType;
  double price;
  
  // constructor method
  public Stores(String product, double initialPrice) {
    productType = product;
    price = initialPrice;
  }
  
  // increase price method
  public void increasePrice(double priceToAdd){
    price += priceToAdd;
  }
  
  // get price with tax method
  public double getPriceWithTax(){
    double tax = 0.08;
    double totalPrice = price + price*tax;
    return totalPrice;
  }
  
  public String toString(){
    return "This stores sells " + productType + " at a price of " + price + ".";
  }

  // main method
  public static void main(String[] args) {
    Stores lemonadeStand = new Stores("Lemonade", 3.75);
    Stores cookieShop = new Stores("Cookies", 5);

    System.out.println(lemonadeStand);
    System.out.println(cookieShop);
  }
}