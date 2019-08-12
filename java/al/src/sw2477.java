

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class sw2477 {
	static int[][] rc;
	static int[][] rp;
	static int[] arriveTime;
	static int[] wait;
	static int[] ans;
	
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			rc = new int[3][N]; rp = new int[3][M]; arriveTime = new int[K+1]; ans = new int[K+1]; wait = new int[K+1]; int num1 =1; int num2=1; int num3=1;
			st = new StringTokenizer(br.readLine());
			int rm=0;
			for(int i=0; i<N; i++) {
				rc[0][i] = Integer.parseInt(st.nextToken());
				if (rc[0][i] > rm) {
					rm = rc[0][i];
				}
			}
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<M; i++) {
				rp[0][i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<K; i++) {
				arriveTime[i+1] = Integer.parseInt(st.nextToken());
			}
			int cnt = 0;
			while(num3 <= K) {
				if(num2<=K) {
					for(int i=0; i<N; i++) {
						if(rc[1][i] != 0) {
							rc[2][i] ++;
							if(rc[2][i] == rc[0][i]) {
								wait[num2] = rc[1][i];
								rc[1][i] = 0; rc[2][i] = 0;
								num2++;
							}
						}
						if(num1 <=K && arriveTime[num1] <= cnt && rc[1][i] == 0) {
							rc[1][i] = num1;
							if(i+1 == A) {
								ans[num1] ++;
							}
							num1 ++;
						}
					}
					
					cnt++;
				}
				for(int i=0; i<M; i++) {
					if(rp[1][i] != 0) {
						rp[2][i] ++;
						if(rp[2][i] == rp[0][i]) {
							rp[1][i] = 0; rp[2][i] = 0;
						}
					}
					if (num3<=K && wait[num3] != 0  && rp[1][i] == 0) {
						rp[1][i] = wait[num3];
						if(i+1 == B) {
							ans[wait[num3]] +=2;
						}
						num3 ++;
					}
				}
				
			}
			int asdf=0;
			for(int i=0 ; i<=K; i++) {
				if(ans[i] == 3) {
					asdf += i;
				}
			}
			if (asdf == 0) {
				asdf = -1;
			}
			System.out.println("#"+tc+" " +asdf);
		}
	}
}
