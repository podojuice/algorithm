import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class kakao2 {
	static int[] stage;
	static int[] succ;
	static int[] num;
	static racio[] fail;
	
	public int[] solution(int N, int[] stages) {
        
        stage = new int[N+2];
        succ = new int[N+2];
        num = new int[N+2];
        fail = new racio[N+1];
        for(int i=0; i<stages.length; i++) {
        	stage[stages[i]] ++;
        }
        for(int i=1; i<=N+1; i++) {
        	if(stage[i]>0) {
        		for(int j=1; j<i; j++) {
        			succ[j] += stage[i];
        			num[j] += stage[i];
        		}
        		num[i] += stage[i];
        	}
        }
        for(int i=1; i<=N; i++) {
        	if(num[i] ==0) {
        		fail[i] = new racio(i, 0f);
        	} else {
        		fail[i] = new racio(i, 1-(float)succ[i]/(float)num[i]);
        	}
        	
        }
        System.out.println(Arrays.toString(fail));
        Arrays.sort(fail, new Comparator<racio>() {
			@Override
			public int compare(racio o1, racio o2) {
				if(o1.data==o2.data) {
					return o1.idx-o2.idx;
				} else {
					if(o1.data >o2.data) {
						return 1;
					}
					return -1;
				}
			}
		});
        
        
        int[] answer = {};
        return answer;
    }
	
	static class racio {
		int idx;
		float data;
		
		racio(int idx, float data) {
			this.idx = idx; this.data = data;
		}
	}
}
