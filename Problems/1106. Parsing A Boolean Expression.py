class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        
        for each in expression:
            if each == ',':
                continue
            if each == 't':
                st.append(True)
            elif each == 'f':
                st.append(False)
            elif each != ')':
                st.append(each)
            else:
                args = []
                while True:
                    curr = st.pop()
                    if curr == True:
                        args.append(True)
                    elif curr == False:
                        args.append(False)
                    elif curr == '(':
                        op = st.pop()
                        st.append(self.cal(op, args))
                        break
        return st[0]
    
    
    def cal(self, op, args):
        if op == '!':
            return not args[0]
        if op == '&':
            return all(args)
        return any(args)
