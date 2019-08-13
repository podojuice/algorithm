import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class sw7793 {
	static char[][] map;
	static int[][] ans;
	static int MIN;
	static int[] q;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("sw7793")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			MIN = 2500;	map = new char[N][M];
			q = new int[N*M*4]; 
			ans = new int[N][M];
			int sx=0; int sy=0; int ax=0; int ay=0; int front = 0; int rear = 0;
			for(int i=0; i<N; i++) {
				map[i] = br.readLine().toCharArray();
				for(int j=0; j<M; j++) {
					if(map[i][j] == 'S') {
						sx = i; sy=j;
					} else if(map[i][j] == 'D') {
						ax=i; ay=j;
					} else if(map[i][j] == '*') {
						q[rear*2] = i; q[rear*2+1] = j;
						rear++;
					}
				}
			}
			q[rear*2] = sx; q[rear*2+1] = sy; rear++;
			int nx; int ny;
			loop:while(front<rear) {
				nx = q[front*2]; ny = q[front*2+1];
				front++;
				for(int i=0; i<4; i++) {
					int tx = nx+dx[i]; int ty = ny+dy[i];
					if(tx>=0 && tx<N && ty>=0 && ty<M) {
						if(map[tx][ty] == 'D') {
							if(map[nx][ny] == 'S') {
								ans[tx][ty] = ans[nx][ny]+1;
								break loop;
							}
						}
						if(map[tx][ty] == '.') {
							map[tx][ty] = map[nx][ny];
							if(map[nx][ny] == 'S') {
								ans[tx][ty] = ans[nx][ny]+1;
							}
							q[rear*2] = tx; q[rear*2+1] = ty;
							rear++;
						}
					}
				}
			}
			for(int i=0; i<N; i++) {
				System.out.println(Arrays.toString(map[i]));
			}
			if(ans[ax][ay] == 0) {
				System.out.println("#"+ tc+ " "+ "GAME OVER");
			} else {
				System.out.println("#"+tc+" "+ans[ax][ay]);
				
			}
			
		}
		
		
	}
}
