import base64 as b64
import marshal
import zlib
import sys
import os
from cryptography.fernet import Fernet

WATERMARK = "# Deobfuscated by Rune's Devare"

def vare(x):
    return marshal.loads(zlib.decompress(b64.b32decode(b64.b64decode(x[::-1]))))

def deobfuscate_obfuscated_file(file_path):
    with open(file_path, "r", encoding="utf-8") as obfuscated_file:
        obfuscated_code = obfuscated_file.read()

    mikey = obfuscated_code.split('__mikey__="')[1].split('"')[0]
    mydata = obfuscated_code.split('mydata="')[1].split('"')[0]

    mikey = Fernet(b64.b64decode(mikey))
    step1 = bytes.fromhex(mydata)
    step2 = mikey.decrypt(step1)
    decr = b64.b64decode(step2)
    decrdata = decr
    gotnew = b64.b32decode(decr)
    newdecr = 986689124326
    getnew = newdecr
    myb64code = b64.b64decode(gotnew)
    myb64codee = b64.b64decode(myb64code)
    code = myb64codee

    return vare(code).decode()  # Convert bytes to string

def add_watermark(deobfuscated_code):
    return f"{WATERMARK}\n\n{deobfuscated_code}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python deobfuscator.py <obfuscated_file>")
        sys.exit(1)

    obfuscated_file_path = sys.argv[1]
    if not os.path.isfile(obfuscated_file_path):
        print("Error: The specified file does not exist.")
        sys.exit(1)

    try:
        deobfuscated_code = deobfuscate_obfuscated_file(obfuscated_file_path)
        deobfuscated_code_with_watermark = add_watermark(deobfuscated_code)

        output_file_name = "Deobfuscated.py"
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            output_file.write(deobfuscated_code_with_watermark)

        print(f"Successfully Deobfuscated! File saved to: {output_file_name}")
    except Exception as e:
        print("Error: An error occurred during deobfuscation.")
        print(e)

if __name__ == "__main__":
    main()
