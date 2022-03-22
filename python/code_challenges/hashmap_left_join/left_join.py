def left_join(left_hash, right_hash):
    hashtable_combine = []

    for key in left_hash:
        # Key of index
        hashtable_combine.append(key)
        # Value of key at index
        hashtable_combine.append(left_hash[key])

        if key in right_hash:
            # if identical key exists in right hash, append value to new hash table
            hashtable_combine.append(right_hash[key])
        else:
            # Append value of None if no identical key is found in right hash table
            hashtable_combine.append(None)

    return hashtable_combine
