import java.util.*;
import java.io.*;

public class sw3813 {
	static int[] ssd;
	static int[] mass;
	static int MAX, ans, N, K;
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("sw3813")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			ans = 200000; MAX = 0;
			ssd = new int[N]; mass = new int[K];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				ssd[i] = Integer.parseInt(st.nextToken());
				if(ssd[i]>MAX) MAX = ssd[i];
			}
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<K; i++) mass[i] = Integer.parseInt(st.nextToken());
			
			System.out.println("#"+tc + " " +binary(0, MAX));
//			System.out.println(binary(0, MAX));
			
			
		}
		
	}
	
	static int binary(int s, int e) {
		while(s<=e) {
			int mid = (s+e)/2;
//			System.out.println(s+ " "+e);
//			System.out.println(mid);
			if(check(mid)) e = mid-1;
			else s = mid+1;
//			System.out.println(s+ " "+e);
		}
		return s;
	}
	
	static boolean check(int num) {
		int i = 0;
		int cnt = 0;
		for(int j=0; j<K; j++) {
			int now = mass[j];
			while(i<N) {
				boolean poss = true;
				for(int k=0; k<now; k++) {
					if(i+k>=N) return false;
					if(ssd[i+k]>num) {
						poss = false;
						i += k+1;
						break;
					}
				}
				if(poss) {
					i += now;
					cnt++;
					break;
				}
			}
		}
		if(cnt != K) return false;
		return true;
	}
}
