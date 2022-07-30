# import main7
hello="hello all"
def print_msg(text):
    print(f"messag {text}")

def main():
    print_msg(hello)

if __name__=="__main__":
    print("main")
else:
    print(f"This is module:{__name__}")
# print(main.test())