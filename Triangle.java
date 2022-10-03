// Written by Adam Kvant, kvant003; and Aidan Kadid, kadid010
import java.awt.*;
import java.lang.Math;
public class Triangle {
    private double xPos;
    private double yPos;
    private double width;
    private double height;
    private Color color;
    // Constructor that creates a new Triangle object
    public Triangle(double xPos, double yPos, double width, double height) {
        this.xPos = xPos;
        this.yPos = yPos;
        this.width = width;
        this.height = height;
    }
    // Function method that calculates the perimeter of the triangle object.
    public double calculatePerimeter(){
        double trianglePerimeter = this.width + Math.sqrt(Math.pow(this.width, 2) + (4* Math.pow(this.height,2)));
        return trianglePerimeter;
    }
    // function method that calculates the area of the triangle
    public double calculateArea() {
        double triangleArea = .5 * this.width * this.height;
        return triangleArea;
    }
    // Setter method that sets the fill color of the triangle.
    public void setColor(Color color) {
        this.color =  color;
    }
    //setter method that sets the position of the bottom left corner of the triangle object
    public void setPos(double xPos, double yPos) {
        this.xPos = xPos;
        this.yPos = yPos;
    }
    // Setter method that gets the height of the triangle
    public void setHeight(double height) {
        this.height = height;
    }
    // Setter method that gets the width of the triangle
    public void setWidth(double width) {
        this.width = width;
    }
    //  getter method that gets the fill color of the triangle object
    public Color getColor() {
        return this.color;
    }
    // getter method that gets the x-position of the bottom left corner of the triangle
    public double getXPos(){
        return this.xPos;
    }
    // getter method that gets the y-position of the bottom left corner of the triangle
    public double getYPos() {
        return this.yPos;
    }
    // getter method that returns the height of the triangle object
    public double getHeight(){
        return this.height;
    }
    // Getter method that returns the width of the triangle object
    public double getWidth() {
        return this.width;
    }

}
