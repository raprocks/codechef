for _ in range(int(input())):
    N = int(input().strip())
    BOX_RED = list(map(int, input().strip().split()))
    BOX_GREEN = list(map(int, input().strip().split()))
    BOX_BLUE = list(map(int, input().strip().split()))
    matrix = [BOX_RED, BOX_GREEN, BOX_BLUE]
    # check if diagonal matrix
    if BOX_RED[0] == BOX_GREEN[1] == BOX_BLUE[2] == N:
        print(0)
        continue
    swap_count = 0

    # check swappable red to green and swap
    swappable_red_green = min(BOX_RED[1], BOX_GREEN[0])
    swap_count += swappable_red_green

    # swap
    # add red balls
    BOX_RED[0] += swappable_red_green
    # remove green balls from BOX_RED
    BOX_RED[1] -= swappable_red_green
    # add green balls to BOX_GREEN
    BOX_GREEN[1] += swappable_red_green
    # remove red balls from BOX_GREEN
    BOX_GREEN[0] -= swappable_red_green

    # check swappable green to blue and swap
    swappable_green_blue = min(BOX_GREEN[2], BOX_BLUE[1])
    swap_count += swappable_green_blue

    # swap
    # add green balls
    BOX_GREEN[1] += swappable_green_blue
    # remove blue balls from BOX_GREEN
    BOX_GREEN[2] -= swappable_green_blue
    # add blue balls to BOX_BLUE
    BOX_BLUE[2] += swappable_green_blue
    # remove green balls from BOX_BLUE
    BOX_BLUE[1] -= swappable_green_blue

    # check swappable red to blue and swap
    swappable_red_blue = min(BOX_RED[2], BOX_BLUE[0])
    swap_count += swappable_red_blue

    # swap
    # add red balls
    BOX_RED[0] += swappable_red_blue
    # remove blue balls from BOX_RED
    BOX_RED[2] -= swappable_red_blue
    # add blue balls to BOX_BLUE
    BOX_BLUE[2] += swappable_red_blue
    # remove red balls from BOX_BLUE
    BOX_BLUE[0] -= swappable_red_blue

    # now the swaps needs to have a intermediate path
    # eg., red has blue balls but blue doesnt have red, the red balls are in the green box.
    # matrix then would be
    #  RED , GREEN, BLUE
    # [[N-y, 0    , y   ] RED_BOX
    #  [y  , N-y  , 0   ] GREEN_BOX
    #  [0  , y    , N-y 0]] BLUE_BOX
    # N is total balls that should be in a box
    # y is the balls that are in the wrong box
    # Now the swaps required will be 2x to get each ball in its box
    # following above example,
    # SWAP RED -> BLUE, BLUE BALLS <-> GREEN BALLS
    # then RED -> GREEN, GREEN BALLS <-> RED BALLS
    # we dont need to swap as the count will be `2*y`
    # and as y = N - current_balls_in_red_box
    swap_count += 2*(N-BOX_RED[0])
    print(swap_count)