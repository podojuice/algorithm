import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj1967 {
	static int[] tree;
	static boolean[] haschild;
	
	public static void main(String[] args) throws Exception{
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("bj1967")));
		int N = Integer.parseInt(br.readLine());
		tree = new int[N+2]; haschild = new boolean[N+1];
		for(int i=0; i<N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int dis = Integer.parseInt(st.nextToken());
			if(tree[s*2]==0) {
				tree[s*2] = dis;
				haschild[s] = true;
			} else {
				tree[s*2+1] = dis;
			}
		}
		
		System.out.println(Arrays.toString(tree));
		System.out.println(Arrays.toString(tree));
		
		
	}
	
	
	
	
}
