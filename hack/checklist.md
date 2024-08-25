# Checklist

![Checklist - all issues must solved before pulishing](/images/11.png)

Have you ever encountered this situation?

Here's a quick solution that allows you to leave your block "unconnected":

The concept is similar to Python's "if True:".

![2 no connected block](/images/12.png)

We simply create an "**if else**" logic that put anywhere, and set the condition to something that's always true.

"**sys.user_id**" is a good target. We can set it as "**is not empty**", which functions like python "if True".

Next, we connect the "else" part to the blocks that you do not want is run, but also do not want to delete it.

The final result looks like this:

![fixed](/images/13.png)

No more checklists\! The block under "else" will never execute.  
Most importantly, you can now click the publish button\!
