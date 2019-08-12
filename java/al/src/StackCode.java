

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class StackCode {
	static int[] stack;
	static int top;
	static int num;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int tc = Integer.parseInt(br.readLine());
		for(int i=1; i<=tc; i++) {
			num = Integer.parseInt(br.readLine());
			stack = new int[num];
			top = 0;
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<num; j++) {
				int tmp = Integer.parseInt(st.nextToken());
				push(tmp);
			}
			System.out.print("#"+i+" ");
			for(int j=0; j<num; j++) {
				pop();
			}
			System.out.println();
		}

	}
	static void push(int a) {
		stack[top] = a;
		if(top != num-1) {
		top ++;
		}
	}
	static boolean isFull() {
		if (top==num-1) {
			return true;
		}
		return false;
	}
	static void pop() {
		System.out.print(stack[top]+ " ");
		top--;
	}

}
