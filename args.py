import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f",
                        "--learn_file",
                        metavar="",
                        required=True,
                        type=str,
                        help="Path to a .txt file to build the markov chain model to emulate text.")


    parser.add_argument("-k",
                        "--k_gram",
                        metavar="",
                        default=7,
                        type=int,
                        help="""argument describing what length to group the text into for the markov model.
                        Smaller values means the model looks at looks at less characters to predict the next one,
                        whereas higher numbers look cause the model to look at more characters to predict the next one.""")

    parser.add_argument("-l",
                        "--length",
                        metavar="",
                        default=1000,
                        type=int,
                        help="how many characters the program should generate.")
    return parser


def get_args():
    parser = get_parser()
    args = parser.parse_args()

    return args
