from .injustor import injustor

def main():
    _injustor = injustor.Injustor()
    print(_injustor._check_type("assets/green_lantern_lore.txt"))


if __name__ == "__main__":
    main()
