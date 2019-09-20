import java.util.*;
import java.io.*;

public class sw4038 {
	public static void main(String[] args) throws Exception{
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for(int tc= 1; tc<=T; tc++) {
			String B = br.readLine();
			String S = br.readLine();
			int ans = 0;
			int blen = B.length();
			int slen = S.length();
			int hash = 257;
			int idx = 0;
			long hashkey = 0;
			long tmp = 1;
			for(int i=0; i<slen; i++) {
				hashkey *= hash;
				hashkey += S.charAt(i);
				if (i<slen) {
					tmp *= hash;
				}
			}

			long now = 0;
			while(idx<blen) {
				if(idx<slen) {
					now *= hash;
					now += B.charAt(idx);
					if(now == hashkey) ans ++;
					idx++;
				} else {
					now -= B.charAt(idx-slen)*tmp;
					now *= hash;
					now += B.charAt(idx);
					if(now == hashkey) ans ++;
					idx++;
				}
			}
			
			System.out.println("#"+tc+" " +ans);
		}
	}
}
