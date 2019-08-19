
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileReader;

public class sw5357 {
	static int[] train;
	public static void main(String[] args) throws Exception {
		File tmp = new File("sw5170.txt");
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(tmp));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken()); int H = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			train = new int[N];
			for(int i=0; i<N; i++) {
				int x = Integer.parseInt(st.nextToken());
				train[i] = x;
			}
			
			st = new StringTokenizer(br.readLine());
			int len = 0;
			int cnt = 0;
			for(int i=0; i<N; i++) {
				int x = Integer.parseInt(st.nextToken());
				if(x==0) {
					len += train[i];
					if(len >= H || i == 0 || i==N-1) {
						len = 0;
						cnt ++;
					}
				} else {
					len = 0;
				}
			}
			
			System.out.println("#"+tc+" "+cnt);
		}
	}
}