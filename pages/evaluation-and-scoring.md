# Evaluation and Scoring   
                           
The **global score** is used to rank the different methods and is computed from a combination of several metrics : 
  - The first criterion rewards model compactness: models under 20 MB receive a perfect size score, while larger models are penalised linearly down to zero at 40 MB.
  - The second and third criteria measure predictive performance on a public test set and a hidden private test set respectively. 
  - Each of these is a 50/50 blend of recall and inference speed, where speed is scored relative to a 60-second reference time. 
  - The final score is the average of these three components.
 
  
To see your score:

  - Go on *My Submission* menu.
  - When the status of your submission is finished, refresh the page and check your score.
  - If your are satifyed by your score, click on the green button 'add to leaderboard' to push it the leaderboard.
  - Click on the "eye" icon (Detailed Results) to get information on your method's results and performances.
  
By clicking on your submission in the submissions summary table, you will get access to:

  - details of your submission (downloaded)

    	- submitted files
    	- prediction results (ingestion output) 
     	- scoring results (scoring output) 
  
  - some execution logs
  - a submission metadata edition menu
  
Check the leaderboard in the *Results*  menu.

To compare your score with other participants, go to the challenge page and navigate to the *Leaderboard* or *Results* section. 
Here, you can see how your submission ranks.
