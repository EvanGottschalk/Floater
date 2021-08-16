[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EvanGottschalk/Floater">
    <img src="logo.png" alt="Logo" width="151" height="80">
  </a>

  <h3 align="center">Floater</h3>

  <p align="center">
    A fun, fast platformer-puzzle game
    <br />
    <a href="https://github.com/EvanGottschalk/Floater"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EvanGottschalk/Floater">View Demo</a>
    ·
    <a href="https://github.com/EvanGottschalk/Floater/issues">Report Bug</a>
    ·
    <a href="https://github.com/EvanGottschalk/Floater/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

One day in college, I was thinking about Mario and the many, many other platformer games, and pondering what could be done to make a platformer that's unique and innovative. I soon stumbled upon a fun twist on traditional platformer games - what if, after your character jumps, they *stay in the air*? I immediately thought I was on to something, but lamented that the game would require a second "descend" button in addition to the "jump" button. One of the biggest appeals of traditional platformers is their efficiency of only needing 1 button (“jump”) to play.

After a brief period of despair, I had a breakthrough: if your character is already on the ground, then they *can't descend*. Similarly, if your character is not on the ground, then they *can't jump*. Therefore, since both situations ("standing" and "floating") and both actions ("jumping" and "descending") are mutually exclusive, a player will never need both options available. They would only need access to the action that's physically possible in their situation. This meant I was back in business: instead of needing 2 buttons, I could use 1 button that always executes the appropriate action based on your character's situation.

And thus, `Floater` was born. While I have not worked on it in a while, it's one of my favorite Python projects, and I look forward to working on it more in the future.

<br />
<p align="center">
  <a href="https://github.com/EvanGottschalk/Floater">
    <img src="screenshots/screenshot_level6.PNG" alt="screenshot_level6" width="550">
  </a>
</p>

### Built With

`Python`

`tkinter`


<!-- GETTING STARTED -->
## Getting Started

Playing `Floater` is pretty simple. All you need is `Python` and the files in the repository.

### Prerequisites

`Floater` should work with any installation of `Python 2` or `Python 3`. Please let me know if you have any issues.

### Installation

1. Download the contents of the `Floater` repository and put them in a folder together.

2. Congratulations, you're done! You can now play `Floater` by running `FloaterCanvas.py`


<!-- USAGE EXAMPLES -->
## Usage

You are the **Floater**! Your goal in each level is to reach the green portal.

Use the left and right directional arrows to move around.

Use spacebar to jump and float, and again to fall.

Reach the portal and press the up-arrow to enter it!

Good luck!


<!-- ROADMAP -->
## Roadmap

I originally wrote this program in 2011 while still at SUNY Binghamton.

See the [open issues](https://github.com/EvanGottschalk/Floater/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU GPL-3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Evan Gottschalk - [@Fort1Evan](https://twitter.com/Fort1Evan) - magnus5557@gmail.com

Project Link: [https://github.com/EvanGottschalk/Floater](https://github.com/EvanGottschalk/Floater)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Thinking about contributing to this project? Please do! Your Github username will then appear here.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EvanGottschalk/Floater.svg?style=for-the-badge
[contributors-url]: https://github.com/EvanGottschalk/Floater/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EvanGottschalk/Floater.svg?style=for-the-badge
[forks-url]: https://github.com/EvanGottschalk/Floater/network/members
[stars-shield]: https://img.shields.io/github/stars/EvanGottschalk/Floater.svg?style=for-the-badge
[stars-url]: https://github.com/EvanGottschalk/Floater/stargazers
[issues-shield]: https://img.shields.io/github/issues/EvanGottschalk/Floater.svg?style=for-the-badge
[issues-url]: https://github.com/EvanGottschalk/Floater/issues
[license-shield]: https://img.shields.io/github/license/EvanGottschalk/Floater.svg?style=for-the-badge
[license-url]: https://github.com/EvanGottschalk/Floater/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/EvanGottschalk
