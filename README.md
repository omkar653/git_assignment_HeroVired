-- Graded Assignment on Git and GitHub --

Q1 steps : 

Step 1 - Created a repository name: git_assignment_HeroVired

Step 2 - Created a ‘dev’ branch and added the provided python code into the branch as 'CalculatorPlus.py'.

Step 3 - Merged 'dev' branch with the 'main' branch and made a release of 'Version 1' of the ‘calculator plus app’.

Step 4 - Added Prerna (classmate) as collaborator.

Step 5 - Implemented a feature by creating a new branch called ‘feature/sqrt’ and added the ‘sqrt’ code to it.

Step 6 - As per the instruction in step g, switched back to dev branch and then added divide by 0 code fix, while keeping the 'feature/sqrt' branch up-to-date.

Step 7 - After this, ensured the code is running properly for both previous implementations and the newly added feature, along with bug fix, created a pull request for main branch.

Step 8 - Asked Prerna, as a code reviewer to review the PR and then merge into main.

Step 9 - After PR merge, merged the 'feature/sqrt' branch to 'dev'.

Step 10 - Did the final testing of code in 'dev' branch and raised the PR for main, as 'Version 2' release.



Q2 steps :

Step 1 - Downloaded and installed git lfs through the git bash (git lfs install) and verified version (git lfs version).

Step 2 - Created a branch 'LFS' from 'main'

Step 3 - From the file explorer, placed a zip file in the same location as git repo.

Step 4 - checked git status and then tracked the lfs file using command - git lfs track "*.zip".

Step 5 - commited the file and then pushed to the LFS branch.

Step 6 - merged the final changes to 'main'


Q3 steps : 

Step 1 - Created a branch 'feature/circle-area' from 'dev' and switched into it.

Step 2 - created a python file 'geometry-calculator.py' and pasted the provided code.

Step 3 - added the changes and then stashed them using 'git stash' command.

Step 4 - switched back to 'dev' and created another branch 'feature/rectangle-area' and switched into it.

Step 5 - performed similar steps as 2 and 3.

Step 6 - now switched back to branch 'feature/circle-area' and retrieved the stashed changes using 'git stash pop'.

Step 7 - completed the circle area implementation and commited and pushed the changes.

Step 8 - switched back to branch 'feature/rectangle-area' and again retrieved the stashed changes using 'git stash pop'.

Step 9 - completed the rectangle area implementation and commited and pushed the changes.

Step 10 - created two PRs, one for 'feature/circle-area' to 'dev' merge and another for 'feature/rectangle-area' to 'dev' merge.

Step 11 - Got the PRs reviewed and approved from classmate (Prerna) and merged the changes to 'dev'.

Step 12 - Finally merged the changes to 'main'.