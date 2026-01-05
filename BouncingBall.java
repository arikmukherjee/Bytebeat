import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;

/*<applet code="BouncingBall" width=300 height=100>
</applet>
*/

public class BouncingBall extends Applet implements Runnable {
    private int x = 50;      // Ball's x position
    private int y = 50;      // Ball's y position
    private int radius = 20; // Ball's radius
    private int dx = 2;      // Change in x (velocity)
    private int dy = 2;      // Change in y (velocity)
    private Thread animator;
    private Image offscreenImage;
    private Graphics offscreenGraphics;

    @Override
    public void init() {
        setSize(400, 300); // Set the size of the applet
    }

    @Override
    public void start() {
        if (animator == null) {
            animator = new Thread(this);
            animator.start();
        }
    }

    @Override
    public void stop() {
        if (animator != null) {
            animator.interrupt();
            animator = null;
        }
    }

    @Override
    public void run() {
        while (Thread.currentThread() == animator) {
            updateBall();
            repaint();
            try {
                Thread.sleep(10); // Pause for a short duration (10 ms)
            } catch (InterruptedException e) {
                // Handle interruption
            }
        }
    }

    public void updateBall() {
        x += dx;
        y += dy;

        // Check for collisions with the applet boundaries
        if (x < radius || x > getWidth() - radius) {
            dx = -dx;
        }
        if (y < radius || y > getHeight() - radius) {
            dy = -dy;
        }
    }

    @Override
    public void update(Graphics g) {
        // Implement double buffering to avoid flickering
        if (offscreenImage == null) {
            offscreenImage = createImage(getWidth(), getHeight());
            offscreenGraphics = offscreenImage.getGraphics();
        }

        offscreenGraphics.setColor(getBackground());
        offscreenGraphics.fillRect(0, 0, getWidth(), getHeight());
        offscreenGraphics.setColor(getForeground());
        paint(offscreenGraphics);

        g.drawImage(offscreenImage, 0, 0, this);
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.RED);
        g.fillOval(x - radius, y - radius, 2 * radius, 2 * radius);
    }
}