// Written by Adam Kvant, kvant003; and Aidan Kadid, kadid010
// FractalDrawer class draws a fractal of a shape indicated by user input
import java.awt.Color;
import java.util.Scanner;
public class FractalDrawer {
    private double totalArea=0;  // class variable for tracking the total area
    // the class variable colorArray is initialized
    private static Color[] colorArray = new Color[8];

    public FractalDrawer(){}  // default constructor
    //TODO:
    // drawFractal creates a new Canvas object
    // and determines which shapes to draw a fractal by calling appropriate helper function
    // drawFractal returns the area of the fractal
    public double drawFractal(String type) {
        //If the user input passed in is rectangle, triangle, or circle, one of the if statements will start the recursive process
        // Canvas objects are initialized in each respective shape
        if (type.equals("circle")){
            Canvas newCanvas = new Canvas(800,800);
            //Calls the drawCircleFractal to begin the recursive drawing of a circle.
            drawCircleFractal(100, 200,200, Color.red, newCanvas, 0);
        }
        else if (type.equals("triangle")){
            Canvas newCanvas = new Canvas(800,800);
            //Calls the drawTriangleFractal to begin the recursive drawing of a triangle.
            drawTriangleFractal(200,200,400,400,Color.red,newCanvas,0);
        }
        else if (type.equals("rectangle")) {
            Canvas newCanvas = new Canvas(800,800);
            //Calls the drawRectangleFractal to begin the recursive drawing of a rectangle.
            drawRectangleFractal(200,200,400,400, Color.red,newCanvas,0);
        }
        // the total area is returned when the drawFractal method is called with ANY other string
        return this.totalArea;

    }
    //TODO:
    // drawTriangleFractal draws a triangle fractal using recursive techniques
    public void drawTriangleFractal(double width, double height, double x, double
            y, Color c, Canvas can, int level){
        // recursion only persists if the level is less than 8, meaning this fractal will have 8 levels of recursion
        if (level < 8){
            //base case which establishes the largest RED Triangle object, draws it, calculates the area and calls the next recursive statement
            if (level == 0){
                //Creates the baseTriangle object, sets its color, draws it, and calculates its area.
                Triangle baseTriangle = new Triangle(x, y, width,height);
                baseTriangle.setColor(c);
                can.drawShape(baseTriangle);
                totalArea += baseTriangle.calculateArea();
                level++;
                //Recursive Call to call the function to draw the smaller triangles with half of the width and the height, respectively.
                drawTriangleFractal(width/2, height/2, x, y, c, can, level);
            }
            //Enters here if the base triangle has already been drawn.
            else {
                // the main recursive statement which starts by creating 3 new Triangle objects
                Triangle triObj1 = new Triangle(x-width,y,width,height);
                Triangle triObj2 = new Triangle(x+width/2,y-2*height, width,height);
                Triangle triObj3 = new Triangle(x+2*width,y,width,height);

                //Color is set for all the new Triangle objects by referencing the appropriate level color in colorArray
                triObj1.setColor(colorArray[level]);
                triObj2.setColor(colorArray[level]);
                triObj3.setColor(colorArray[level]);
                //totalArea is calculated for the triangles that have just been drawn and is added to the totalArea of the previous triangles.
                totalArea = totalArea + triObj1.calculateArea() + triObj2.calculateArea() + triObj3.calculateArea();
                // The Triangle objects are drawn on the canvas object
                can.drawShape(triObj1);
                can.drawShape(triObj2);
                can.drawShape(triObj3);
                // level is incremented in order to prevent infinite recursion
                level++;
                //Recursive calls to call the function to draw smaller triangles with half of the width and the height, respectively
                //at the 3 corners of the triangle that was just drawn.
                drawTriangleFractal(width/2,height/2,x-width,y,c,can,level);
                drawTriangleFractal(width/2, height/2, x+width/2, y-2*height, c, can, level);
                drawTriangleFractal(width/2, height/2, x+2*width, y, c, can, level);

            }
        }
        else{
            //Calls drawFractal method with an empty string as to return the totalArea of the fractal.
            drawFractal("");
        }
    }
    // TODO:
    // drawCircleFractal draws a circle fractal using recursive techniques
    public void drawCircleFractal(double radius, double x, double y, Color c, Canvas can, int level) {
        // recursion only persists if the level is less than 8, meaning this fractal will have 8 levels of recursion
           if (level < 8) {
               //base case which establishes the largest RED circle object, draws it, calculates the area and calls the next recursive statement
               if (level==0){
                   Circle baseCircle = new Circle(x,y,radius);
                   baseCircle.setColor(c);
                   totalArea += baseCircle.calculateArea();
                   can.drawShape(baseCircle);
                   level++;
                   // radius is halved to make the new objects shrink as they are supposed to in a fractal
                   drawCircleFractal(radius/2,x,y,c,can,level);

               }
               else{
                   // the main recursive statement which starts by creating 4 new Circle objects
                   Circle CirObj1 = new Circle(x+2*radius,y+2*radius,radius);
                   Circle CirObj2 = new Circle(x+2*radius,y-2*radius,radius);
                   Circle CirObj3 = new Circle(x-2*radius,y+2*radius,radius);
                   Circle CirObj4 = new Circle(x-2*radius,y-2*radius,radius);

                   //Color is set for all the new Circle objects by referencing the appropriate level color in colorArray
                   CirObj1.setColor(colorArray[level]);
                   CirObj2.setColor(colorArray[level]);
                   CirObj3.setColor(colorArray[level]);
                   CirObj4.setColor(colorArray[level]);
                   // area is tallied for all new Circle objects
                   totalArea = totalArea + CirObj1.calculateArea() + CirObj2.calculateArea() + CirObj3.calculateArea() + CirObj4.calculateArea();
                   // the circle objects are drawn on the canvas object
                   can.drawShape(CirObj1);
                   can.drawShape(CirObj2);
                   can.drawShape(CirObj3);
                   can.drawShape(CirObj4);
                   // level is incremented in order to prevent infinite recursion
                   level++;
                   // recursive function calls that pass in the same values as the values used by the Circle objects in this level
                   drawCircleFractal(radius/2, x+2*radius, y+2*radius, c, can, level);
                   drawCircleFractal(radius/2, x+2*radius,y-2*radius,c,can,level);
                   drawCircleFractal(radius/2, x-2*radius, y+2*radius, c, can, level);
                   drawCircleFractal(radius/2, x-2*radius,y-2*radius,c,can,level);

               }
           }
           // calls drawFractal with an empty string in order to return the area of the fractal
           else drawFractal("");
    }
    //TODO:
    // drawRectangleFractal draws a rectangle fractal using recursive techniques
    public void drawRectangleFractal(double width, double height, double x, double
            y, Color c, Canvas can, int level) {
        // recursion only persists if the level is less than 8, meaning this fractal will have 8 levels of recursion
        if (level < 8){
            //base case which establishes the largest RED Rectangle object, draws it, calculates the area and calls the next recursive statement
            if (level == 0){
                Rectangle baseRectangle = new Rectangle(x, y, width,height);
                baseRectangle.setColor(c);
                can.drawShape(baseRectangle);
                level++;
                // height and width are halved to make the new objects shrink as they are supposed to in a fractal
                drawRectangleFractal(width/2, height/2, x, y, c, can, level);
            }
            else {
                // the main recursive statement which starts by creating 4 new Rectangle objects
                Rectangle retObj1 = new Rectangle(x-width,y+2*height,width,height);
                Rectangle retObj2 = new Rectangle(x+2*width,y-height,width,height);
                Rectangle retObj3 = new Rectangle(x-width,y-height,width,height);
                Rectangle retObj4 = new Rectangle(x+2*width,y+2*height,width,height);

                //Color is set for all the new Rectangle objects by referencing the appropriate level color in colorArray
                retObj1.setColor(colorArray[level]);
                retObj2.setColor(colorArray[level]);
                retObj3.setColor(colorArray[level]);
                retObj4.setColor(colorArray[level]);
                // Area is tallied for all new Rectangle objects
                totalArea = totalArea + retObj1.calculateArea() + retObj2.calculateArea() + retObj3.calculateArea() + retObj4.calculateArea();
                // The Rectangle objects are drawn on the canvas object
                can.drawShape(retObj1);
                can.drawShape(retObj2);
                can.drawShape(retObj3);
                can.drawShape(retObj4);
                // level is incremented in order to prevent infinite recursion
                level++;
                // recursive function calls that pass in the same values as the values used by the Rectangle objects in this level
                drawRectangleFractal(width/2,height/2,x-width,y+2*height,c,can,level);
                drawRectangleFractal(width/2, height/2, x+2*width, y-height, c, can, level);
                drawRectangleFractal(width/2, height/2, x-width, y-height, c, can, level);
                drawRectangleFractal(width/2, height/2, x+2*width, y+2*height, c, can, level);

            }
        }
        else{
            // calls drawFractal with an empty string in order to return the area of the fractal
            drawFractal("");
        }
    }
    //TODO:
    // main should ask user for shape input, and then draw the corresponding fractal.
    // should print area of fractal
    public static void main(String[] args) {
        // idea 2 on readme has the guide I used to create an array object.
        // color values are assigned for each level of the fractal, Note: colorArray[0] is not used
        // colorArray[0] is kept as red as the base case uses red for user readability of the array.
        colorArray[0] = Color.red;
        colorArray[1] = Color.orange;
        colorArray[2] = Color.yellow;
        colorArray[3] = Color.green;
        colorArray[4] = Color.blue;
        colorArray[5] = Color.pink;
        colorArray[6] = Color.cyan;
        colorArray[7] = Color.yellow;
        //Creates a new Scanner object to take in user input.
        Scanner myScanner = new Scanner(System.in);
        System.out.println("Enter the shape (circle, triangle, rectangle) you would like to be used: ");
        String shape = myScanner.nextLine();
        int counter = 0;
        //Checks to make sure that the user entered an allowed shape.
        while (counter != 1) {
            if (shape.equals("circle")) {
                counter = 1;
            } else if (shape.equals("rectangle")) {
                counter = 1;
            } else if (shape.equals("triangle")) {
                counter = 1;
            } else {
                // an "Error" message that prompts the user to enter the correct shape
                System.out.println("Incorrect input, please input circle, triangle, or rectangle");
                shape = myScanner.nextLine();
            }
        }
        //Creates a FractalDrawer object
        FractalDrawer newFractalObj = new FractalDrawer();
        //Sets the area to the return of the drawFractal method and then prints the area.
        double area = newFractalObj.drawFractal(shape);
        System.out.println("The total area of the fractal is " + area);
    }
}