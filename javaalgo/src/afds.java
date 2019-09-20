import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class afds {
	static long[][] arr;
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("sw3820")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			arr = new long[N][2];
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				arr[i][0] = Integer.parseInt(st.nextToken());
				arr[i][1] = Integer.parseInt(st.nextToken());
			}		
			Arrays.sort(arr, new Comparator<long[]>() {
				public int compare(long[] o1, long[] o2) {
					long tmp = o1[1]*(o2[0]-1)-o2[1]*(o1[0]-1);
					if(tmp<0) return -1;
					else return 1;
				}
			});
			
			long ans = 1;
			
			for(int i=0; i<N; i++) {
				ans = (ans*arr[i][0]+arr[i][1])%1000000007;
			}
			System.out.println("#"+tc+" "+ans);
		}
	}
}
