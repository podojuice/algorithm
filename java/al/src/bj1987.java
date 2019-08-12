
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;


public class bj1987 {
	static int MAX;
	static int[][] map;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	static boolean[] alpa;
	static int N, M;
	
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj1987.txt")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		char[][] tmp = new char[N][M];
		MAX = 0;
		for(int i=0; i<N; ++i) {
			tmp[i] = br.readLine().toCharArray();
			for(int j=0; j<M; ++j) {
				map[i][j] = tmp[i][j]-'A';
			}
			
		}
		alpa = new boolean[26];
		alpa[map[0][0]] = true;
		DFS(0, 0, 1);
		System.out.println(MAX);
	}
	
	static void DFS(int x, int y, int cnt) {
		
		if(cnt>MAX) {
			MAX = cnt;
		}
		for(int i=0; i<4; i++) {
			int tx = x+dx[i]; int ty = y+dy[i];
			if(tx>=0 && tx<N && ty >= 0 && ty < M) {
				if(!alpa[map[tx][ty]]) {
					alpa[map[tx][ty]] = true;
					DFS(tx, ty, cnt+1);
					alpa[map[tx][ty]] = false;
				}
			}
		}
		
	}
}
