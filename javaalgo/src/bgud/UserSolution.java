package bgud;

class list {
	int db_idx, prv, nxt;
}

class trie {
	int list_idx[], link[];
	trie() {
		this.list_idx = new int[5];
		this.link = new int[128];
	}
}

class database {
	boolean isUsed;
	String data[];
	int link[];
	
	database() {
		this.data = new String[5];
		this.link = new int[5];
	}
	
}



class UserSolution {
	static int list_cnt, trie_cnt, db_cnt, enc[], enc_cnt;
	static list[] lst;
	static trie root;
	static database[] db;
	static trie[] tries;

	void InitDB()
	{
		lst = new list[250010];
		root = new trie();
		tries = new trie[1000010];
		db = new database[50010];
		enc = new int[128];
//		for(int i=0; i<38; ++i) if(root.link[i] != 0) root.link[i] = 0;
		list_cnt = 0;
		trie_cnt = 0;
		db_cnt = 0;
		enc_cnt = 0;
		enc['@'] = enc_cnt++;
		enc['.'] = enc_cnt++;
		for(int i='0'; i<='9'; ++i) enc[i] = enc_cnt++;
		for(int i='a'; i<='z'; ++i) enc[i] = enc_cnt++;
	}

	void Add(String name, String number, String birthday, String email, String memo)
	{
		int len; 
		int db_idx = 0;
		String[] strs = {name, number, birthday, email, memo};
		trie now;
		
		if(db_cnt<50000) db_idx = ++db_cnt;
		else for(db_idx = 1; db_idx <=50000; ++db_idx) if(!db[db_idx].isUsed) break;
		db[db_idx].isUsed = true;
		for(int i =0; i<5; ++i) db[db_idx].data[i] = strs[i];
		// reverse(email);
		for(int i=0; i<5; ++i) {
			len = strs[i].length();
			now = root;
			for(int j=0; j<len; ++j) {
				if(now == null) {
					now = new trie();
					now.link[enc[strs[i].charAt(j)]] = ++trie_cnt;
				}
				now = tries[now.link[enc[strs[i].charAt(j)]]];
			}
			lst[++list_cnt] = new list();
			lst[list_cnt].db_idx = db_idx;
			lst[list_cnt].prv = 0;
			lst[list_cnt].nxt = now.list_idx[i];
			if(now.list_idx[i] != 0) lst[now.list_idx[i]].prv = list_cnt;
			now.list_idx[i] = list_cnt;
			db[db_idx].link[i] = now;
		}
		
	}

	int Delete(int field, String str)
	{
		return 1;
	}

	int Change(int field, String str, int changefield, String changestr)
	{
		return 1;
	}

	Solution.Result Search(int field, String str, int returnfield)
	{
		Solution.Result result = new Solution.Result();

		return result;
	}
}
