# cw_one_click

## Prerequisites :

* ### Expect Utility 

    
    The expect utility or scripting language works with scripts that expect user inputs. It automates the task by providing inputs to expected outputs. Here is the expect script that we're using to automate the ssh login : 

    ```console
    #!/usr/bin/expect
    spawn ssh -o StrictHostKeyChecking=no user@server_ip
    expect "password"
    send "password"
    send "\r"
    interact
    ```
    Inorder for it to successfully trigger we need it installed. You may use the following command to install :
    ```console
    $  sudo apt-get install expect
    ```
* ### Python3

    The expect script is executed here by using a Python program that listens for data from the extension and than adds the necessary data to the script before executing it in a bash shell. The python program currently requires Python3 and isn't backwards compatible. You may use the following command to install :
    ```console  
    $  sudo apt-get install python3
    ```
## Installation Steps :

To get an overview of the files and science behind the extension you may refer to the doc here : https://developer.chrome.com/extensions/overview

* ### Loading the Extension : 

    To install the extension simply navigate to the extensions tab : chrome://extensions/ and turn on developer options. Than use the load unpacked button to load the extension by navigating to the extension directory i.e cw_one_click in this case.

    ![loading the extension](https://i.ibb.co/fGD1Lhb/2020-11-22-02-12.png)


* ### Updating the Host's manifest : 

    Inorder for the extension communicates to the python program we need to update the following : 

* ### Update the Extension ID

    Copy the extension ID which can be found here : 

    ![Extension Details](https://i.ibb.co/fGD1Lhb/2020-11-22-02-12.png)

    And update it in the host/one_click.json where the Extension_ID_HERE placeholder is.

* ### Update the host path

    Similarily update the path of the python program in host/one_click.json where the Your_PATH placeholder is. The path can be found simply by running the $pwd in the cw_one_click host directory.  

* ### Move the manifest to the NativeMessagingHosts Directory :

    The final step is to move the host's manifest to the location google-chrome extension's looks for by default if there are any relevant host program information an extension needs.

    To this simply run the command in the cw_one_click/host's directory :
    ```console
    mv ./host/one_click.json ~/.config/google-chrome/NativeMessagingHosts/
    ```

Awesome!. You've just finished installing the cw_one_click for automating ssh logins. Keep track of this repo for some amazing upcoming feature and don't forget to star this repo :) 