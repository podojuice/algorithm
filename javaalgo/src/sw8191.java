
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileReader;

public class sw8191 {
	static int[] book;
	public static void main(String[] args) throws Exception {
		File tmp = new File("sw8191.txt");
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(tmp));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			book = new int[N+1];
			int cnt = 1;
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				book[Integer.parseInt(st.nextToken())] = i;
			}
			for(int i=N; i>1; i--) {
				if (book[i] <= book[i-1]) {
					cnt ++;
				}
			}
			System.out.println("#"+ tc+" "+ cnt);
		}
		
	}
}
