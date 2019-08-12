
import java.util.Scanner;
import java.io.File;

public class sw1249 {
	static int[][] map;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int N;
	static boolean[][] asdf;
	static int[][] used;
	/**
	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(new File("1249.txt"));
		int T = sc.nextInt();
		for(int tc=1; tc<=10; tc++) {
			N = sc.nextInt();
			map = new int[N][N];
			for(int i = 0; i<N; i++) {
				String temp = sc.next();
				for(int j=0; j<N; j++) {
					int push = temp.charAt(j) -'0';
					map[i][j] = push;
				}
			}
			asdf = new boolean[N][N];
			used = new int[N][N];
			asdf[0][0] = true;
			BFS(0, 0);
			System.out.println("#"+tc+" " +used[N-1][N-1]);
			
		}
	}
	
	static void BFS(int x, int y) {
		if (x==N-1 && y==N-1) {
			return;
		}
		else {
			for(int i=0; i<4; i++) {
				int nx = x+dx[i]; int ny = y+dy[i];
				
				if(0<=nx && nx<N && 0<=ny && ny<N) {
					int compare = used[x][y]+map[nx][ny];
					if (asdf[nx][ny] == false) {
						asdf[nx][ny] = true;
						used[nx][ny] = compare;
//						DFS(nx, ny);
					} else {
						if (compare <used[nx][ny]) {
							used[nx][ny] = compare;
//							DFS(nx, ny);
						}
					}
					
				}
				
			}
		}
		
	}
	
	static class Node {
		int a; 
		int b;
		Node next;
		Node before;
		public Node(int x, int y) {
			this.a = x;
			this.b = y;
			this.next = null;
			this.before = null;
		}
	}
	
	static class Queue {
		Node head;
		Node rear;
		public Queue(Node a) {
			this.head = a;
			this.rear = a;
		}
		
		public void push(Node a) {
			this.rear.next = a;
			this.rear = a;
		}
		
		public Node pop() {
			Node tmp = this.head;
			this.head = this.head.next;
			return tmp;
		}
	}

}
