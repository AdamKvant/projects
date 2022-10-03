// Written by Adam Kvant, kvant003; and Aidan Kadid, kadid010
import java.awt.*;
import java.lang.Math;
public class Circle {
    private double x;
    private double y;
    private double radius;
    private Color color;
    // Constructor Method that creates new Circle object
    public Circle(double x, double y, double radius){
        this.x = x;
        this.y = y;
        this.radius = radius;
    }
    // Function method that calculates the perimeter of a Circle object.
    public double calculatePerimeter() {
        double circlePerimeter = 2 * Math.PI * this.radius;
        return circlePerimeter;
    }
    // function method that calculates the area of the Circle object
    public double calculateArea(){
        double circleArea = 2 * Math.PI * this.radius * this.radius;
        return circleArea;
    }
    // setter method that sets the fill color of the circle
    public void setColor(Color color) {
        this.color = color;
    }
    // Setter method that sets the x and y position of the center of the circle
    public void setPos(double xPos, double yPos){
        this.x = xPos;
        this.y = yPos;

    }
    // setter method that sets the radius of the circle
    public  void setRadius(double radius) {
        this.radius = radius;
    }
    // getter method that returns the color of the circle
    public Color getColor() {
        return this.color;
    }
    // getter method that returns the x-position of the center of the circle.
    public double getXPos(){
        return this.x;
    }
    // getter method that gets the y-position of the center of the circle
    public double getYPos() {
        return this.y;
    }
    //getter method that gets the radius of the circle
    public double getRadius(){
        return this.radius;
    }
}
