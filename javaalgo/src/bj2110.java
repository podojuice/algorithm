import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj2110 {
	static int[] house;
	static int N;
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj2110")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		house = new int[N];
		for(int i=0; i<N; i++) {
			house[i] = Integer.parseInt(br.readLine());
		}
		sort(0, N-1);
		System.out.println(binary(0, house[N-1], C));
		System.out.println(Arrays.toString(house));
	}
	
	static int binary(int start, int end, int key) {
		int mid;
		while(start<=end) {
			mid = (start+end)/2;
			// 커스터마이징 논리
			int tmp = 0;
			int cnt = 1;
			for(int i=1; i<N; i++) {
				if(house[i] - house[tmp] >=mid) {
					if(++cnt==key) {
						break;
					}
					tmp = i;
				}
			}
			// 끝났다? 체크 후 넘김.
			if(cnt == key) start = mid+1;
			else end = mid-1;
		}
		return end;
	}
	
	
	static void sort(int start, int end) {
		int pivot = (start+end)/2;
		int l = start; int r = end;
		int temp;
		if(start < end) {
			while(l<r) {
				while(house[l]<=house[pivot] && l<end) {
					l++;
				}
				while(house[r] > house[pivot]) {
					r--;
				}
				if(l<r) {
					temp = house[l];
					house[l] = house[r];
					house[r] = temp;
				}
			}
			temp = house[pivot];
			house[pivot] = house[r];
			house[r] = temp;
			sort(start, r-1);
			sort(r+1, end);
		}
		
	}
}
