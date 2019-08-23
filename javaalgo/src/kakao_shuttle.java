import java.util.Arrays;

public class kakao_shuttle {
	
	public static void main(String[] args) {
		solution(1, 1, 5, new String[] {"08:00", "08:01", "08:02", "08:03"});
	}
	
	
	static String solution(int n, int t, int m, String[] timetable) {
		int[] tt = new int[timetable.length];
		for(int i=0; i<timetable.length; i++) {
			tt[i] = Integer.parseInt(timetable[i].replace(":", ""));
		}
		
		Arrays.sort(tt);
		
		int ccnt = 0;
		int start = 900;
		int pcnt = 0;
		int key = -1;
		// 온 사람들 하나하나 보면서 갈거임. 
		for(int i=0; i<tt.length; i++) {
			// i번째 잇는 사람이 start시간보다 작다면, pcnt를 더해줘야지.
			if(tt[i] <= start) {
				pcnt ++;
			} else {
				// 만약 cnt가 m보다 작거나 같다면, 지금까지 온 사람 다 탈 수 있다.
				if(pcnt<=m) {
					pcnt = 0;
					start += n;
					ccnt ++;
				}
			}
			if(ccnt>=t) {
				key = i;
				break;
			}
		}
		System.out.println(ccnt+ " "+ key+ " "+ start);
		
		
		
		return "1";
		
		
	  }

}
