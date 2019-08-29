package bgud;

class record {
	record next;
	record before;
	String[] field;
	
	long s_time = System.currentTimeMillis();
	
	void set(String name, String number, String birthday, String email, String memo) {
		this.field = new String[5];
		this.field[0] = name;
		this.field[1] = number;
		this.field[2] = birthday;
		this.field[3] = email;
		this.field[4] = memo;
	}
	
}

class DB {
	record head;
	record tail;
	
	DB() {
		record tmp = new record();
		this.head = tmp;
		this.tail = tmp;
	}
	void add(String name, String number, String birthday, String email, String memo) {
		record tmp = new record();
		tmp.set(name, number, birthday, email, memo);
		tail.next = tmp;
		tmp.before = tail;
		tail = tmp;
	}
	
	
	int delete(int field, String str) {
		record tmp = this.head.next;
		int ans = 0;
		while(tmp != null) {
			if(eq(tmp.field[field], str)) {
				tmp.before.next = tmp.next;
				tmp.next.before = tmp.before;
				ans++;
			}
			
			tmp = tmp.next;
		}
		return ans;
	}
	
	int change(int field, String str, int changefield, String changestr) {
		record tmp = this.head.next;
		int ans = 0;
		while(tmp != null) {
			if(eq(tmp.field[field], str)) {
				tmp.field[changefield] = changestr;
				ans++;
			}
			tmp = tmp.next;
		}
		return ans;
	}
	
	void search(Solution.Result result, int field, String str, int returnfield) {
		result.count = 0;
		result.str = "";
		record tmp = this.head.next;
		while(tmp != null) {
			if(eq(tmp.field[field], str)) {
				result.str = tmp.field[returnfield];
				result.count ++;
			}
			tmp = tmp.next;
		}
		if(result.count != 1) result.str = "";
	}
	
	boolean eq(String a, String b) {
		
		if(a.length() != b.length()) {
			return false;
		}
		for(int i=0; i<a.length(); i++) {
			if(a.charAt(i) != b.charAt(i)) {
				return false;
			}
		}
		
		return true;
	}
}





class UserSolution {
	static DB db;
	void InitDB()
	{
		db = new DB();
	}

	void Add(String name, String number, String birthday, String email, String memo)
	{
		db.add(name, number, birthday, email, memo);
	}

	int Delete(int field, String str)
	{
		return db.delete(field, str);
	}

	int Change(int field, String str, int changefield, String changestr)
	{
		return db.change(field, str, changefield, changestr);
	}

	Solution.Result Search(int field, String str, int returnfield)
	{
		Solution.Result result = new Solution.Result();
		db.search(result, field, str, returnfield);
		return result;
	}
}
