
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;


public class sw7586 {
	static char[][] map;
 	static int[][] right;
 	static int[][] left;
	static int cnt;
	static int N;
	
	public static void main(String[] args) throws Exception {
		File tmp = new File("sw7586.txt");
		BufferedReader br = new BufferedReader
				(new FileReader(tmp));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			map = new char[N][N];
			right = new int[N][N];
			left = new int[N][N];
			cnt = 0;
			for(int i=0; i<N; i++) {
				map[i]=br.readLine().toCharArray();
			}
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(map[i][j] == 'B') {
						if(j==0) {
							right[i][j] = 1;
						} else {
							right[i][j] = right[i][j-1] +1;
						}
					}
					
				}
			}
			for(int i=0; i<N; i++) {
				for(int j=N-1; j>=0; j--) {
					if(map[i][j] == 'B') {
						if(j==N-1) {
							left[i][j] = 1;
						} else {
							left[i][j] = left[i][j+1] +1;
						}
					}
					
				}
			}

			for(int i=N-1; i>0; i--) {
				for(int j=N-1; j>=0; j--) {
					int MIN = right[i][j];
					int sumnum = 0;
					for(int k=i; k>=0; k--) {
						if(right[k][j] < MIN) {
							MIN = right[k][j];
						} 
						sumnum += MIN;
					}
					right[i][j] = sumnum;
				}
			}
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					int MIN = left[i][j];
					int sumnum = 0;
					for(int k=i; k<N; k++) {
						if(right[k][j] < MIN) {
							MIN = left[k][j];
						} 
						sumnum += MIN;
					}
					left[i][j] = sumnum;
				}
			}
			System.out.println(Arrays.deepToString(right));
			System.out.println(Arrays.deepToString(left));

			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
						if(right[i][j] > 1) {
							int key = right[i][j]-1;
							for(int x=0; x<N; x++) {
								for(int y=0; y<N; y++) {
									if(x>i || y>j) {
										if(left[x][y]>1) {
											System.out.println(i+" "+ j+" "+ x+" "+ y + "   " + key*(left[x][y]-1));
											cnt += key*(left[x][y]-1);
											
										}
										
									}
								}
							}
						}
						
					
				}
			}
			
			System.out.println("#"+tc+ " "+cnt);
		}
	}
	


}
