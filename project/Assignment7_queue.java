import java.util.Scanner;

public class Assignment7_queue {
    private int front, rear, capacity;
    private int[] queue;

    // Constructor
    Assignment7_queue(int size) {
        capacity = size;
        queue = new int[capacity];
        front = 0;
        rear = -1;
    }


    // Check if the queue is full
    public boolean isFull() {
        return rear == capacity - 1;
    }

    // Check if the queue is empty
    public boolean isEmpty() {
        return front > rear;
    }

    // Enqueue operation
    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue is full. Cannot enqueue " + item);
            return;
        }
        queue[++rear] = item;
        System.out.println(item + " enqueued to queue.");
    }

    // Dequeue operation
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot dequeue.");
            return -1;
        }
        int item = queue[front++];
        System.out.println(item + " dequeued from queue.");
        return item;
    }

    // Peek operation
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return -1;
        }
        return queue[front];
    }

    // Display the queue
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        System.out.print("Queue: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(queue[i] + " ");
        }
        System.out.println();
    }

    // Main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Assignment7_queue q = new Assignment7_queue(5);

        while (true) {
            System.out.println("\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value to enqueue: ");
                    int value = sc.nextInt();
                    q.enqueue(value);
                    break;
                case 2:
                    q.dequeue();
                    break;
                case 3:
                    int front = q.peek();
                    if (front != -1)
                        System.out.println("Front element: " + front);
                    break;
                case 4:
                    q.display();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}

