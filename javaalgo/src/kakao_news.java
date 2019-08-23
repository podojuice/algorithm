
public class kakao_news {
	public static void main(String[] args) {
	}
	
	public int solution(String str1, String str2) {
		char[] A = str1.toLowerCase().toCharArray();
		char[] B = str2.toLowerCase().toCharArray();
		int[] Aarr = new int[27*27];
		int[] Barr = new int[27*27];
		for(int i=1; i<A.length; i++) {
			int a = A[i-1]-0; int b = A[i]-0;
			if(97<=a && a<=122 && 97<=b && b<=122) {
				Aarr[a*27+b] ++;
			}
			
		}
		for(int i=1; i<B.length; i++) {
			int a = B[i-1]-0; int b = B[i]-0;
			if(97<=a && a<=122 && 97<=b && b<=122) {
				Barr[a*27+b] ++;
			}
		}
		int hap=0; int gyo = 0;
		for(int i=0; i<27*27; i++) {
			hap += Math.max(Aarr[i], Barr[i]);
			gyo += Math.min(Aarr[i], Barr[i]);
		}
		if(hap == 0) {
			return 65536;
		} else {
			float tmp = (float)gyo/(float)hap;
			return (int)(tmp*65536);
		}
	}

}
