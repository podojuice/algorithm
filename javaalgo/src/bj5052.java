import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;

public class bj5052 {
	static boolean yes;
	public static void main(String[] args) throws Exception{
//		BufferedReader br = new BufferedReader(new FileReader(new File("bj5052")));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc=0; tc<T; tc++) {
			yes = true;
			Tree trie = new Tree();
			int N = Integer.parseInt(br.readLine());
			for(int i=0; i<N; i++) {
				if(yes) {
					trie.push(br.readLine());
				} else {
					break;
				}
			}
			if(yes) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		}
		
	}
	
	static class Node {
		Node[] child;
		boolean isEnd;
		
		Node() {
			this.child = new Node[10];
			this.isEnd=false;
		}
	}

	static class Tree {
		Node root;
		Tree() {
			this.root = new Node();
		}
		void push(String str) {
			Node tmp = this.root;
			for(int i=0; i<str.length(); i++) {
				if(tmp.isEnd) {
					yes = false;
					return;
				}
				if(i == str.length()-1 && tmp.child[str.charAt(i)-'0'] != null) {
					yes = false;
					return;
				} else {
					if(tmp.child[str.charAt(i)-'0'] == null) {
						tmp.child[str.charAt(i)-'0'] = new Node();
					}
					tmp = tmp.child[str.charAt(i)-'0'];
				}
				
				
			}
			tmp.isEnd = true;
		}
	}

}


