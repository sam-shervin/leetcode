class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = ""
        for i in address:
            if i == ".":
                string += "[.]"
                continue
            string += i
        return string
        