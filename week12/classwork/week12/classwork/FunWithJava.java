package week12.classwork;

import java.util.ArrayList;

public class FunWithJava {

    static class InnerClass {
        private int arg1;
        private String arg2;
        public static double PI = 3.14159;

        public InnerClass(int arg1, String arg2) {
            this.arg1 = arg1;
            this.arg2 = arg2;
        }
    }

    public static void main(String[] args) {
        int[] myArray = new int[10];

        for (int i = 0; i < 10; i++) {
            myArray[i] = i * i;
            System.out.println(myArray[i]);
        }

        ArrayList<Double> list = new ArrayList<>();
        for (double i = 0; i < 10; i++) {
            list.add(i);
        }

        System.out.println("list=" + list);

        InnerClass innerClass1 = new InnerClass(-17, "Hello");
        System.out.println("innerClass1.arg1=" + innerClass1.arg1);
        System.out.println("innerClass1.arg2=" + innerClass1.arg2);
        System.out.println("innerClass1.PI=" + InnerClass.PI);
        InnerClass.PI = 4.0;

        InnerClass innerClass2 = new InnerClass(151617, "Good-Bye");
        System.out.println("innerClass2.arg1=" + innerClass2.arg1);
        System.out.println("innerClass2.arg2=" + innerClass2.arg2);
        System.out.println("innerClass2.PI=" + InnerClass.PI);
        
    }
}