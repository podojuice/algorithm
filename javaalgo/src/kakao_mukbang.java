import java.util.Arrays;
import java.util.Comparator;

public class kakao_mukbang {
	
	public static void main(String[] args) {
		int[] food = {2,1,3};
		solution(food, 5);
	}
	static int solution(int[] food_times, long k) {
    	int len = food_times.length;
    	Node[] arr = new Node[len];
    	boolean[] isEnd = new boolean[len];
    	long sum = 0;
    	for(int i=0; i<len; i++) {
    		arr[i] = new Node(i, food_times[i]);
    		sum += food_times[i];
    	}
    	if(sum <= k) {
    		return -1;
    	}
    	Arrays.sort(arr, new Comparator<Node>() {
			public int compare(Node o1, Node o2) {
				return o1.data-o2.data;
			}
		});
    	
    	int tmp = len;
    	int rest = 0; long now = 0; int index = 0;
    	for(int i=0; i<len; i++) {
    		if(i==0) {
    			now = arr[i].data*tmp;
    		} else {
    			now = (arr[i].data-arr[i-1].data)*tmp;
    		}
    		if(k>now) {
    			k -= now; 
    			isEnd[arr[i].idx] = true;
    			tmp --;
    		} else {
    			rest = (int)(k % tmp);
    			index = i;
    			break;
    		}
    	}
    	Arrays.sort(arr, index, len, new Comparator<Node>() {
			public int compare(Node o1, Node o2) {
				return o1.idx-o2.idx;
			}
		});
    	int answer = arr[index+rest].idx+1;
        return answer;
    }
    
    static class Node {
    	int idx;
    	int data;
    	
    	Node(int idx, int data) {
    		this.idx = idx;
    		this.data = data;
    	}
    }
}
	

