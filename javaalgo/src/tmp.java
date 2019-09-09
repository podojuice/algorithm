
import java.io.*;
import java.util.*;;
 
public class tmp {
    public static void main(String[] args) {
		int[][] tmp = new int[2][2];
		tmp[0][0] = 1; tmp[0][1] = 2;
		tmp[1][0] = 2; tmp[1][1] = 1;
		
		Arrays.sort(tmp, new Comparator<int[]>() {
			public int compare(int[] o1, int[] o2) {
				return o1[1]-o2[1];
			}
		});
		System.out.println(Arrays.toString(tmp[1]));
	}
     
}