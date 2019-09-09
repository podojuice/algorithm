import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class sw3282 {
	static int[][] pack;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("sw3282")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			pack = new int[N+1][K+1];
			for (int i = 1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				int vol = Integer.parseInt(st.nextToken());
				int pri = Integer.parseInt(st.nextToken());
				for(int j=0; j<vol; j++) {
					pack[i][j] = pack[i-1][j];
				}
				for(int j=vol; j<=K; j++) {
					// ºÎÇÇ.
					if(pack[i-1][j] <pack[i-1][j-vol]+pri) pack[i][j] = pack[i-1][j-vol]+pri;
					else pack[i][j] = pack[i-1][j];

				}
			}
			System.out.println("#"+tc+" " +pack[N][K]);
		}
		
	}
}