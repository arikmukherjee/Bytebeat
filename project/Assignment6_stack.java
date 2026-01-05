public class Assignment6_stack {
    private int maxSize;
    private int[] stackArray;
    private int top;

    // Constructor
    public Assignment6_stack(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    // Push operation
    public void push(int value) {
        if (isFull()) {
            System.out.println("Stack is full. Cannot push " + value);
        } else {
            stackArray[++top] = value;
            System.out.println(value + " pushed to stack.");
        }
    }

    // Pop operation
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty. Cannot pop.");
            return -1;
        } else {
            return stackArray[top--];
        }
    }

    // Peek operation
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty. Nothing to peek.");
            return -1;
        } else {
            return stackArray[top];
        }
    }

    // Check if stack is empty
    public boolean isEmpty() {
        return (top == -1);
    }

    // Check if stack is full
    public boolean isFull() {
        return (top == maxSize - 1);
    }

    // Main method to test the stack
    public static void main(String[] args) {
        Assignment6_stack myStack = new Assignment6_stack(5);

        myStack.push(10);
        myStack.push(20);
        myStack.push(30);

        System.out.println("Top element is: " + myStack.peek());
        System.out.println("Popped element: " + myStack.pop());
        System.out.println("Top element after pop: " + myStack.peek());

        while (!myStack.isEmpty()) {
            System.out.println("Popped: " + myStack.pop());
        }

        myStack.pop(); // Attempt to pop from empty stack
    }
}
