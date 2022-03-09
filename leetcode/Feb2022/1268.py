class Solution:
    def suggestedProducts(self, products, searchWord: str):
        self.trie={}
        for product in products:
            self.addword(product)
        searchStr=""
        result=[]
        for ch in searchWord:
            searchStr+=ch
            result.append(self.searchTrie(searchStr,3))
        return result
    def addword(self,word):
        cur=self.trie
        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True
    def searchTrie(self,sreachStr,maxWords):
        cur=self.trie
        for ch in sreachStr:
            if ch in cur:
                cur= cur[ch]
            else:
                return []
        return self.dfs(cur,sreachStr,0,[])
    def dfs(self,trie,string,count,res):
        print(count,string)
        if len(res) <3:
            if '*' in trie:
                res.append(string)
                count+=1
            for c in sorted(trie.keys()):
                if c != '*':
                    self.dfs(trie[c],string+c,count,res)
        return res
print(Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))