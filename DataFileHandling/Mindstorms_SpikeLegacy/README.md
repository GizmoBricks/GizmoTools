# About
This guide provides a solution to store and manage large data files 
for use with the Mindstorms Robot Inventor Hub and Spike Prime Hub 
via their official apps.
It has been tested with the SPIKE Legacy and Mindstorms.

> [!IMPORTANT]
> This method doesn't work with Spike 3.
> [Here](https://github.com/GizmoBricks/GizmoTools/tree/main/DataFileHandling/Spike_3) 
> is a solution for Spike 3.

# Uploading Data Files to the Hub

1.	Create a Python Project with the MINDSTORMS or SPIKE Legacy apps.
2.	Delete any existing data within the Project.
3.	Input or paste your data.
4.	Select a slot and run or upload the Project. 
    ![Creating and uploading a data file](https://github.com/GizmoBricks/GizmoTools/assets/127412675/50f04bb9-b5eb-487d-be5d-3f020b1b9eea)


> [!NOTE]
> The best choice is to run the Project.
> In this case, you will know when exactly uploading is completed.
> Also, the app console returns _a SyntaxError with the full path to the uploaded data file_.
>
> SyntaxError in this case is normal and the file will be stored on the hub.
> ![]()

>[!IMPORTANT]
> If you choose to press "Upload", the app does not show any notification, when upload will be done.
> In this case the path to the uploaded file won't be shown.
> ![]()
> To verify the Stored File:
>   - Press 'Open Hub connections' and choose the 'Programs' tab. 
>   Wait until the program appears in the respective slot's line. 
>   ![]()
  
> [!CAUTION]
> Do not disconnect the hub during file uploading to avoid data loss.
>
> During the file uploading process, the hub might not respond to any actions.

> [!NOTE]
> Larger data files might take some time to upload, up to several minutes in some cases.
