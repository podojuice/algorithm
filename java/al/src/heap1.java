

public class heap1 {
	// ù��° ��带 ����Ű�� �ʵ�
    private Node head;
    private Node tail;
    private int size = 0;
    private class Node{
        // �����Ͱ� ����� �ʵ�
        private int[] data;
        // ���� ��带 ����Ű�� �ʵ�
        private Node next;
        public Node(int[] input) {
            this.data = input;
            this.next = null;
        }
        // ����� ������ ���� ����ؼ� Ȯ���غ� �� �ִ� ���
        public String toString(){
            return String.valueOf(this.data);
        }
    }
    public void addFirst(int[] input){
        // ��带 �����մϴ�.
        Node newNode = new Node(input);
        // ���ο� ����� ���� ���� �ص带 �����մϴ�.
        newNode.next = head;
        // ���� ���ο� ��带 �����մϴ�.
        head = newNode;
        size++;
        if(head.next == null){
            tail = head;
        }
    }
    public void addLast(int[] input){
        // ��带 �����մϴ�.
        Node newNode = new Node(input);
        // ����Ʈ�� ��尡 ���ٸ� ù��° ��带 �߰��ϴ� �޼ҵ带 ����մϴ�.
        if(size == 0){
//        	System.out.println(newNode.data[2]);11
            addFirst(input);
        } else {
            // ������ ����� ���� ���� ������ ��带 �����մϴ�.
            tail.next = newNode;
            // ������ ��带 �����մϴ�.
            tail = newNode;
            // ������Ʈ�� ������ 1 ���� ��ŵ�ϴ�.
            size++;
        }
        int tmp = size-1;
        while(tmp != 0) {
        	if(node(tmp).data[2] < node((tmp-1)/2).data[2]) {
        		swap(tmp, (tmp-1)/2);
        		tmp = (tmp-1)/2;
        	} else { break; }
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
        // ���� k�� 0�̶�� ù��° ��忡 �߰��ϴ� ���̱� ������ addFirst�� ����մϴ�.
        if(k == 0){
            addFirst(input);
        } else {
            Node temp1 = node(k-1);
            // k ��° ��带 temp2�� �����մϴ�.
            Node temp2 = temp1.next;
            // ���ο� ��带 �����մϴ�.
            Node newNode = new Node(input);
            // temp1�� ���� ���� ���ο� ��带 �����մϴ�.
            temp1.next = newNode;
            // ���ο� ����� ���� ���� temp2�� �����մϴ�.
            newNode.next = temp2;
            size++;
            // ���ο� ����� ���� ��尡 ���ٸ� ���ο� ��尡 ������ ����̱� ������ tail�� �����մϴ�.
            if(newNode.next == null){
                tail = newNode;
            }
        }
    }
    public String toString() {
        // ��尡 ���ٸ� []�� �����մϴ�.
        if(head == null){
            return "[]";
        }       
        // Ž���� �����մϴ�.
        Node temp = head;
        String str = "[";
        // ���� ��尡 ���� ������ �ݺ����� �����մϴ�.
        // ������ ���� ���� ��尡 ���� ������ �Ʒ��� ������ ������ ���� ���ܵ˴ϴ�.
        while(temp.next != null){
            str += temp.data[2] + ",";
            temp = temp.next;
        }
        // ������ ��带 ��°���� ���Խ�ŵ�ϴ�.
        str += temp.data[2];
        return str+"]";
    }
    public int[] pop(){
        int[] returnData = head.data;
        Node tmp = head.next;
        head = node(size-1);
        head.next = tmp;
        node(size-2).next = null;
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
