import java.util.Arrays;
import java.util.Comparator;

public class kakao_auto {
	
	public static void main(String[] args) {
		String[] input = {"img00.", "img-103 png", "img103.png", "ImG01.png", "IMG1", "img2.JPG"};
		solution(input);
//		System.out.println(' '-0);
	}
	
	static String[] solution(String[] files) {
		Node[] a = new Node[files.length];
		for (int i = 0; i < files.length; i++) {
			a[i] = new Node(files[i], i);
		}
		
		Arrays.sort(a, new Comparator<Node>() {
			public int compare(Node o1, Node o2) {
				String s1 = o1.name.toLowerCase();
				String s2 = o2.name.toLowerCase();
				if (s1.compareTo(s2) > 0) {
					return 1;
				} else if (s1.compareTo(s2) == 0) {
					return o1.number - o2.number;
				} else {
					return -1;
				}
			}
		});
		String[] answer = new String[files.length];
		for(int i=0; i<files.length; i++) {
			answer[i] = a[i].data;
		}
		return answer;
	}
	static class Node {
		String data;
		String name;
		int number;
		int idx;

		Node(String data, int idx) {
			this.data = data;
			this.idx = idx;
			boolean str = false;
			boolean num = false;
			int now = 0;
			for (int i = 0; i < data.length(); i++) {
				if (Character.isDigit(data.charAt(i)) && !str) {
					this.name = data.substring(now, i);
					now = i;
					str = true;
				} else if (str) {
					if (!Character.isDigit(data.charAt(i))) {
						this.number = Integer.parseInt(data.substring(now, i));
						num = true;
						break;
					}
				}
			}
			if(!num) {
				this.number = Integer.parseInt(data.substring(now));
			}
		}
	}

}
