import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1654 {
	static int[] lines;
	static int N;
	static int MAX;
	public static void main(String[] args)throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br = new BufferedReader(new FileReader(new File("bj1654")));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken()); 
		lines = new int[N]; MAX = 0;
		for(int i=0; i<N; i++) {
			lines[i] = Integer.parseInt(br.readLine());
		}
		int tmp= 1;
		for(int i=0; i<31; i++) tmp = tmp*2;
		tmp--;
		System.out.println(binary(0, tmp, K));
		
		
	}
	
	static long binary(long s, long e, int K) {
		long mid;
		while(s<=e) {
			mid = (s+e)/2;
			
			int tmp = 0;
			for(int i=0; i<N; i++) {
				tmp += lines[i]/mid;
			}
//			System.out.println(mid+" "+ s+ " "+ e+ " "+tmp);
			if(tmp>=K) s = mid+1;
			else e = mid-1;
		}
		return e;
	}
}
