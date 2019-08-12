

import java.util.Scanner;
import java.io.File;

public class Main {
	static int[][] map;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int N;
	static boolean[][] used;
	static int[][] cnt;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(new File("1249.txt"));
		int T = sc.nextInt();
		for(int tc=1; tc<=10; tc++) {
			heap a = new heap();
			N = sc.nextInt();
			map = new int[N][N];
			for(int i = 0; i<N; i++) {
				String temp = sc.next();
				for(int j=0; j<N; j++) {
					int push = temp.charAt(j) -'0';
					map[i][j] = push;
				}
			}
			used = new boolean[N][N];
			cnt = new int[N][N];
			used[0][0] = true;
			int[] temp = {0, 0, 0};
			a.addLast(temp);
			BFS(a);
			System.out.println("#"+tc+" "+cnt[N-1][N-1]);

			
			
		}
		
	}
	
	/**
	 * @param a
	 */
	static void BFS(heap a) {
		
		while(true) {
			int[] tmp = a.pop();
			used[tmp[0]][tmp[1]] = true;
			for(int i=0; i<4; i++) {
				int x = tmp[0]+dx[i]; int y = tmp[1]+dy[i];
				if (x<N && x>=0 && y<N && y>=0) {
					if (used[x][y] == false) {
						
//						System.out.print(x+" ");
//						System.out.println(y);
						cnt[x][y] = tmp[2]+map[x][y];
						int[] add = new int[] {x, y, cnt[x][y]};
						a.addLast(add);
						if(x == N-1 && y==N-1) {
							return;
						}
						
					}
				}
			}
		}
	}
	
	static class heap {
		// 첫번째 노드를 가리키는 필드
	    private Node head;
	    private Node tail;
	    private int size = 0;
	    private class Node{
	        // 데이터가 저장될 필드
	        private int[] data;
	        // 다음 노드를 가리키는 필드
	        private Node next;
	        public Node(int[] input) {
	            this.data = input;
	            this.next = null;
	        }
	        // 노드의 내용을 쉽게 출력해서 확인해볼 수 있는 기능
	        public String toString(){
	            return String.valueOf(this.data);
	        }
	    }
	    public void addFirst(int[] input){
	        // 노드를 생성합니다.
	        Node newNode = new Node(input);
	        // 새로운 노드의 다음 노드로 해드를 지정합니다.
	        newNode.next = head;
	        // 헤드로 새로운 노드를 지정합니다.
	        head = newNode;
	        size++;
	        if(head.next == null){
	            tail = head;
	        }
	    }
	    public void addLast(int[] input){
	        // 노드를 생성합니다.
	        Node newNode = new Node(input);
	        // 리스트의 노드가 없다면 첫번째 노드를 추가하는 메소드를 사용합니다.
	        if(size == 0){
//	        	System.out.println(newNode.data[2]);11
	            addFirst(input);
	        } else {
	            // 마지막 노드의 다음 노드로 생성한 노드를 지정합니다.
	            tail.next = newNode;
	            // 마지막 노드를 갱신합니다.
	            tail = newNode;
	            // 엘리먼트의 개수를 1 증가 시킵니다.
	            size++;
	            int tmp = size-1;
		        while(tmp != 0) {
		        	if(node(tmp).data[2] < node((tmp-1)/2).data[2]) {
		        		swap(tmp, (tmp-1)/2);
		        		tmp = (tmp-1)/2;
		        	} else { break; }
		        }
	        }
	        
	    }
	    public void swap(int a, int b) {
	    	int[] tmp = node(a).data;
	    	node(a).data = node(b).data;
	    	
	    	node(b).data = tmp;
	    	

	    }
	    Node node(int index) {
	    	if (index>=size) {
	    		return null;
	    	}
	        Node x = head;
	        for (int i = 0; i < index; i++)
	            x = x.next;
	        return x;
	    }
	    public void add(int k, int[] input){
	        // 만약 k가 0이라면 첫번째 노드에 추가하는 것이기 때문에 addFirst를 사용합니다.
	        if(k == 0){
	            addFirst(input);
	        } else {
	            Node temp1 = node(k-1);
	            // k 번째 노드를 temp2로 지정합니다.
	            Node temp2 = temp1.next;
	            // 새로운 노드를 생성합니다.
	            Node newNode = new Node(input);
	            // temp1의 다음 노드로 새로운 노드를 지정합니다.
	            temp1.next = newNode;
	            // 새로운 노드의 다음 노드로 temp2를 지정합니다.
	            newNode.next = temp2;
	            size++;
	            // 새로운 노드의 다음 노드가 없다면 새로운 노드가 마지막 노드이기 때문에 tail로 지정합니다.
	            if(newNode.next == null){
	                tail = newNode;
	            }
	        }
	    }
	    public String toString() {
	        // 노드가 없다면 []를 리턴합니다.
	        if(head == null){
	            return "[]";
	        }       
	        // 탐색을 시작합니다.
	        Node temp = head;
	        String str = "[";
	        // 다음 노드가 없을 때까지 반복문을 실행합니다.
	        // 마지막 노드는 다음 노드가 없기 때문에 아래의 구문은 마지막 노드는 제외됩니다.
	        while(temp.next != null){
	            str += temp.data[2] + ",";
	            temp = temp.next;
	        }
	        // 마지막 노드를 출력결과에 포함시킵니다.
	        str += temp.data[2];
	        return str+"]";
	    }
	    public int[] pop(){
	        int[] returnData = head.data;
	        Node tmp = head.next;
	        head = node(size-1);
	        head.next = tmp;
	        tail = node(size-2);
	        tail.next = null;
	        size--;
	        int idx = 0;
	        while(true) {
	        	Node me = node(idx);
	        	Node com1 = node(idx*2+1);
	        	Node com2 = node(idx*2+2);
	        	if (com1!= null && com2!=null) {
	        		if(com1.data[2]>com2.data[2]) {
	        			if (com2.data[2] < me.data[2]) {
	        				swap(idx*2+2, idx);
	        				idx = idx*2+2;
	        			} else {break;}
	        		} else {
	        			if (com1.data[2] < me.data[2]) {
	        				swap(idx*2+1, idx);
	        				idx = idx*2+1;
	        			} else {break;}
	        		}
	        	} else if (com1 != null) {
	        		if (com1.data[2] < me.data[2]) {
	    				swap(idx*2+1, idx);
	    				idx = idx*2+1;
	    			} else {break;}
	        	} else if (com2 != null) {
	        		if (com2.data[2] < me.data[2]) {
	    				swap(idx*2+2, idx);
	    				idx = idx*2+2;
	    			} else {break;}
	        	} else {
	        		break;
	        	}
	        }
	        return returnData;
	    }

	    public int size(){
	        return size;
	    }
	    public Object get(int k){
	        Node temp = node(k);
	        return temp.data;
	    }

	}
}

