[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.styvio.com">
    <img src="images/blackLogo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Contra AI Engine</h3>

  <p align="center">
    A lightweight, production ready Tensorflow alternative developed by Styvio
    <br />
    <a href="https://www.styvio.com"><strong>styvio.com »</strong></a>
    <br />
    <br />
    <a href="#get-started">How to Use</a>
    ·
    <a href="https://github.com/styvio/Contra/issues">Report Bug</a>
    ·
    <a href="https://github.com/styvio/Contra/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Contra</a>
      <ul>
        <li><a href="#what">What is Contra?</a></li>
        <li><a href="#why">Why does Contra exist?</a></li>
        <li><a href="#how">How can I use Contra?</a></li>
      </ul>
    </li>
    <li>
      <a href="#get-started">Getting Started</a>
      <ul>
        <li><a href="#python-installation">Installation</a></li>
        <li><a href="#quickstart">Quickstart</a></li>
      </ul>
    </li>
    <li><a href="">PyPi Module Page</a></li>
    <li><a href="https://github.com/styvio/Contra/blob/main/LICENSE.txt">License</a></li>
    <li><a href = "https://twitter.com/Styvioapp">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div id="about-the-project"></div>

Welcome to Contra, a fully open source AI engine developed by Styvio.  Contra is a lightweight, production ready alternative to Tensorflow.  Contra is written fully in Python and built to solve complex problems with AI.  Contra is built specifically to solve time series prediction problems, server or client side.

<div id="what"></div>

### What is Contra?

Contra is a collections of functions that allow you to solve complex time series problems with AI.  If you have used or built or used prediction algorithms before, you will fully understand what is going on under the hood here.  Contra is based on the simple KNN algorithm, but with one major modification.  Instead of averaging the closest data points, the prediction is based on a linear combination of the sum of all other previous outcomes, and their distance to the requested prediction in terms of their step function.

<div id="why"></div>

### Why does Contra exist?

Other AI engines or libraries can sometimes take minutes to run, and produce weights files that are far to large to run directly on a production website.  It is frusterating having to perform complex calculations off-server and then to sending the results over to a database via an API.  It is equally frusterating having weights files that are over 0.5 GB large.  These challenges make libraries like Tensorflow useless in solving complex problems fast.  Using tensorflow for time series prediction is like attatching a V8 engine to a lawn mower.  We have become far too farmiliar with these challenges, and built Contra to erase this headache.

<div id="how"></div>

### How can I use Contra?

You can use Contra anywhere you need to solve a complex problem with AI.  Contra can be applied anywhere annalysis of time series data using AI prediction makes sense.   Contra comes with the MIT liscence, meaning you can use it for personal and commercial projects without worying about liscence fees, giving credit, or litigation.

<!-- GETTING STARTED -->
<div id="get-started"></div>

## Getting Started

This section provides assistance on how to install Contra, as well as a general rundown on using the module.

<div id="python-installation"></div>

### Installation

 ```
pip install Contra
```
<div id="quickstart"></div>

 ### Quickstart

Now that the Contra module is installed, it can be imported in any .py python file, wherever you normally write code.



<a href="https://www.styvio.com/">
  <img src="images/blackLogo.png" data-canonical-src="images/blackLogo.png" width="200" height="200"/>
</a>

[contributors-shield]: https://github.com/styvio/Contra.svg?style=for-the-badge
[contributors-url]: https://github.com/styvio/Contra/graphs/contributors
[forks-shield]: https://github.com/styvio/Contra.svg?style=for-the-badge
[forks-url]: https://github.com/styvio/Contra/network/members
[stars-shield]: https://github.com/styvio/Contra.svg?style=for-the-badge
[stars-url]: https://github.com/styvio/Contra/stargazers
[issues-shield]: https://github.com/styvio/Contra.svg?style=for-the-badge
[issues-url]: https://github.com/styvio/Contra/issues
[license-shield]: https://github.com/styvio/Contra.svg?style=for-the-badge
[license-url]: https://github.com/styvio/Contra/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/styvio
