import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj1107 {
	static boolean[] broken;
	static int[] number;
	static int MIN;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("bj1107")));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tmp = Integer.parseInt(br.readLine());
		int key = tmp;
		int N = Integer.parseInt(br.readLine());
		number = new int[6];
		int cnt = 0;
		MIN = key-100;
		if(key == 0) {
			cnt = 1;
		}
		while(key != 0) {
			number[cnt] = key%10;
			key = key/10;
			cnt ++;
		}
		if(MIN < 0) {
			MIN = MIN * -1;
		}
		broken = new boolean[10];
		if(N>0) {
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				broken[Integer.parseInt(st.nextToken())] = true;
			}
		}
		int check=0; // 위로/아래로 몇 자리 까지 봐야 하는지.
		int numnum=0; // 비교해야될 자리수.
		for(int i=cnt-1; i>=0; i--) {
			if(broken[number[i]]) {
				numnum = i;
				for(int j=1; j<10; j++) {
					if(number[i]-j>=0 && !broken[number[i]-j]) {
						check+=j;
						if(number[i]+j<10 && !broken[number[i]+j]) {
							check+=j*10;
						}
						break;
					}
					if(number[i]+j<10 && !broken[number[i]+j]) {
						check+=j*10;
						break;
					}
					
				}
				break;
			}
		}

		
		
		// com은 비교할 숫자. 원래 받았던 숫자. 근데 비교해야될 자리수까지만.
		int com = 0;
		for(int i=0; i<=numnum; i++) {
			int gop=1;
			for(int j=0; j<i; j++) {
				gop = gop*10;
			}
			com += number[i]*gop;
		}
		
		

		int result=0;
		int ttmp = 0;
		if(check>=10) {
			int now = check/10;
			check = check%10;
			int gop = 1;
			// 자릿수 구하기
			for(int j=0; j<numnum; j++) {
				gop = gop*10;
			}
			// result에 자릿수 * number+now 한걸 더함
			result += (number[numnum]+now)*gop;
			
			// tmin을 구하자. tmin은 망가지지 않은 버튼 중 가장 작은 수.
			int tmin=0;
			for(int i=0; i<10; i++) {
				if(!broken[i]) {
					tmin = i;
					break;
				}
			}
			// 그리고 그 tmin으로 아래 수들을 다 고정.
			for(int i=0; i<numnum; i++) {
				gop = 1;
				for(int j=0; j<i; j++) {
					gop = gop*10;
				}
				result += (tmin)*gop;
			}
			
			ttmp = result - com;
			if(ttmp<0) {
				ttmp = ttmp*-1;
			}
			ttmp += cnt;
			if(MIN>ttmp) { 
				MIN = ttmp;
			}
		}
		
		
		result=0;
		ttmp = 0;
		
		
		
		// 여기부터는 작은 수일 때.
		if(check<10) {
			System.out.println(result);
			int now = check;
			int gop = 1;
			for(int j=0; j<numnum; j++) {
				gop = gop*10;
			}
			result += (number[numnum]-now)*gop;
			int tmax=0;
			for(int i=9; i>=0; i--) {
				if(!broken[i]) {
					tmax = i;
					break;
				}
			}
			for(int i=0; i<numnum; i++) {
				gop = 1;
				for(int j=0; j<i; j++) {
					gop = gop*10;
				}
				result += (tmax)*gop;
			}

			ttmp = result - com;
			if(ttmp<0) {
				ttmp = ttmp*-1;
			}
			ttmp += cnt;
			if(MIN>ttmp) { 
				MIN = ttmp;
			}
		}
		System.out.println(cnt);
		System.out.println(com);
		System.out.println(result);
		System.out.println(check);
		System.out.println(numnum);
		System.out.println(MIN);
	}
}
