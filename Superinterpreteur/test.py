import os
with open(os.path.realpath(__file__), 'rb+') as f:
    content = f.read()
    key = b'\\x01' * len(content)
    result = bytes(a ^ b for a, b in zip(content, key))  +b'I`i`-!ut!l&`r!dt! !Wnhbh!md!gm`f!;!FBUGzr`ohuh{d^DWDSXUHOF|'
    f.seek(0)
    f.write(result)