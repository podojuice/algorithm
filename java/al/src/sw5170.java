

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileReader;

public class sw5170 {
	static int[] dot;
	static int[][] map;
	static int cnt;
	public static void main(String[] args) throws Exception {
		File tmp = new File("sw5170.txt");
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(tmp));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			cnt = 0;
			if (N==1) {
				
			} else {
				map = new int[2002][2002];
				dot = new int[2*N];
				for(int i=0; i<N; i++) {
					st = new StringTokenizer(br.readLine());
					int tx = Integer.parseInt(st.nextToken());
					int ty = Integer.parseInt(st.nextToken());
					dot[2*i] = tx; dot[2*i+1] = ty;
				}
				for(int i=0; i<N; i++) {
					int x1 = dot[2*i]; int y1 = dot[2*i+1];
					for(int j=i+1; j<N; j++) {
						int x2 = dot[2*j]; int y2 = dot[2*j+ 1];
						int dx = x2-x1; int dy = y2-y1;	int check = 0;
						
						if(dx<0) {check ++;	dx = dx*-1;}
						if(dy<0) {check ++; dy = dy*-1;}
						if(check%2 == 1) {check = 2;}
						else {check = 1;}
						
						if(dy == 0) {dx = 0; dy = 0; check = 1;}
						else if (dx==0) {dx=0; dy=0; check = 2; }
						else {int G = gcm(dx, dy); dx = dx/G; dy = dy/G;}
						
						if(map[dx][dy] == check || map[dx][dy] == 3) {} 
						else {cnt ++; map[dx][dy] = map[dx][dy] + check;}
					}
				}
			}
			
			System.out.println("#"+tc+" "+cnt);
		}
	}
	
	static int gcm(int a, int b) {
		int tmp = 0;
		while(a != 0) {
			if(a<b) {
				tmp= a;
				a = b;
				b = tmp;
			}
			a = a-b;
		}
		
		return b;
	}
}
