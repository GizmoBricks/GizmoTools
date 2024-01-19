# About
This guide provides a solution to store and manage large data files 
for use with the Mindstorms Robot Inventor Hub and Spike Prime Hub 
via their official apps.
It has been tested with the SPIKE Legacy and Mindstorms.

> [!IMPORTANT]
> This method doesn't work with Spike 3.
> [Here](https://github.com/GizmoBricks/GizmoTools/tree/main/DataFileHandling/Spike_3) 
> is a solution for Spike 3.

# Technical details

If you are interested in technical details about this solution:

# An "exploit"

If a project doesn't contain any Syntax Errors, 
it will be precompiled by the app into a MicroPython `.mpy` file 
and stored in the Hub.

A MicroPython file is a binary file. 
More importantly, as it's a pre-compiled file, its content will differ from the original file.

However, if a project contains any Syntax Errors, 
it'll be stored in the Hub as a regular Python `.py` file, essentially a text file.
Text files are easily navigable using Python.
Usually, a file with some data contains a lot of Syntax Errors from the Python perspective.

This method capitalizes on this “exploit”.

## Project Storage in the Hub

All projects reside in the `/projects/` directory, each having its own directory. 
These directories are labeled with specific digits, acting as unique IDs. All these IDs are recorded in the `/projects/.slots` file.

The full path to a project file looks like this: 
`/projects/{ID}/__init__.mpy` for SyntaxError-free files
or `/projects/{ID}/__init__.py` for files with any SyntaxErrors.

> [!IMPORTANT]
> The ID of each project changes every time you run or upload the program from the app.
> However, this ID remains unchanged if you run the program directly from the Hub.
   

# Uploading Data Files to the Hub

> [!CAUTION]
> Do not disconnect the hub during file uploading to avoid data loss.
>
> During the file uploading process, the hub might not respond to any actions.

> [!NOTE]
> Larger data files might take some time to upload, up to several minutes in some cases.

#### How to create and store a data file

1.	Create a Python Project with the MINDSTORMS or SPIKE Legacy apps.
2.	Delete any existing data within the Project.
3.	Input or paste your data.
4.	Select a slot and run or upload the Project.
    *  Now you can use the path from the third line of the SyntaxError to read data.

<details>
   
   <summary>Data creating and storing process:</summary>
   
   ![Creating and uploading a data file](https://github.com/GizmoBricks/GizmoTools/assets/127412675/50f04bb9-b5eb-487d-be5d-3f020b1b9eea)
   
</details>

> [!NOTE]
> The best choice is to run the Project.
> In this case, you will know when exactly uploading is completed.
> Also, the app console returns _a SyntaxError with the full path to the uploaded data file_.
>
> SyntaxError in this case is normal and the file will be stored on the hub.
>
> <details>
>
> <summary>Example of SyntaxError message:</summary>
>
> ![SyntaxError with the path to a data file](https://github.com/GizmoBricks/GizmoTools/assets/127412675/298d6b39-317c-49d6-a857-1ef35ddfb2ec)
>   
> `8040` is ID in this case.
> 
> </details>

>[!IMPORTANT]
> If you choose to press "Upload", the app does not show any notification, when upload will be done.
> In this case the path to the uploaded file won't be shown.
> 
> To verify the Stored File:
>   - Press 'Open Hub connections' and choose the 'Programs' tab. 
>   Wait until the program appears in the respective slot's line.
>
> <details>
>   
>  <summary>Verifying data uploading:</summary>
>
>  ![Verifying data uploading](https://github.com/GizmoBricks/GizmoTools/assets/127412675/1d721298-b699-45c5-a652-c8d5498e4ec3)
>
>  </details>

# Reading data from the uploaded file

## Basic solution

1. Create your data and store it in the Hub.
   
   Here is an example of a data file:
   https://github.com/GizmoBricks/GizmoTools/blob/8d730b13015e52b1415f72900c7f04436530aede/DataFileHandling/Mindstorms_SpikeLegacy/slot_0#L1-L3
2. Copy an ID from the SyntaxError and put it into the following code. Run the code.
   https://github.com/GizmoBricks/GizmoTools/blob/8e8aac657a37cfd664ba9a2870d7c1d6bb87e261/DataFileHandling/Mindstorms_SpikeLegacy/Basic/data_reading.py#L1-L5
4. Adapt code to your needs if necessary.

