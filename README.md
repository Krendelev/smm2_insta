# Instagram Sweepstakes

Returns list of users qualified to enter your [Instagram](https://instagram.com) sweepstakes according to a set of predefined rules.

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Put your [Instagram](https://instagram.com) `login` and `password` into the `.env` file in the working directory like this:

```bash
INSTA_LOGIN=myaccount
INSTA_PASS=mypassword
```

Run `main.py` with link to your post as an argument.

```bash
$ python main.py https://www.instagram.com/p/B15-qRooKYe/
99marvik99, _sadseal__, peryzt, yarik24_mr, tiiny.yy, iiamgerman_, 06.05m
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
