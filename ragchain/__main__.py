from .injustor import injustor

def main():
    _injustor = injustor.Injustor()
    print(_injustor.type_checker.check("assets/green_lantern_lore.txt"))

if __name__ == "__main__":
    main()
