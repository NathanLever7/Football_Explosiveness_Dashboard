#Football: Explosiveness vs Consistency with Expected Goals

To view the results, follow the link: https://footballexplosivenessdashboard-bceuyhdbdmrjoqfadkzc2a.streamlit.app/

To get this outcome, I ran the .ipynb file to get the results, and then the .py file to dashboard and visualise.

For pre-requisites, refer to the Requirements.txt file. These can be installed by running pip install -r requirements.txt in the terminal.

##Player Explanation:

Not all xG is made equal.
Let's take 2 players in a match, players A and B. Let's say A has 1 shot of 1 xG, and B has 10 shots of 0.1 xG. Both have an xG of 1. However, the chances that both score 1 goal are different. A is guaranteed to score 1 goal, but B could score anywhere between 0-10 goals.
The aim of these metrics are to find which players belong to which category.

Players who take many shots, and have a high npxG per 90 tend will have high explosiveness - they have the opportunity to score many goals, and the high number of shots makes their actual goals scored variable. In contrast, players with high consistency are rewarded for both their npxG per 90, and their average chance being higher quality.
In both cases, we expect players that score highly, to score goals often. Explosive players are more likely to have greater variance in goals per game than consistent players.

##Team Explanation:

Team explosiveness orders the teams who take a lot of shots and generate high xG. They are the teams likely to score many goals in a given game, but outcome can be quite variable.
In contrast, the opposition data shows the teams that concede a lot of shots, and high xG. They are the teams likely to concede many goals in a given game, but again, how many goals can be more variable.

In terms of consistency, teams high up create a high number of good chances, they should score a less variable amount of goals than those at the top of the explosiveness rankings.
The opposition data shows teams that should have conceded a more stable amount of goals that those at the top of the explosiveness opposition metric

##Overall:
We can assess which players and teams are likely to score more/less goals, and how likely they are to be close/far away from their xG.


##Key Definitions:

xG = Expected Goals

np = Non-penalty

Sh = Shots


Contact nathanleversedge@gmail.com for more info.
