import java.util.*;
import java.io.*;

public class bj2014 {
	public static void main(String[] args) throws IOException {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		int k = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
	 
	    long[] prime = new long[k];
	    heapInit();
	    st = new StringTokenizer(br.readLine());
	    for (int i = 0; i < k; i++) {
	        prime[i] = Integer.parseInt(st.nextToken());
	        heapPush(prime[i]);
	    }
	    long head = 0;
	 
	    for (int i = 0; i < n; i++) {
	        head = heapPop();

	        for (int j = 0; j < k; j++) {
	            long value = head * prime[j];
	            heapPush(value);
	 
	            if (head % prime[j] == 0) {
	                break;
	            }
	        }
	    }
	    System.out.println(head);
	}
	static final int MAX_SIZE = 100000;
	 
    static long heap[] = new long[MAX_SIZE];
    static int heapSize = 0;
 
    static void heapInit()
    {
        heapSize = 0;
    }
 
    static void heapPush(long value)
    {
        if (heapSize + 1 > MAX_SIZE)
        {
            return;
        }
 
        heap[heapSize] = value;
 
        int current = heapSize;
        while (current > 0 && heap[current] < heap[(current - 1) / 2]) 
        {
            long temp = heap[(current - 1) / 2];
            heap[(current - 1) / 2] = heap[current];
            heap[current] = temp;
            current = (current - 1) / 2;
        }
 
        heapSize = heapSize + 1;
    }
 
    static long heapPop()
    {
        if (heapSize <= 0)
        {
            return -1;
        }
 
        long value = heap[0];
        heapSize = heapSize - 1;
 
        heap[0] = heap[heapSize];
 
        int current = 0;
        while (current < heapSize && current * 2 + 1 < heapSize)
        {
            int child;
            if (current * 2 + 2 >= heapSize)
            {
                child = current * 2 + 1;
            }
            else
            {
                child = heap[current * 2 + 1] < heap[current * 2 + 2] ? current * 2 + 1 : current * 2 + 2;
            }
 
            if (heap[current] < heap[child])
            {
                break;
            }
 
            long temp = heap[current];
            heap[current] = heap[child];
            heap[child] = temp;
 
            current = child;
        }
        return value;
    }

}
