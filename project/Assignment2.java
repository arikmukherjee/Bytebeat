//WAP to calculate the area of different shapes.

//Here we are using runtime polymorphism.


import java.lang.Math;          

abstract class Shapes{          // abstract class = jei class er obj banano jaye na.
    abstract double area();
}

class Triangle extends Shapes{
    int side1;
    int side2;
    int side3;
   
    Triangle(int side1, int side2, int side3){
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }
    
    @Override
    double area(){
        double s = (side1+side2+side3)/2;
        double a = Math.sqrt(s*((s-side1)*(s-side2)*(s-side3)));
        return a;
    }
}

class Square extends Shapes{
    int side1;
    int side2;

    Square(int side1, int side2){
        this.side1 = side1;
        this.side2 = side2;
    }
    
    @Override
    double area(){
        double a = side1*side2;
        return a;
    }
}

class Rectangle extends Shapes{
    int length;
    int bredth;
    
    Rectangle(int length, int bredth){
        this.length = length;
        this.bredth = bredth;
    }
    
    @Override
    double area(){
        double a = length*bredth;
        return a;
    }
}

class Circle extends Shapes{
    int radius;
    Circle(int radius){
        this.radius = radius;
    }
    
    @Override
    double area(){
        double a = Math.PI * radius*radius;
        return a;
    }
}
public class Assignment2{
    public static void main(String [] args){
        Triangle t = new Triangle(5,5,5);
        System.out.println(t.area());
        
        Square s = new Square(4,4);
        System.out.println(s.area());
        
        Rectangle r = new Rectangle(6,3);
        System.out.println(r.area());
        
        Circle c = new Circle(6);
        System.out.println(c.area());
    }
}