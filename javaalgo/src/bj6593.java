
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj6593 {
	static char[][][] map;
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("bj6593.txt")));
		while(true) {
			st = new StringTokenizer(br.readLine());
			int L = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			map = new char[L][R][C];
			if(L == 0) break;
			
			for(int i=0; i<L; i++) {
				for(int j=0; j<R; j++) {
					map[i][j] = br.readLine().toCharArray();
					System.out.println(Arrays.toString(map[i][j]) );
				}
				br.readLine();
			}
		}
	}
}
