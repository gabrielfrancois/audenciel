# Submission               
                           
This section describes the submission process step-by-step. If a part of the process stays unclear, you can check the FAQ page. 

## Simple submission process using python

1. Download the `starting_kit.zip` file

To download the files for this project, follow these steps:

 - Go on the challenge page,
 - Go the *Get started* menu,
 - Click on the *Files* tab,
 - Download the `starting_kit` file.

2. Unzip the starting_kit.zip on your local machine
 
The unzipped starting_kit directory contains the following files:

- `submission_script.py`, a python script to use/modify to generate a submission using python.
- `datasets.zip`, a ZIP file containing the differents **power usage datasets** to be analyzed.
 
3. Go to the starting kit directory and run the appropriate submission script (python)

```
cd starting_kit
python submission_script.py
```

It generates the files:

- `zip_program`, a zip file containing your code,
-` zip_results`, a zip file containing your results.

The description on how to execute `submission_script.py` is in the following section.
Another section showcases a way to execute the submission script through a docker image.


4. Next, submit either your code archive (`zip_program`) or your results archive (` zip_results`) through the *My Submission* section on the Codabench website. On the *My Submission* page, the status of your submission will progress through the following stages: *Submitting* > *Submitted* > *Running* > *Finished*.

5. Now you can try and improve performance with **your own code**

Edit the `submission_script.py` to replace the baseline method by the method of your choice, *i.e.* modify the code inside the `program` function, between the tags:

```
## 
## YOUR CODE BEGINS/ENDS HERE 
##
```	

