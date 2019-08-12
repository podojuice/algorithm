import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj15686 {
	static int cnum;
	static int[][] chicken;
	static int hnum;
	static int[][] home;
	static int MIN;
	static boolean[] used;
	static int[][] distance;
	
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br = new BufferedReader(new FileReader(new File("bj15686")));
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		hnum = 0; cnum=0; chicken = new int[13][2]; home = new int[2*N][2]; MIN = 1000000;
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				int tmp = Integer.parseInt(st.nextToken());
				if (tmp == 1) {
					home[hnum][0] = i; home[hnum][1] = j;
					hnum ++;
				}
				if (tmp == 2) {
					chicken[cnum][0] = i; chicken[cnum][1] = j;
					cnum++;
				}
			}
		}
		distance = new int[cnum][hnum];
		
		for(int i=0; i<cnum; i++) {
			int cx = chicken[i][0]; int cy = chicken[i][1];
			for(int j=0; j<hnum; j++) {
				int hx = home[j][0]; int hy = home[j][1];
				int x = hx-cx; int y =hy-cy;
				if(x<0) x = x*-1;
				if(y<0) y = y*-1;
				distance[i][j] = x+y;
			}
		}
		
		
		used = new boolean[cnum];
		check(0, M, 0);
		System.out.println(MIN);
		
	}
	
	static void check(int cnt, int M, int asdf) {
		if(cnt == M) {
			int sumnum=0;
			for(int i=0; i<hnum; i++) {
				int tmp = 1000000;
				for(int j=0; j<cnum; j++) {
					if (used[j]) {
						if (distance[j][i] < tmp) {
							tmp = distance[j][i];
						}
					}
				}
				sumnum += tmp;
				
			}
			if(sumnum < MIN) MIN = sumnum;
			return;
		}
		
		for(int i=asdf; i<cnum; i++) {
			if (!used[i]) {
				used[i] = true;
				check(cnt+1, M, i);
				used[i] = false;
			}
		}
	}
	
	
}
