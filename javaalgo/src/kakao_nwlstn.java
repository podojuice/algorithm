
public class kakao_nwlstn {
	public static void main(String[] args) {
		solution(16, 16, 2, 1);
	}

	public static String solution(int n, int t, int m, int p) {
		int cnt = 0;
		int now = 0;
		StringBuilder sb = new StringBuilder();
		sb.append("0");
		while(cnt < t) {
			now ++;
			if(cnt*m+p == now) {
				cnt++;
			}
			int tmp = now;
			StringBuilder sb2 = new StringBuilder();
			while(tmp != 0) {
				int tmp2 = tmp%n;
				if(tmp2>=10) {
					sb2.insert(0, ((char)(55+tmp2)));
				} else {
					sb2.insert(0, ""+tmp2);
				}
				tmp = tmp/n;
			}
			sb.append(sb2);
		}
		cnt = 0;
		StringBuilder answer = new StringBuilder();
		while(cnt<t) {
			answer.append(sb.charAt(cnt*m+p-1));
			cnt++;
		}
		System.out.println(answer.toString());
		return answer.toString();
	}
}
