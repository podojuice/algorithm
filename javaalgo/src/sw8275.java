
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class sw8275 {
	static int[] hamster;
	static int[][] lrs;
	static boolean[] unfix;
	static boolean ans;
	static int count;
	static int[] ret;
	static int MAX;
	static int[] idontknow;
	
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
		File tmp = new File("sw8275.txt");
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br = new BufferedReader(new FileReader(tmp));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int X = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			hamster = new int[N+1];
			lrs = new int[M][3];
			ans = false;
			unfix = new boolean[N+1];
			count = 0;
			MAX=0;
			
			for(int i=0; i<M; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<3; j++) {
					lrs[i][j] = Integer.parseInt(st.nextToken());
				}
				int start = lrs[i][0]; int end = lrs[i][1];
				for(int j=start; j<=end; j++) {
					unfix[j] = true;
				}
			}
			for(int j=1; j<=N; j++) {
				if(unfix[j]) {
					count ++;
				}
			}
			
			int now = X;
			if(X>10) {
				for(int i=1; i<count; i++) {
					int key = 1;
					for(int j=0; j<i; j++) {
						key = key*100;
					}
					now += X*key;
				}
			} else {
				for(int i=1; i<count; i++) {
					int key = 1;
					for(int j=0; j<i; j++) {
						key = key*10;
					}
					now += X*key;
				}
			}
			
			ret = new int[N+1];
			for(int i=0; i<=now; i++) {
				if(check(N,M,X,i)) {
					int ttmp = 0;
					for(int j=1; j<N+1; j++) {
						ttmp += hamster[j];
					}
					if(ttmp>MAX) {
						for(int j=1; j<=N; j++) {
							ret[j] = hamster[j];
						}
						MAX = ttmp;
					}
					
				}
			}
			if(ans) {
				for(int j=1; j<=N; j++) {
					if(!unfix[j]) {
						ret[j] = X;
						}
				}
				System.out.print("#"+tc+ " ");
				for(int i=1; i<=N; i++) {
					System.out.print(ret[i]+ " ");
					
				}
				System.out.println();
			} else {
				System.out.println("#"+ tc+ " "+-1);
			}
			
		}
		
	}
	static boolean check(int N, int M, int X, int key) {
		hamster = new int[N+1];
		if(X>10) {
			for(int i=N; i>0; i--) {
				if(unfix[i]) {
					if(key%100 <=X) {
						hamster[i] = key%100;
						key = key/100;
					} else {
						return false;
					}
				}
			}
		} else {
			for(int i=N; i>0; i--) {
				if(unfix[i]) {
					if(key%10 <=X) {
						hamster[i] = key%10;
						key = key/10;
					} else {
						return false;
					}
				}
			}
		}
		for(int i=N; i>0; i--) {
			if(unfix[i]) {
				if(key%100 <=X) {
					hamster[i] = key%100;
					key = key/100;
				} else {
					return false;
				}
			}
		}
		
		for(int i=0; i<M; i++) {
			int start = lrs[i][0]; int end = lrs[i][1];
			int sumnum = 0;
			for(int j=start; j<=end; j++) {
				sumnum += hamster[j];
			}
			if(sumnum != lrs[i][2]) {
				return false;
			}
		}
		ans = true;
		return true;
	}
	
}
