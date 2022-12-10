#+begin_src python :session :results file
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(3,2))
plt.plot([1,3,2])
fig.tight_layout()

fname = 'images/myfig.pdf'
plt.savefig(fname)
fname # return this to org-mode
#+end_src

#+RESULTS:
[[file:images/myfig.pdf]]
