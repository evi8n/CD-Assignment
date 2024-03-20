<<<<<<< HEAD
# CD-Assignment

as
=======
# CD-Assignment

The three components of my solution that I should probably mention, are GitHub Actions, the Virtual Private Server (VPS), and SSH keys. From what I gather, GitHub Actions is the robot automating everything and coordinating deployment procedures triggered by code modifications. The VPS is where my Flask-app lives, providing the platform for everything to run. The SSH keys behave as a lock and key, allowing secure communication between GitHub and the VPS.

The main problem that I encoutered was basicaly figuring out how everything connects to everything else (gunicorn, nginx, server, github actions) and what each one's role was exactly. Another problem was making right use of the SSH keys (while figuring out where to put each one and how to use GitHub secrets) and the third problem was figuring out how to use appleboy-ssh action.

While googling everything and looking at all kinds of solutions that made sense at each time, I basically made things work through trial and error. In this process I was also able to figure out how it was all interacting. I worked going from error to error, fixing one after the other, until things started making more sense and then to my great joy, it finally worked.

This assignment was certainly the most independent one that we had to do during this whole course. I can’t deny I learned a whole bunch of new things and that even though I would have initially liked to have a bit more explanation or even step by step guidance, I am glad that I didn’t. I feel that now I am more capable of tackling challenges that might come about in a professional environment.
>>>>>>> fdfceb4ec01e4a4917ddb35bf055e466807a517f
