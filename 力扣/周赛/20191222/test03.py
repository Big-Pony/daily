class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        numbers = 0
        l=len(s)
        start = -1
        end = maxSize-1
        nl=[]
        while maxSize>=minSize:
            start+=1
            end+=1
            aim=s[start:end]
            if len(set(aim))<=maxLetters:
                i=-1
                la=len(aim)-1

                while la<=l:
                    i += 1
                    la+=1
                    if  s[i:la]==aim:
                        numbers+=1
                nl.append(numbers)
                numbers=0
            if end==l-1:
                start=-1
                maxSize-=1
                end=maxSize-1
        nl.append(0)
        print(max(nl))
        return max(nl)


a=Solution()
a.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3)
s2="ffhrimojtdwnwrwsmwxxprahdofmwzzcziskfyxvlteunhyjvmexcbxlrxtcsozrxyaxppdztpzqfcnpiwzhcvyyvpnlwwkhjlctlsbboosvyabdglhzvwdtazcyrumynkhqywrmyljhkxbpnwmfkxnqpchyjckwwpiqjljynsidcccffguyqmvnubgznsjzgkublxwvdjequsguchpzcfncervajafyhyjvoqetaxkybvqgbglmcoxxapmymxmmsqpddpctymxkkztnpiqcgrsybfrqzepnteiuzkvfnnfwsjwrshjclvkvjiwfqbvprbknvxotekxskjofozxiisnomismymubikpagnvgrchynsyjmwadhqzbfssktjmdkbztodwidpwbihfguxzgrjsuksfjuxfqvmqqojoyjznvoktfbwykwhaxorlduchkefnbpgknyoodaizarigbozvsikhxhokfpedydzxlcbasrxnenxrqxgkyfncgnhmbtxnigznqaawmslxehbshmelgfxaayttbsbhvrpsehituihvleityqckpfpmcjffhhgxdprsylnjvrezjdwjrzgqbdwdctfnvibhgcpmudxnoedfgejnbctrcxcvresawrgpvmgptwnwudqfdpqiokqbujzkalfwddfpeptqhewwrlrwdabafodecuxtoxgcsbezhkoceyydjkniryftqdoveipatvfrfkhdztibywbajknxvkrcvfhgbnjxnoefgdwbekrvaalzuwypkhwhmxtnmoggsogczhemzysagznnmjiiwwyekibytqhgwfzmsqlntvakyhaaxiqvlxbhgknvdxjwecccsquqqqmrxsysfyidsbtqytgonmzyjcydyqqqmixrbrllbcbbnwvriqcrznobzippyssjypvjemvadgdcriydntlpyrmxejtdyzhzdljhbyifxewdyokbhcgkhpdjoeqexfxqwvxys"
ma2=18
mi2=2
mas2=22
a.maxFreq(s2,ma2,mi2,mas2)
