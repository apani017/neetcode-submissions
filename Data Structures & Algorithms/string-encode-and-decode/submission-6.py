class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        length = ""
        for word in strs:
            encoded = encoded+word
            length = length+"SIXTYNINE"+str(len(word))
        length = length + "SIXTYNINE" + str(len(encoded))
        return encoded+length

    def decode(self, s: str) -> List[str]:
        splitString = s.split("SIXTYNINE")
        lengths = splitString.pop()
        encoded = splitString.pop(0)
        
        i = 0
        res = []


        for length in splitString:
            print(encoded[i:int(length)])
            res.append(encoded[i:i+int(length)])
            i = i+int(length)
        return res


#["neet","code","love","you"]
# neetcodeloveyou#4#4#4#3#15
#
