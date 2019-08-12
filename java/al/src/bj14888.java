
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.File;
import java.io.FileReader;
import java.util.StringTokenizer;


public class bj14888 {
	static int list[];
	static int MAX, MIN;
	static int N;
	
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj14888")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		list = new int[N];
		int[] oper = new int[4];
		MAX = -1000000000; MIN = 1000000000;
		for(int i=0; i<N; i++) {
			list[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<4; i++) {
			oper[i] = Integer.parseInt(st.nextToken());
		}
		
		DFS(oper, 0, list[0]);
		System.out.println(MAX);
		System.out.println(MIN);
	}
	
	static void DFS(int[] oper, int now, int add) {
		if(now == N-1) {
			if (add > MAX) {
				MAX = add;
			}
			if (add < MIN) {
				MIN = add;
			}
			return;
		}
		for(int i=0; i<4; i++) {
			if(oper[i] != 0) {
				oper[i]--;
				int tmp = add;
				if(i ==0) {
					add = add + list[now+1];
				} else if (i == 1) {
					add = add - list[now+1];
				} else if (i==2) {
					add = add*list[now+1];
				} else {
					add = add / list[now+1];
				}
				DFS(oper, now+1, add);
				oper[i]++;
				add = tmp;
			}
		}
	}
}
