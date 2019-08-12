
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileReader;

public class sw1843 {
	public static void main(String[] args) throws Exception {
		File tmp = new File("sw1843.txt");
		BufferedReader br = new BufferedReader(new FileReader(tmp));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				int card = Integer.parseInt(st.nextToken());
				for (int j=0; j<card; j++) {
					int tmp1 = Integer.parseInt(st.nextToken());
					System.out.println(tmp1);
				}
			}
		}
		
	}
}
