

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class bj6359 {
	static boolean[] jail;
	static int[] ans;
	public static void main(String[] args) throws Exception {
		File tmp = new File("bj6359.txt");
		BufferedReader br = new BufferedReader(new FileReader(tmp));
		int T = Integer.parseInt(br.readLine());
		jail = new boolean[101];
		ans = new int[101];
		for(int i=1; i<=100; i++) {
			int cnt = 1;
			while(i*cnt <= 100) {
				jail[i*cnt] = !jail[i*cnt];
				cnt ++;
			}
		}
		
		for(int i=1; i<=100; i++) {
			if(jail[i] == true) {
				ans[i] = ans[i-1]+1;
			} else {
				ans[i] = ans[i-1];
			}
		}
		for(int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			
			System.out.println(ans[N]);
		}
	}
}
