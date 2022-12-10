#+name: savefig
#+begin_src python :var figname="plot.svg" width=5 height=5 :exports none
  return f"""plt.savefig('{figname}', width={width}, height={height})
  '{figname}'"""
#+end_src

#+header: :noweb strip-export
#+begin_src python :results value file :session :exports both
  import matplotlib, numpy
  import matplotlib.pyplot as plt
  fig=plt.figure(figsize=(4,2))
  x=numpy.linspace(-15,15)
  plt.plot(numpy.sin(x)/x)
  fig.tight_layout()
  <<savefig(figname="plot.png", width=10, height=5)>>
#+end_src
