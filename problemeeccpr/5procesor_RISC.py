n = int(input())

registru = {}
for i in range(0,15):
    registru[str(i)] = 0

for i in range(n):
    cmd = input()

    if cmd.split()[0] == "lconst":
        registru[cmd.split()[1]] = int(cmd.split()[2])

    if cmd.split()[0] == "add":
        registru[cmd.split()[1]] = registru[cmd.split()[2]] + registru[cmd.split()[3]]

    if cmd.split()[0] == "mul":
        registru[cmd.split()[1]] = registru[cmd.split()[2]] * registru[cmd.split()[3]]

    if cmd.split()[0] == "div":
        if registru[cmd.split()[3]] == 0:
            print("Exception: line", i+1)
            exit()
        else:
            registru[cmd.split()[1]] = registru[cmd.split()[2]] / registru[cmd.split()[3]]

    if cmd.split()[0] == "print":
        print(int(registru[cmd.split()[1]]))
