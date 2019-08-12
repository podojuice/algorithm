

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class bj2146 {
	static int[][] map;
	static boolean[][] used;
	static int N;
	static int MIN;
	static int[][] island;
	static int islandNum;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int[][] Q;
	static int cnt;
	
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N]; used = new boolean[N][N]; island = new int[N][N]; 
		MIN = 2*N; islandNum = 1;
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				int tmp = Integer.parseInt(st.nextToken());
				map[i][j] = tmp;
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if (map[i][j] == 1 && island[i][j] == 0) {
					Q = new int[10000][2];
					Q[0][0] = i; Q[0][1] = j;
					BFS1();
					islandNum ++;
				}
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				for(int k=0; k<4; k++) {
					int tx = i+dx[k]; int ty = j+dy[k];
					if (tx>=0 && tx<N && ty>=0 && ty<N && map[i][j] == 0) {
						if (map[tx][ty] != 0) {
							used = new boolean[N][N];
							used[i][j] = true;
							Q = new int[10000][2];
							Q[0][0] = i; Q[0][1] = j;
							BFS2(island[tx][ty]);
							break;
						}
					}
				}
			}
		}
		
		System.out.println(MIN);
	}
	
	static void BFS2(int key) {
		int S = 0; int E = 1; cnt = 1;
		while (E>S) {
			if (cnt == MIN) { 
				return;
			}
			int ts = S; int te = E;
			for (int p=0; p<te-ts; p++) {
				int x = Q[S][0]; int y = Q[S][1];
				for(int k=0; k<4; k++) {
					int tx = x+dx[k]; int ty = y+dy[k];
					if(tx>=0 && tx<N && ty>=0 && ty<N) {
						if (island[tx][ty] != 0 && island[tx][ty] != key) {
							MIN = cnt;
							return;
						}
					}
					
				}

				for(int k=0; k<4; k++) {
					int tx = x+dx[k]; int ty = y+dy[k];
					if(tx>=0 && tx<N && ty>=0 && ty<N) {
						if(map[tx][ty] == 0 && used[tx][ty] == false) {
							Q[E][0] = tx; Q[E][1] = ty;
							used[tx][ty] = true;
							E ++ ;
						}
					}
				}
				S ++;
			}
			cnt ++;
		}
	}
	
	static void BFS1() {
		int S = 0; int E = 1;
		while (E>S) {
			int x = Q[S][0]; int y = Q[S][1];
			island[x][y] = islandNum;
			for(int k=0; k<4; k++) {
				int tx = x+dx[k]; int ty = y+dy[k];
				if(tx>=0 && tx<N && ty>=0 && ty<N) {
					if(map[tx][ty] == 1 && used[tx][ty] == false) {
						Q[E][0] = tx; Q[E][1] = ty;
						used[tx][ty] = true;
						E ++ ;
					}
				}
			}
			S ++;
		}
	}
	
	
	
	
	
}
