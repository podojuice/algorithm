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
		// �� ����� �ϳ��ϳ� ���鼭 ������. 
		for(int i=0; i<tt.length; i++) {
			// i��° �մ� ����� start�ð����� �۴ٸ�, pcnt�� ���������.
			if(tt[i] <= start) {
				pcnt ++;
			} else {
				// ���� cnt�� m���� �۰ų� ���ٸ�, ���ݱ��� �� ��� �� Ż �� �ִ�.
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
