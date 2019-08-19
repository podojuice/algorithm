import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.File;
import java.util.StringTokenizer;

public class bj2178 {
	static char[][] map;
	static int[][] ans;
	static int[] q;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj2178")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		map = new char[N][M]; ans = new int[N][M]; q = new int[N*M*2+1];
		for(int i=0; i<N; i++) {
			map[i] = br.readLine().toCharArray();
			for(int j=0; j<M; j++) {
				if(map[i][j] == '1') {
					ans[i][j] = 1;
				}
			}
		}
		int now = 0; int curr = 1;
		q[0] = 0; q[1] = 0;
		
		while(now<N*M) {
			int nx = q[now*2]; int ny = q[now*2+1];
			for(int i=0; i<4; i++) {
				int tx = nx + dx[i]; int ty  = ny + dy[i];
				if(tx>=0 && tx<N && ty>=0 && ty<M) {
					if (map[tx][ty] == '1' && ans[tx][ty] == 1) {
						ans[tx][ty] += ans[nx][ny];
						if(tx==N-1 && ty == M-1) {
							now = N*M;
							break;
						}
						q[curr*2] = tx; q[curr*2+1] = ty;
						curr ++;
					}
				}
			}
			now ++;
		}
		System.out.println(ans[N-1][M-1]);
		
	}
}
