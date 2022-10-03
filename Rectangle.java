// Written by Adam Kvant, kvant003; and Aidan Kadid, kadid010
import javax.swing.plaf.ColorUIResource;
import java.awt.*;


public class Rectangle {
    private double xPos;
    private double yPos;
    private double width;
    private double height;
    private Color color;
    // Constructor method that creates a new Rectangle object.
    public Rectangle(double xPos, double yPos, double width, double height) {
        this.xPos = xPos;
        this.yPos = yPos;
        this.width = width;
        this .height = height;
    }
    // function method that calculates the perimeter of the rectangle object
    public double calculatePerimeter(){
       double rectPerimeter = 2*this.width + 2*this.height;
       return rectPerimeter;
    }
    // Function method that calculates the area of the rectangle object.
    public double calculateArea() {
        double rectArea = (2 * width) + (2 * height);
        return rectArea;
    }
    // setter method that sets the fill color of the rectangle
    public void setColor(Color color) {
        this.color = color;
    }
    // setter method that sets the bottom upper left corner of the rectangle
    public void setPos(double xPos, double yPos){
        this.xPos = xPos;
        this.yPos = yPos;
    }
    // setter method that sets the height of the rectangle.
    public void setHeight(double height) {
        this.height = height;
    }
    // Setter method that sets the width of the rectangle.
    public void setWidth(double width){
        this.width = width;
    }
    // getter method that sets the color of the rectangle
    public Color getColor() {
        return this.color;
    }
    // getter method that gets the x-position of the upper left corner of the rectangle
    public double getXPos() {
        return this.xPos;
    }
    // Getter method that gets the y-position of the upper left corner of the rectangle
    public double getYPos(){
        return this.yPos;
    }
    // getter method that gets the height of the rectangle
    public double getHeight() {
        return this.height;
    }
    // Getter method that gets the width of the rectangle.
    public double getWidth(){
        return this.width;
    }

}
