
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class sw7829 {
	static int MIN;
	static int MAX;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("sw7829")));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc= 1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			MIN = 1000000; MAX = 0;
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				int tmp = Integer.parseInt(st.nextToken());
				if (tmp < MIN) {
					MIN = tmp;
				}
				if(tmp>MAX) {
					MAX = tmp;
				}
			}
			System.out.println("#"+tc+" " +MIN*MAX);
		}
		
	}
}
