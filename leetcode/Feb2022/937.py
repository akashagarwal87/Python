from curses.ascii import isalnum


class Solution:
    def reorderLogFiles(self, logs):
        logs.sort(key=self.sortedC)
        return logs
    def sortedC(self,string):
        id,strArr=string.split(" ",maxsplit=1)
        if str(strArr[1]).isnumeric():
            return (1,)
        else:
            return (0,strArr,id)
        