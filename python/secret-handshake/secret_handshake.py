from typing import List
def commands(binary_str: str) -> List[str]:
    actions = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []

    # Reverse the binary string to iterate from right to left
    reversed_binary_str = binary_str[::-1]

    # Iterate through each bit in the reversed binary string
    for i in range(len(reversed_binary_str)):
        if reversed_binary_str[i] == '1':
            if i < len(actions):
                handshake.append(actions[i])

    # Check if the reverse bit is set (leftmost bit of original binary_str)
    if len(binary_str) == len(actions) + 1 and binary_str[0] == '1':
        handshake.reverse()

    return handshake
