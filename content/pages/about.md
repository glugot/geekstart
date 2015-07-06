Title: Getting Started
Category: site-pages;
Date: Sun Jul 05 06:53:56  IST 2015
Tags: info; admin; about; introduction; getting-started;
Authors: Senthil Kumaran S (stylesen);
Summary: Getting started guide for Geek Start.

Introduction
============
Geek Start is a community blog maintained by the community members of 
GNU/Linux User groups of [TCE][1] ([GLUGOT][2]). The primary purpose of this 
blog is to introduce GLUGOT members to collaborative development. That said,
did "Geek Start" sound like "Kick Start" yes of course, we want to kick start
members of GLUGOT to get into Free Software development. Geek Start is a
community blog so anyone can contribute to this blog as long as:

  + You are subscribed to [GLUGOT mailing list][3]
  + Want to get started with Free Software development
  + Have the passion to write

The following infographic explains the workflow of Geek Start at a high level.

![Geek Start Work Flow] ({filename}/images/geekstartinfographic.jpg){:width="650px"}

[Download Geek Start Work Flow in PDF]({filename}/pdfs/geekstartinfographic.pdf)

Work Flow in Detail
===================
Prerequisite
------------

 1. Working GNU/Linux machine with internet connection
 2. 'git' version control system installed
 3. 'make' command - available via build-essentials package in Debian based
    systems
 4. pelican web site generator installed - use pip or Debian package
    python-pelican
 5. python-markdown package installed

Step 1 - Join GLUGOT
--------------------
Subscribe to GLUGOT mailing list with your email id. In order to subscribe to
the mailing list follow the instructions available in this page [https://lists.tce.edu/mailman/listinfo/glugot][3]

Step 2 - Create GitHub Account
------------------------------
GitHub is a powerful collaboration, code review, and code management platform
for software development. Create an account in GitHub by visiting
[https://github.com/][4] and "Sign up for GitHub".

Read more about GitHub [here][5]

Step 3 - Fork Geek Start
------------------------
Sign in with your new GitHub account. The Geek Start repository URL is
[https://github.com/glugot/geekstart][6], visit the same and fork the
repository. To know more on how to fork a GitHub repository see
[https://help.github.com/articles/fork-a-repo/][7]

Step 4 - Clone your Fork
------------------------
Clone your forked Geek Start repository to your local filesystem. To know more
about cloning a repository see
[https://help.github.com/articles/cloning-a-repository/][8]

*NOTE: Pay attention here, do not clone the main Geek Start repository, but clone the forked (See Step 3 above) Geek Start repository.*

Step 5 - Add Article
--------------------
As mentioned previously, Geek Start is a community blog where anyone, who is a
member of GLUGOT can add their articles which will go through a review process
and gets added to [http://geekstart.tce.edu/][9]

 1. Think about an interesting article
 2. In your Geek Start local cloned folder, look for *contents* folder
 3. Create a file with extension *.md* where you can write your article
 4. We use markdown syntax for the article, to know more about markdown see 
    [https://help.github.com/articles/markdown-basics/][10]

*NOTE: Feel free to use any text editor of your choice to edit your article*

Step 6 - Preview Article
------------------------
Once you are done with editing your article, you can preview it by issuing the 
following command in your local clone of Geek Start repository:

          $ make html

The above command will create the html files along with the article you added 
in the *output* folder in the current directory. Use a web browser to view the 
website, for example:

         $ firefox /home/stylesen/geekstart/output/index.html

The article which you added should appear in the web browser. You can make 
sure if the alignment, look and feel are good.

Step 7 - Pull Request
---------------------
When you are satisfied editing and previewing your article, send a pull 
request for the editors to review your article. Take a look at 
[https://help.github.com/articles/creating-a-pull-request/][11]

Step 8 - Editor Reviews
-----------------------
The pull request created in Step 7 will be examined by a reviewer who are part 
of the GLUGOT community. They will look for the following,

 * Does the article consist of any offensive material?
 * Is the article content plagiarised from some other material?
 * Improvements if any?

Depending on the above if there are no comments, your article will be merged 
to the main Geek Start repository and eventually will get published to 
[http://geekstart.tce.edu/][9]. If there are comments, then the reviewer will 
communicate the same using GitHub review mechanism which will be intimated to 
you via an email registered as part of your GitHub account.

Read more on GitHub review process in this link [https://help.github.com/articles/using-pull-requests/#reviewing-the-pull-request][12]

Step 9 - Article Published
--------------------------
The publishing to [http://geekstart.tce.edu][9] happens via an automated 
script, which runs every 3 hours and publishes the website contents as seen in 
Geek Start's master GitHub repository.

Getting Help
------------
 * Email your questions to "glugot _at_ lists _dot_ tce _dot_ edu" with
   '[geekstart]' tag on the subject line.
 * We are available in #geekstart IRC channel on irc.freenode.net

Suggested Reading
=================
 * [About GLUGOT][2]
 * [Producing Open Source Software][13]
 * [Git Tutorial][14]
 * [Pelican Documentation][15]

[1]: http://www.tce.edu/
[2]: http://glugot.tce.edu/
[3]: https://lists.tce.edu/listinfo/glugot/
[4]: https://github.com/
[5]: https://github.com/about/
[6]: https://github.com/glugot/geekstart/
[7]: https://help.github.com/articles/fork-a-repo/
[8]: https://help.github.com/articles/cloning-a-repository/
[9]: http://geekstart.tce.edu/
[10]: https://help.github.com/articles/markdown-basics/
[11]: https://help.github.com/articles/creating-a-pull-request/
[12]: https://help.github.com/articles/using-pull-requests/#reviewing-the-pull-request
[13]: http://producingoss.com/
[14]: https://git-scm.com/docs/gittutorial/
[15]: http://docs.getpelican.com/en/3.6.0/
