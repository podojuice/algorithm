import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj5430 {
	static char[] def;
	static int[] list;
	static boolean R;
	static boolean err;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj5430")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			def = br.readLine().toCharArray();
			int N = Integer.parseInt(br.readLine());
			String tmp = br.readLine();
			int len = tmp.length();
			tmp = tmp.substring(1, len-1);
			st = new StringTokenizer(tmp, ",");
			list = new int[N];
			int front = 0; int rear = N; R = true; err= false;
			for(int i=0; i<N; i++) {
				list[i] = Integer.parseInt(st.nextToken());
			}
			for(int i=0; i<def.length; i++) {
				if(def[i] == 'R') R = !R;
				else {
					if(front == rear) {
						err = true;
					}
					if(R) front ++;
					else rear --;
				}
			}
			if(err) {
				System.out.println("error");
				continue;
			}
			if(R) {
				System.out.print("[");
				for(int i=front; i<rear; i++) {
					System.out.print(list[i]);
					if(i != rear-1) {
						System.out.print(",");
					}
				}
				System.out.print("]");
				System.out.println();
			} else {
				System.out.print("[");
				for(int i=rear-1; i>=front; i--) {
					System.out.print(list[i]);
					if(i != front) {
						System.out.print(",");
					}
				}
				System.out.print("]");
				System.out.println();
			}
			
			
		}
	}
}
