#my python toolbox module
#
#this mainly consists of splitio testing utilities
#
#created by agustinona

def randomAlphanumKey(len):
    import random, string
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
    return x