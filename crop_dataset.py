def copy_first_n_lines(input_file, output_file, n=10000):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for _ in range(n):
                line = infile.readline()
                if not line:
                    break
                outfile.write(line)

# Usage:
copy_first_n_lines('./eth_transactions.csv', 'eth_transactions_cropped.csv')