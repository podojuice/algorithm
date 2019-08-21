import java.util.Arrays;
import java.util.Comparator;

public class kakao4 {

}


class Solution {
	static int[][] answer;
	static int cnt;
	
    public int[][] solution(int[][] nodeinfo) {
    	int len = nodeinfo.length;
    	int[][] tmp = new int[len][3];
    	for(int i=0; i<len; ++i) {
    		tmp[i][0] = nodeinfo[i][0];
    		tmp[i][1] = nodeinfo[i][1];
    		tmp[i][2] = i+1;
    	}
    	Arrays.sort(tmp, new Comparator<int[]>() {
			public int compare(int[] o1, int[] o2) {
				return o2[1]-o1[1];
			}
		});
    	
    	Node root = new Node(tmp[0][0], tmp[0][1], tmp[0][2]);
    	for(int i=1; i<len; ++i) {
    		Node curr = root;
    		while(true) {
    			if(curr.x>tmp[i][0]) {
        			if (curr.left == null) {
        				curr.left = new Node(tmp[i][0], tmp[i][1], tmp[i][2]);
        				break;
        			} else {
        				curr = curr.left;
        			}
        		} else {
        			if (curr.right == null) {
        				curr.right = new Node(tmp[i][0], tmp[i][1], tmp[i][2]);
        				break;
        			} else {
        				curr = curr.right;
        			}
        		}
    		}
    	}
    	
        answer = new int[len][len];
        cnt = 0;
        firstrun(root);
        return answer;
    }
    static void firstrun(Node now) {
    	if(now == null) {
    		return;
    	}
    	answer[0][cnt] = now.idx;
    	cnt++;
    	firstrun(now.left);
    	firstrun(now.right);
    	
    }
}

class Node {
	int x;
	int y;
	int idx;
	Node left;
	Node right;
	
	Node(int x, int y, int idx) {
		this.x = x; this.y = y; this.idx = idx;
	}
}



