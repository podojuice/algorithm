import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileReader;



public class bj2252 {
	static int N;
	static int M;
	static List[] arr;
	static int[] cnt;
	static int front;
	static int rear;
	
	public static void main(String[] args) throws Exception {
		StringTokenizer st;
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj2252")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new List[N+1];
		cnt = new int[N+1];
		for(int i=1; i<=N; i++) {
			arr[i] = new List();
		}
		for ( int i=0; i<M; i++ ) {
			st = new StringTokenizer(br.readLine());
			int F = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			if(arr[F] == null) {
				arr[F] = new List();
			} else {
				arr[F].push(B);
			}
			cnt[B] ++;
		}
		int[] q = new int[N];
		front = 0; rear = 0;
		for(int i=1; i<=N; i++) {
			if(cnt[i]==0) q[rear++] = i;
		}
		while(front != rear) {
			int tmp = q[front++];
			System.out.print(tmp+" ");
			Node now = arr[tmp].head;
			while(now!=null) {
				if(--cnt[now.data]==0) {
					q[rear++] = now.data;
				}
				now=now.next;
			}
		}
	}
	
	static class Node{
		int data;
		Node next;
		
		Node(int a) {
			this.data = a;
		}
		
	}
	
	static class List{
		Node head;
		Node tail;
		
		void push(int a) {
			if(head == null) {
				this.head = new Node(a);
				this.tail = head;
			} else {
				Node tmp = new Node(a);
				this.tail.next = tmp;
				this.tail = tmp;
			}
		}
	}
}
