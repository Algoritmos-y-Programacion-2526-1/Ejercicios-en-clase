

def exponential(base, exp, aux):
    if aux == exp:
        return base
    return base * exponential(base, exp, aux + 1)
    # 2 * exponential(2,8,2) // 2 * 2 * 2 * 2 * 2 * 2 *  2 * 2
    # 2 * exponential(2,8,3) // 2 * 2 * 2 * 2 * 2 *  2 * 2
    # 2 * exponential(2,8,4) // 2 * 2 * 2 * 2 *  2 * 2
    # 2 * exponential(2,8,5) // 2 * 2 * 2 *  2 * 2
    # 2 * exponential(2,8,6) // 2 * 2 *  2 * 2
    # 2 * exponential(2,8,7) // 2 *  2 * 2
    # 2 * exponential(2,8,8) // 2 * 2
    # 2                      // 2

def main():
    base = int(input("Base:"))
    exp = int(input("Exp:"))
    print(exponential(base, exp, 1))

main()