import fire


def health():
    print('OK!')


def main():
    fire.Fire({
        'health': lambda: health,
    })


if __name__ == '__main__':
    main()
