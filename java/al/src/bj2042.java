

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj2042 {
	static int[] value;
	static long[] tree;
	
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new FileReader(new File("bj2042.txt")));
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		value = new int[N];
		int H = 1;
		while(H<N) {
			H <<= 1; 
		}
		H <<= 1;
		tree = new long[H];
		for(int i=0; i<N; ++i) {
			value[i] = Integer.parseInt(br.readLine());
		}
		makeTree(0, 0, N-1);
		for(int i=0; i<K+M; ++i) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			if(a==1) {
				long diff = c-value[--b];
				value[b] = c;
				update(0, 0, N-1, b, diff);
			} else {
				System.out.println(sum(0, 0, N-1, b-1, c-1));
			}
		}
//		System.out.println(Arrays.toString(tree));
	}
	
	
	static long makeTree(int idx, int start, int end) {
		if(start == end) {
			return tree[idx] = value[start];
		} else {
			return tree[idx] = makeTree(idx*2+1, start, (start+end)/2)+makeTree(idx*2+2, (start+end)/2+1, end );
		}
	}
	
	static void update(int idx, int start, int end, int change, long diff) {
		if(change < start || change > end) return;
		tree[idx] += diff;
		if(start != end) {
			update(idx*2+1, start, (start+end)/2, change, diff);
			update(idx*2+2, (start+end)/2+1, end, change, diff);
		}
	}
	static long sum(int idx, int start, int end, int left, int right) {
		if (left > end || right < start) {
			return 0;
		}
		if(left <=start && right >= end) {
			return tree[idx];
		}
		return sum(idx*2+1, start, (start+end)/2, left, right) + sum(idx*2+2, (start+end)/2+1, end, left, right);
	}
}
