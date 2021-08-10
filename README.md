
<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Morris Worm</h3>

  <p align="center">
A software package containing a TCP port scanner, a botnet to remotely interact with multiple SSH terminals and an FTP injection to replace HTML boilerplate with a harmless custom template.
  <br>
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Security and defending against hacking sound really interesting to me. I had no idea what these fields were, maybe the hacker's matrix code goes down the screen and the defenders matrix code goes up the screen? After a little reading it turns out this isn't the case.

I decided to write some software that simulates a primitive 'reconaissance' and 'attack'.

A terminal application that can scan for open ports, once found we can use the ssh terminal to interact with the machine remotely and with access we can replace a some predetermined documents with harmless HTML.

The code is primitive, so don't go expecting to see my name plastered on times square after it's used to deactivate facebook. It's more of a toe in the water to understand security and hacking.



### Python Modules

* [](Sockets)Sockets
* [](Threading)Threading
* [](Argparse)Argparse
* [](Nmap)Nmap
* [](Pexpect)Pexpect

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Most of the modules and libraries are native to python. Exceptions:

* Pexpect
  ```sh
  pip install pexpect
  ```
* Nmap
  ```sh
  https://nmap.org/download.html
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jayfranklinn/Morris-Worm/
   ```


<!-- USAGE EXAMPLES -->
## Usage

The python files operate on the command line using argparse. Argparse, details how the input should be written in the cla.

Here is the usage prompt for one of the files, followed by the error message for incorrect arguments:
```sh
usage: python3 MW_FTP.py HOST_IP[S] -r INJECT_PAGE [-f USERPASS_FILE]

MW_FTP.py: error: the following arguments are required: HOST_IP[S], -r
```

An example of an IP and port scan.
```sh
[+] Scan results for: hostXXXXXXXXXXXXXXXX
[+] 80/tcp open
        [>] HTTP/1.0 501 Not Implemented
Server: httpd
Date: Tue, 10 Aug 2021 10:32:07 GMT
Content-Type: text
[-] 200/tcp closed
[-] 100/tcp closed
[+] 81.154.128.200 tcp/80 open
[+] 81.154.128.200 tcp/100 closed
[+] 81.154.128.200 tcp/200 closed
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jay Franklin - franklin.jamie0303@gmail.com

Project Link: https://github.com/jayfranklinn/Morris-Worm/



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
