import java.util.*;
import java.io.*;


public class sw3998 {
	static int[] arr;
	static int[] dp;
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			arr = new int[N];
			dp = new int[N];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			for(int i=1; i<N; i++) {
				for(int j=i-1; j>=0; j--) {
					if(arr[i]<arr[j]) {
						dp[i] = dp[j]+1;
						break;
					}
				}
			}
			int ans = 0;
			for(int i=0; i<N; i++) {
				if(dp[i] != 0) ans += dp[i];
			}
			System.out.println(Arrays.toString(dp));
			System.out.println("#"+tc+" " +ans);
		}
		
	}
}
