import argparse
from .rest import REST


def run(args):
    api = REST(**args)
    try:
        from IPython import embed
        embed()
    except ImportError:
        import code
        code.interact(locals=locals())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url')
    parser.add_argument('--oauth', help='OAUTH_TOKEN')
    args = parser.parse_args()

    run({k: v for k, v in vars(args).items() if v is not None})


if __name__ == '__main__':
    main()
