package week12.classwork;

import java.util.ArrayList;

public interface InnerFunWithJava {

    public int add(int x, int y);
    
}

public class FunWithJava implements Runnable {

    public int number = 0;

    public static class Coordinates {
        int x;
        int y;
        ArrayList list;

        public Coordinates(int x, int y, ArrayList list) {
            this.x = x;
            this.y = y;
            this.list = list;
        }
    }

    public static void main(String[] args) {
        int value1 = 150;
        int value2 = 50;

        int[] list = new int[5];
        float[] flist = new float[7];
        String[] slist = new String[10];

        ArrayList myList = new ArrayList();
        myList.add(value1);

        Coordinates c = new Coordinates(value1, value2, myList);

        FunWithJava funWithJava = new FunWithJava();
        funWithJava.example();
        funWithJava.number = funWithJava.number + 1;

        FunWithJava funWithJava2 = new FunWithJava();
        System.out.println(funWithJava2.number);
        funWithJava.add(value1, value2);

        MyThread myThread = new MyThread();
        myThread.start();

        try {
            myThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void example() {
        number = number + 1;
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'run'");
    }
}