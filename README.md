# Cloudways One Click

## Overview :

The extension is a quick utility to automate the ssh process of launching a terminal and moving back and forth in copying the username, password and IP address to login into your Clouways Server terminal.

Tested On :

* OS : Linux(Ubuntu 20.0 )/64bit
* Browser : Google Chrome 

## Prerequisites :

* ### Expect Utility 
    
    The expect utility or scripting language works with scripts or programs that expect user inputs. It automates the task by providing inputs to expected outputs. Here is the expect script that we're using to automate the ssh login : 

    ```console
    #!/usr/bin/expect
    spawn ssh -o StrictHostKeyChecking=no user@server_ip
    expect "password"
    send "password"
    send "\r"
    interact
    ```
    Inorder for it to execute we need it installed. You may use the following command to install :
    ```console
    $  sudo apt-get install expect
    ```
* ### Python3

    The expect script is executed here by using a Python program that we will refer to as the host program and which listens for data from the extension and than adds the necessary data to the script before executing it in a bash shell. The host program currently requires Python3 and isn't backwards compatible. You may use the following command to install if not already:
    ```console  
    $  sudo apt-get install python3
    ```
## Installation Steps :

To get an overview of the files and science behind the extension you may refer to the doc here : 

https://developer.chrome.com/extensions/overview

* ### Loading the Extension : 

    To install the extension turn on developer options by navigating to the extensions tab. You can input the following in the URL area and it'll take you there directly : 
    ```console  
    chrome://extensions/
    ``` 
    ![loading the extension](https://i.ibb.co/fGD1Lhb/2020-11-22-02-12.png)

    Use the load unpacked button to load the extension by navigating to the extension's directory i.e cw_one_click in this case.

    ![loading the extension](https://i.ibb.co/PTPbJD2/2020-11-22-08-48.png)

    


* ### Updating the Host's manifest : 

    By now you must have noticed that there are two manifests in our little set-up. 
    * The [extensions's manifest](https://github.com/mhumair/cw_one_click/blob/master/manifest.json) which contains the extension's information like the permissions and scripts to run 
    * and the other [host's manifest](https://github.com/mhumair/cw_one_click/blob/master/host/one_click.json) which provide's details about the host program that the extension will communicate too(By host we simply mean the machine the program will run on). 
    
    In-order for the extension to communicate to the host program we need to update the following : 

    * ### Update the Extension ID :

        We will include the extension's ID in the python script to allow the desired extension to interact with it. Copy the extension ID which can be found here : 

        ![Extension Details](https://i.ibb.co/8mxwLzF/Screenshot.png)

        And update it in the [host/one_click.json](https://github.com/mhumair/cw_one_click/blob/master/host/one_click.json) where the Extension_ID_HERE placeholder is.

    * ### Update the host path

        Similarily update the path of the python program in [host/one_click.json](https://github.com/mhumair/cw_one_click/blob/master/host/one_click.json) where the Your_PATH placeholder is. The path can be found simply by running the `$pwd` in the [cw_one_click host](https://github.com/mhumair/cw_one_click/tree/master/host) directory.  

    * ### Move the host's manifest to the NativeMessagingHosts Directory :

        The final step is to move the host's manifest to the location google-chrome extension's looks for by default if there are any relevant host program information an extension needs.

        To this simply run the command in the cw_one_click/host's directory :
        ```console
        mv ./host/one_click.json ~/.config/google-chrome/NativeMessagingHosts/
        ```

    *Awesome!*. You've just finished installing cw_one_click for automating ssh logins. Keep track of this repo for some amazing upcoming feature(s) and don't forget to star this repo :) 