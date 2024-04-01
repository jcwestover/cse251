public class PrimeThread extends Thread {
    
    int start;
    int end;
    int[] array;

    public PrimeThread(int s, int e, int[] a) {
        this.start = s;
        this.end = e;
        this.array = a;
    }

    static boolean isPrime(int n) 
    { 
        // Corner cases 
        if (n <= 1) return false; 
        if (n <= 3) return true; 
      
        // This is checked so that we can skip  
        // middle five numbers in below loop 
        if (n % 2 == 0 || n % 3 == 0) return false; 
      
        for (int i = 5; i * i <= n; i = i + 6) 
          if (n % i == 0 || n % (i + 2) == 0) 
            return false; 
      
        return true; 
    }

    @Override
    public void run() {
        for (int i = 0; i < array.length; i++) {
            if(isPrime(array[i])) {
                System.out.println(array[i] + " is prime");
            }
        }
    }
}
