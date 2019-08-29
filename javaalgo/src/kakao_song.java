import java.util.Arrays;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class kakao_song {

	public static void main(String[] args) throws ParseException{
		String[] tmp = {"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"};
		solution("ABC", tmp);
	}
	
	static String[] songinfo;
	static String solution(String m, String[] musicinfos) throws ParseException {
		// �Էº��� �޾ƺ���.
		String answer = "";
		StringBuilder sb;

		int MAX = 0;
		for(int i=0; i<musicinfos.length; i++) {
			sb = new StringBuilder();
			songinfo = new String[4];
			songinfo = musicinfos[i].split(",");
			StringBuilder alpha = new StringBuilder();
			alpha.append(songinfo[3]);
			int j = 0;
			while(j<alpha.length()) {
				if(alpha.charAt(j) == '#') {
				
				}
			}

				

			int min = (int)(new SimpleDateFormat("hh:mm").parse(songinfo[1]).getTime() - new SimpleDateFormat("hh:mm").parse(songinfo[0]).getTime())/60000;
			// ��� �ð� min�� �����.
			
			// ���� �־��� �뷡 ����*2 ���̺��� ���� ����� �ð��� ������,
			int share = min/songinfo[3].length();
			int rest = min%songinfo[3].length();
			for(int k=0; k<share; k++) {
				sb.append(songinfo[3]);
			}
			sb.append(songinfo[3].substring(0, rest));
			String key = sb.toString();
			if(key.contains(m)) {
				if(min>MAX) {
					System.out.println(min+" "+ MAX);
					MAX = min;
					answer = songinfo[2];
				}
			}
			
		}
	   System.out.println(answer);
	   
	    return answer;
	}
}

