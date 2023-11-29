package week12.classwork;

public class MyThread extends Thread {
    public void run() {
        System.out.println("thread is running... " + Thread.currentThread().getName());

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
