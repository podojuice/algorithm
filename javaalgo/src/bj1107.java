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
		int check=0; // ����/�Ʒ��� �� �ڸ� ���� ���� �ϴ���.
		int numnum=0; // ���ؾߵ� �ڸ���.
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

		
		
		// com�� ���� ����. ���� �޾Ҵ� ����. �ٵ� ���ؾߵ� �ڸ���������.
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
			// �ڸ��� ���ϱ�
			for(int j=0; j<numnum; j++) {
				gop = gop*10;
			}
			// result�� �ڸ��� * number+now �Ѱ� ����
			result += (number[numnum]+now)*gop;
			
			// tmin�� ������. tmin�� �������� ���� ��ư �� ���� ���� ��.
			int tmin=0;
			for(int i=0; i<10; i++) {
				if(!broken[i]) {
					tmin = i;
					break;
				}
			}
			// �׸��� �� tmin���� �Ʒ� ������ �� ����.
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
		
		
		
		// ������ʹ� ���� ���� ��.
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
