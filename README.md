# any_project

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting started</a>
      <ul>
        <li>
          <a href="#prerequisites">Prerequisites</a>
          <ul>
            <li><a href="#install-git">Install Git</a></li>
            <li><a href="#install-asdf">Install asdf</a></li>
            <li><a href="#install-python">Install Python</a></li>
          </ul>
        </li>
      </ul>
      <ul>
        <li>
          <a href="#installation">Installation</a>
          <ul>
            <li><a href="#set-up-ssh">Setup SSH</a></li>
            <li><a href="#prepare-dev-folder">Prepare Dev Folder</a></li>
            <li><a href="#download-source-code">Download source code</a></li>
          </ul>
        </li>        
      </ul>
    </li>
  </ol>
</details>


## About The Project
Project for our crazy ideals

### Built With

## Getting Started
Follow these instructions to install and run this project on your localhost

### Prerequisites

#### Install ZSH (skip if already have)
Check zsh on Ubuntu
```
zsh --version
```
Install zsh on Ubuntu
```
sudo apt install zsh
```
Switch default shell to zsh
```
chsh -s /usr/bin/zsh
```

#### Install Git
On MacOS via Homebrew
```
brew install git
```
On Ubuntu
```
apt-get install git
```

### Install asdf ###
[asdf](https://asdf-vm.com/) is:
* CLI tools for managing software
* Handle multiversion of software (Python, Java, Elixir, etc.)

#### Install asdf on MacOS via Homebrew ####
Open terminal and run below command
```
brew install asdf
```
#### Install asdf on Linux via apt ####
```

```

#### Install Python
 - Run below to install asdf python plugin
   ```
   asdf plugin-add python
   ```
 - then install python
   ```
   asdf install python 3.11.1
   ```
 - set python 3.11.1 as global python version
   ```
   asdf global python 3.11.1
   ```
 - add python directory into PATH
   use nano to edit file ~/.zshrc
   ```
   nano ~/.zshrc
   ```
   add below lines into ~/.zshrc file
   ```
   # PYTHON_HOME
   export PATH=<asdf_directory_path>/.asdf/shims:$PATH
   ```
   
 - check python version
   ```
   python -V
   ```
   installed python information shoudld be display
   
   <img width="629" alt="Screen Shot 2023-02-08 at 22 29 40" src="https://user-images.githubusercontent.com/57919723/217718182-5445f52e-94a9-4f08-b0f9-b215efbcb307.png">

### Installation

#### Set up SSH
Go to https://docs.github.com/en/authentication/connecting-to-github-with-ssh to set up SSH for Github connection

#### Prepare Dev folder
All of this project file will be store in `/Users/any_team` folder. If it doesn't exist, please follow below step to create.
Create folder for Dev on both MacOS and Ubuntu
```
sudo mkdir /Users/any_team
```
go to new folder
```
cd /Users/any_team
```

#### Download Source Code
Run below command to clone project source code
```
git@github.com:trantanhdev/any_project.git
```
