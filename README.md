# Tracy's-Mask
Use a mask layer to clean up procreate artwork. 
Have you ever drawn something like this?
![image](example/Original1.png)
Or this?
![image](example/Original2.png)
Try Tracy's Mask hotfix. 
# Section 1: Preprocess
1. Simply draw a mask like this:
![image](example/Mask.png)
2. Here's what the drawing looks like with the mask on:
![image](example/WithMask.png)
3. Now export all the layers in Procreate. 
![image](example/ExportLayers.jpeg)

# Section 2: Python-Process
## Method 1: With a PC with Python installed. 
0. One-time setup the Python environment with the required modules installed. 
    ```
    git clone https://github.com/iBobbyTS/Tracys-Mask.git
    cd Tracys-Mask
    python3 -m pip install -r requirements.txt
    ```
1. Store all the layers in a folder, rename the mask layer to `mask.png`. 
![image](example/Layers.png)
2. In terminal or cmd run:
    ```
    python3 main.py path/to/the/folder/with/the/layers
    ```
    For example:
    ```
    python3 main.py /Users/ibobby/Downloads/Future\ Girl
    ```
3. Done!
![image](example/Done.png)
![image](example/Results.png)
## Method 2: With an iPad or an iPhone.
