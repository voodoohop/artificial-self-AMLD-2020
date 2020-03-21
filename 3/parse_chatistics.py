from argparse import ArgumentParser

from utils import read_conversation_data


def main(data_path, out_path):
    df = read_conversation_data(data_path)
    df = df[df.text != ""]
    with open(out_path, "w") as f:
        for i, col in df.iterrows():
            f.write(col["text"] + "\t")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        dest="data_path", type=str, help="Path to chatistics data",
    )
    parser.add_argument(
        dest="out_path", type=str, help="Path to output raw data",
    )
    args = parser.parse_args()
    main(args.data_path, args.out_path)
