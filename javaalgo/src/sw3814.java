import java.util.*;
import java.io.*;


public class sw3814 {
	static int[] arr;
	static int MAX, ans, N, K;
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("sw3814")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			arr = new int[N];
			MAX = 1000000000;
//			System.out.println(MAX);
			for(int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());
			
			System.out.println("#"+tc+ " "+binary(0, MAX));
			
			
		}
	}
	static int binary(int s, int e) {
		
		while(s<=e) {
			int mid = (s+e)/2;
			int sum = 0;
			int[] tarr = new int[N];
			for(int i=0; i<N; i++) tarr[i] = arr[i];
			// 여기서부터 검증.
			
			for(int i=0; i<N-1; i++) {
				if(tarr[i]<tarr[i+1]) {
					if(tarr[i+1]-tarr[i]>mid) {
						// 여기서 이제 mid까지 깎아줘야함.
						int tmp = tarr[i+1]-tarr[i]-mid;
						sum += tmp;
						tarr[i+1] -= tmp;
					}
				} else if (tarr[i+1]<tarr[i]) {
					if(tarr[i]-tarr[i+1] > mid) {
						int tmp = tarr[i]-tarr[i+1] - mid;
						sum += tmp;
						tarr[i] -= tmp;
					}
					int ttmp = i;
					while(ttmp>0) {
						if(tarr[ttmp-1]>tarr[ttmp]) {
							if(tarr[ttmp-1]-tarr[ttmp] > mid) {
								int tmp = tarr[ttmp-1]-tarr[ttmp] - mid;
								sum += tmp;
								tarr[ttmp-1] -= tmp;
								ttmp --;
							}
							else break;
						} else break;
					}
				}
			}
			if(sum<=K) e = mid-1;
			else s = mid+1;
		}
		
		return s;
	}
}
