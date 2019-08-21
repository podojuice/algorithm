import java.util.HashSet;
import java.util.Set;

public class kakao3 {
	static String[][] input = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
	public static void main(String[] args) {
		solution(input);
	}
	
	static int col, row;
	
	
	static int solution(String[][] relation) {
        
		
        int total = 1<<relation[0].length;
        Set<Integer> keys = new HashSet<>();
        for(int i=1; i<total; ++i) {
        	boolean isMin = true;
        	for(int uniq: keys) {
        		if((uniq & i) == uniq) {
        			isMin = false;
        			break;
        		}
        	}
        	if(!isMin) continue;
        	int t = i;
        	int col = 0;
        	StringBuilder[] strs = new StringBuilder[relation.length];
        	for(int k=0; k<strs.length; ++k) {
        		strs[k] = new StringBuilder();
        	}
        	while(t>0) {
        		if((t&1) == 1) {
        			for(int k=0; k<relation.length; ++k) {
        				strs[k].append(relation[k][col]);
        			}
        		}
        		t >>= 1;
        		col++;
        	}
        	Set<String> set = new HashSet<>();
        	for(StringBuilder sb: strs) {
        		set.add(sb.toString());
        	}
        	if(set.size() == relation.length) {
        		keys.add(i);
        	}
        	
        	
        }
        System.out.println(keys.size());
        return keys.size();
    }
	
}