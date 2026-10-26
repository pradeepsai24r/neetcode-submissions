class Solution:
    """
    s ---> CODE --> bool
    inputs:
        1. "" --> False
        2. ({[]}) --> true
        3. ({[]) --> F
        4. (){}[] --> T
        5. ({)} --> F
        6. ( --> F
        7. } --> F
    """
    def isValid(self, s: str) -> bool:
        match_table = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        if not s or (len([ch for ch in s if ch in match_table.values()]) == len(s)) or (len(s) % 2 != 0):
            return False
        
        stack = []
        
        for ch in s:
            if ch in match_table:
                stack.append(ch)
            else:
                if stack:
                    if match_table[stack.pop()] != ch :
                        return False
        return len(stack) == 0

        

