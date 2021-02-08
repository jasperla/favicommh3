# Faviconmmh3

Calculate the MurmurHash3 of a favicon.

When researching the usage of a particular web application it's often useful to run a [Shodan.io](https://shodan.io/) search. This tool will calculate the [MurmurHash3](https://en.wikipedia.org/wiki/MurmurHash) value of a *favicon* file. This value can subsequently be used in an `http.favicon.hash` query.

## Installation and usage

```
pip install -r requirements.txt
export FLASK_APP=app
flask run
```

## ToDo

- help with styling the pages is very much welcomed!

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Jasper Lievisse Adriaanse - `favicommh3 <at symbol> jasper.la`

Project Link: [https://github.com/jasperla/favicommh3](https://github.com/jasperla/favicommh3)
