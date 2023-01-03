// https://www.lintcode.com/problem/454/
// Implement a Rectangle class which include the following attributes and methods:

// Two public attributes width and height.
// A constructor which expects two parameters width and height of type int.
// A method getArea which would calculate the size of the rectangle and return.

class RectangleArea {

  public int width;
  public int height;

  public Rectangle(int width, int height) {
    this.width = width;
    this.height = height;
  }

  public int getArea() {
    return this.width * this.height;
  }
}
