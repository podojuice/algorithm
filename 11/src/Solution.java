import java.util.ArrayList;
import java.util.HashSet;


class Solution {
	public static void main(String args[]) throws Exception {
		solution("KAKAO");
	}

	static int[] solution(String msg) {
		ArrayList<String> list = new ArrayList<>();
		StringBuilder sb;
		HashSet<String> hs = new HashSet<>();
		list.add("-");
		ArrayList<Integer> ta = new ArrayList<>();
		for (int i = 65; i < 65 + 26; i++) {
			char t = (char)i;
			String tmp = t+"";
			list.add(tmp);
			hs.add(tmp);
		}
		
		// 입력 다 받았고, hashset에도 넣었다. 이제 보자.
		int i = 0;
		while(i<msg.length()) {
			sb = new StringBuilder();
			int j=i;
			while(j<msg.length()) {
				sb.append(msg.charAt(j));
				String key = sb.toString();

				// 셋에 key가 없으면, hs에 key 추가, list에도 추가. 
				if(hs.add(key)) {
					ta.add(list.indexOf(key.substring(0, key.length()-1)));
					hs.add(key);
					list.add(key);
					i=j-1;
					break;
				} else if(j == msg.length()-1) {
					ta.add(list.indexOf(key));
					i = j;
					break;
				}
				j++;
			}
			i++;
		}
		
		int[] answer = new int[ta.size()];
		for(int k=0; k<ta.size(); k++) {
			answer[k] =ta.get(k);
		}
		
		return answer;
		
	}
}
