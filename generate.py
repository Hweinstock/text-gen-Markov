from args import get_args
from reader import read_file
from use_model import generate_random_text

def main():
    args = get_args()
    learning_text = read_file(args.learn_file)
    print(generate_random_text(learning_text, args.k_gram, args.length))

if __name__ == '__main__':

    main()
