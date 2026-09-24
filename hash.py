import hashlib

def hash(txt):
  hash_objet = hashlib.sha256(txt.encode())
  hash_hex = hash_objet.hexdigest()
  return hash_hex


def compare_hash(hash1, hash2):
  if hash1 == hash2:
    return True
  else:
    return False