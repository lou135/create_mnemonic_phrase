from mnemonic import Mnemonic
def create_mnemonic():
    mnemo=Mnemonic("english")
    mnemonic=mnemo.generate(strength=128)
    return mnemonic

print(create_mnemonic())
