import hashlib
from datetime import datetime
from random import randint
import sys
sys.setrecursionlimit(100000)

def hasher(var):
    res = hashlib.sha256(var.encode('utf-8'))
    res = res.hexdigest()
    return res


def proof_frinder(stroka, dif):
    pam = hasher(stroka)
    count = 0
    i = True
    while (i):
        if (pam.startswith(dif)):
            i = False
            return count - 1
        else:
            pam = hasher(stroka + str(count))
            count += 1

def min(block,dif):

    res = block.mine(block.index,block.proof,block.phash,block.hash,dif)

    print("-----------------------------------------")
    print(block.index)
    print("Time of creation" , block.time)
    print(block.proof)
    print(block.phash)
    print(block.hash)
    return min(res,dif)

class Blockchain():

    def __init__(self, index_of_block: int, time: int, proofow: int, pr_hash, hash):
        self.block = {"Index": index_of_block,
                      "Time": time,
                      "Proof of work": proofow,
                      "Previous hash": pr_hash,
                      "Hash": hash
                      }
        self.index = index_of_block
        self.time = time
        self.proof = proofow
        self.phash = pr_hash
        self.hash = hash

    def mine(self, index, proofow, pr_hash, hash, dif):
        index = self.index
        index += 1
        time = datetime.now()
        pr_hash = self.hash
        buf = pr_hash
        proofow = proof_frinder(buf, dif)
        hash = hasher(pr_hash + str(proofow))
        return Blockchain(index, time, proofow, pr_hash, hash)

time_of_start = datetime.now()
print("time of start ",time_of_start)
dif = input("Choose numbers of 0 with block should starts with: ")
time = datetime.now()
proof = 0
pr_hash = str(randint(0, 2147483648))
print(pr_hash)

var1 = proof_frinder(pr_hash,dif)
var2 = hasher(pr_hash+str(var1))

main_block = Blockchain(1, time, proof, pr_hash, var2)

while(True):
    print(min(main_block,dif))