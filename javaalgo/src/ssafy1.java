import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

public class ssafy1 {
	
	static int[] arr;
	static int[] sorted1;
	static int[] sorted2;
	static int MIN;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("1")));
		// �ٴ��� N/2�� N-1�� �ݹ� ������. 
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=T; tc++) {
			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			arr = new int[N]; sorted1 = new int[N]; sorted2 = new int[N];
			for(int i=0; i<N; i++) {
				int tmp =Integer.parseInt(st.nextToken());
				arr[i] = tmp;
				sorted1[i] = tmp;
				sorted2[i] = tmp;
			}
			sorted1 = arr;
			sorted2 = arr;
			Arrays.sort(sorted1);
			System.out.println(Arrays.toString(arr));
			// arr �ϼ�.
			MIN = 6;
			check(N, 0);
			
		}
	}
	
	static void check(int N, int cnt) {
		if(cnt>5) {
			return;
		}
		for(int i=0; i<N; i++) {
			// N��ŭ ���鼭,
			// ���ݺο���,
			if(i<N/2) {
				
			}
		}
	}
	
	
	
}
