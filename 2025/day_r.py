# input and setting up
p = [i.strip() for i in open("2025/real.txt", "r").readlines()]
dial = 50
freq = 0

# part 1
# for i in p:
#     match i[0]:
#         case "R":
#             dial = (dial + int(i[1:])) % 100
#         case "L":
#             dial = (dial - int(i[1:])) % 100
#     if dial == 0:
#         freq += 1
# print(freq)

# part 2 (had to set up again cuz no functions welp)
dial = 50
freq = 0
for i in p:
    match i[0]:
        case "L":
            if (dial - int(i[1:]) % 100) <= 0 and dial != 0:
                freq += 1  
            print((dial - int(i[1:]) % 100))
            dial = (dial - int(i[1:])) % 100  
            freq += int(i[1:]) // 100  # full rotations
            print(dial, freq)
        case "R":
            if (dial + int(i[1:]) % 100) >= 100:
                freq += 1  
            print((dial + int(i[1:]) % 100))
            dial = (dial + int(i[1:])) % 100
            freq += int(i[1:]) // 100  # full rotations

            print(dial, freq)
print(freq)