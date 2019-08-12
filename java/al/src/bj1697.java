
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj1697 {
	static int[] map;
	static Node curr;
	static Node head;
	static int cnt;
	static int answer;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int subin = Integer.parseInt(st.nextToken());
		int sister = Integer.parseInt(st.nextToken());
		map = new int[100001];
		map[subin] = 1;
		head = new Node(subin);
		curr = head;
		cnt=0;

		while(true) {
			if(map[sister]!=0) {
				answer = map[sister];
				break;
			}
			add1(head.data);
			head = head.next;
			
		}
		head = new Node(sister);
		curr = head;
		while(head != null) {
			if(map[head.data] == 1) {
				cnt += 1;
			}
			add2(head.data);
			head = head.next;
			
		}
		
		
		System.out.println(map[sister]-1);
		System.out.println(cnt);
	}
	static void add1(int a) {
		if (a+1<=100000) {
			push(a, a+1);
		}
		if (a-1 >=0) {
			push(a, a-1);
		}
		if (a*2 <=100000) {
			push(a, a*2);
		}
	}
	static void add2(int a) {
		if (a+1<=100000 && map[a+1] == map[a]-1) {
			Node tmp = new Node(a+1);
			curr.next = tmp;
			curr = tmp;
		}
		if (a-1 >=0 && map[a-1] == map[a]-1) {
			Node tmp = new Node(a-1);
			curr.next = tmp;
			curr = tmp;
		}
		if (a%2 == 0 && a/2 <=100000 && map[a/2] == map[a]-1) {
			Node tmp = new Node(a/2);
			curr.next = tmp;
			curr = tmp;
		}
	}
	static void push(int a ,int b) {
		if (map[b] != 0) {
			return;
		} else {
			map[b] = map[a]+1;
			Node tmp = new Node(b);
			curr.next = tmp;
			curr = tmp;
		}
		
	}
	
	static class Node{
		public int data;
		public Node next;
		
		Node(int a) {
			this.data = a;
			this.next = null;
		}
	}
		
}
