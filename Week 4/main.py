import hashlib
import re


def md5_hash(s):
    hash = hashlib.md5(s.encode()).hexdigest()
    for i in range(2016):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def find_keys(salt, num_keys=64):
    index = 0
    keys = []
    hash_cache = {}
    triple_pattern = re.compile(r"(.)\1\1")

    while len(keys) < num_keys:
        if index not in hash_cache:
            hash_cache[index] = md5_hash(salt + str(index))
        hash_val = hash_cache[index]

        match = triple_pattern.search(hash_val)
        if match:
            char = match.group(1)
            quint_pattern = char * 5

            for i in range(index + 1, index + 1001):
                if i not in hash_cache:
                    hash_cache[i] = md5_hash(salt + str(i))
                if quint_pattern in hash_cache[i]:
                    keys.append(index)
                    break
        index += 1

    return keys[-1]


print(find_keys('ahsbgdzn', 64))