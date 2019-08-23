
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;

public class kakao_choosuck {
	public static void main(String[] args) throws ParseException{
		String[] l = new String[1];
		l[0] = "2016-09-15 20:59:57.421 0.351s";
		solution(l);
		
	}
	static Node[] arr;
	static int solution(String[] lines) throws ParseException {
		SimpleDateFormat f = new SimpleDateFormat("HH:mm:ss.SSS");
		int len = lines.length;
		arr = new Node[len];
		int cnt = 0;
		// 입력받기.
		for(String s: lines) {
			String[] tmp = s.split(" ");
			String end = tmp[1];
			String tt = tmp[2].substring(0, tmp[2].length()-1);
			float ttt = Float.parseFloat(tt);
			int time = (int)(ttt*1000);
			System.out.println(time);
			Date d1 = f.parse(end);
			Date d2 = f.parse("00:00:00.000");
			long et = d1.getTime()-d2.getTime() + 3000;
			long st = (et)-time+1;
			System.out.println();
			System.out.println(st+ " "+ et);
			arr[cnt] = new Node(st, et);
			cnt++;
		}
		int MAX = 1;
		for(int i=0; i<len-1; i++) {
			int sum = 1;
			long nowend = arr[i].end;
			for(int j=i+1; j<len; j++) {
				if(arr[j].start>=nowend) {
					sum ++;
				}
			}
			if(sum>MAX) {
				sum = MAX;
			}
		}
		System.out.println(MAX);
	    return MAX;
	  }
	
	static class Node {
		long start;
		long end;
		
		Node(long s, long e) {
			this.start = s;
			this.end = e;
		}
	}
	
	
	
	
}
