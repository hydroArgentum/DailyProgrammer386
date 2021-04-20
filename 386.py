## Global Constants.
# The difference sequences' odd sequence starts with 1.
ODD_START = 1
# The difference sequences' even sequene starts with 3.
EVEN_START = 3

## Global Variables
# Caching answers.
partition_cache = {0:1}

## Functions
# We need to find how large our sequence list needs to be based on the
# sum of the odd and even difference sequences.
def establish_d_sequences(target_number):
    # Need to keep track of the difference sequences.
    # Odd
    odd_list = [1]
    # Even
    even_list = [3]
    # Index difference.
    diff_list = []
    # Find the maximum difference that can fit into the target number.
    start_number = 1
    # DEBUG
    #final_number = 1
    # What index of the sequence we have.
    sequence_index = 0
    # The difference that is added to the tracked number.
    value_difference = 1
    while start_number <= target_number:
        # This is to preserve the final number before the target number is reached.
        # DEBUG
        #final_number = start_number
        diff_list.append(start_number)
        if sequence_index % 2 == 1:
            value_difference = even_list[(sequence_index // 2)]
            even_list.append(even_list[(sequence_index // 2)] + 2)
        else:
            value_difference = odd_list[sequence_index // 2]
            odd_list.append(odd_list[(sequence_index // 2)] + 1)
        # Iterate through the indicies.
        sequence_index += 1
        start_number += value_difference
        # DEBUG
        #print(value_difference)
        #print(start_number)
    return diff_list
    # DEBUG
    #print(final_number)
    #print(max_difference)

# Rotate the sign of the sign every two indicies (starting from index 1)
# based on the length of the intended list.
# e.g. 1, -1, -1, 1, 1, -1, etc...
def sign_rotation_list(list_length):
    # Need to keep track of the order of the signs for each recursion.
    sign_list = [1]
    index = 1
    sign = 1
    while index < list_length:
        sign_list.append(sign_list[index - 1] * sign)
        sign *= -1
        index += 1
    return sign_list

# Partition count function.
def partition_count(number):
    partition_sum = 0
    subpartition_index = 0
    subpartition_list = establish_d_sequences(number)
    subpartition_multiplier = sign_rotation_list(len(subpartition_list))
    for subpartition in subpartition_list:
        # If we're already aware of the answer, no need to repeat it.
        if (number - subpartition) in partition_cache:
            partition_sum += (partition_cache[number - subpartition] * subpartition_multiplier[subpartition_index])
            subpartition_index += 1
            continue
        partition_sum = partition_sum + (partition_count(number - subpartition) * subpartition_multiplier[subpartition_index])
        subpartition_index += 1
    partition_cache[number] = partition_sum
    return partition_sum

# DEBUG
# Print aribtrary lists and put commas.
def print_list(input_list):
    for input_item in input_list:
        print(input_item, end=", ")

# Main Code. This is where we'll call functions.
def main():
    print(partition_count(666))
    #output_list = establish_d_sequences(6)
    #print_list(odd_list)
    #print()
    #print_list(even_list)
    #print_list(output_list)
    #print()
    #print(len(output_list))

# Needed to run code. DO NOT MODIFY.
if __name__ == "__main__":
    main()

